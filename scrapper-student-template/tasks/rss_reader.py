import json
import xml.etree.ElementTree as ET
from abc import abstractmethod
from argparse import ArgumentParser
from typing import List, Optional, Sequence, Dict

import requests

test_rss = 'https://practicaldatascience.co.uk/feed.xml'
test_file_name = 'test.xml'


def xml_to_string(xml_file_path: str):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    xml_string = ET.tostring(root, encoding="utf-8", method="xml")
    return xml_string.decode("utf-8")


def flat(lst: List):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flat(item))
        else:
            flat_list.append(item)
    return flat_list


class MissingRequiredTagsException(Exception):
    def __init__(self, *tag_names):
        self.message = f"Missing required tags: {', '.join(tag_names)}"
        super().__init__(self.message)


class RssViewBuilder:
    def __init__(self, root_tag):
        self.root_tag = root_tag

    @staticmethod
    def builder(root_tag, is_json: bool = False):
        return JsonRssViewBuilder(root_tag) if is_json else LineRssViewBuilder(
            root_tag)

    def with_tags(self, named_tags: Dict[str, str], is_required=False):
        for name, tag_name in named_tags.items():
            tag = self.root_tag.find(tag_name)

            if tag is not None:
                self._add_tag(name, tag_name, tag.text)
            elif is_required:
                raise MissingRequiredTagsException(tag_name)

    @abstractmethod
    def with_join_tags(self, name, tag_name):
        raise NotImplementedError()

    def with_object(self, name, obj):
        if obj is not None:
            self._add_object(name, obj)

    def with_desc(self):
        tag = self.root_tag.find("description")
        if tag is not None:
            self._add_desc(tag.text)

    @abstractmethod
    def build(self):
        raise NotImplementedError()

    @abstractmethod
    def get_lines(self):
        raise NotImplementedError()

    @abstractmethod
    def _add_tag(self, name, tag_name, tag_text):
        raise NotImplementedError()

    @abstractmethod
    def _add_object(self, name, obj):
        raise NotImplementedError()

    @abstractmethod
    def _add_desc(self, tag_text):
        raise NotImplementedError()


class LineRssViewBuilder(RssViewBuilder):
    def __init__(self, root_tag):
        super().__init__(root_tag)
        self.result = []

    def build(self):
        return self.result

    def get_lines(self):
        return self.result

    def with_join_tags(self, name, tag_name):
        tags = self.root_tag.findall(tag_name)
        if len(tags):
            tag_text = ', '.join(list(map(lambda el: el.text, tags)))
            self._add_tag(name, tag_name, tag_text)

    def _add_tag(self, name, tag_name, tag_text=""):
        self.result.append(f"{name}: {tag_text}")

    def _add_object(self, name, obj):
        if isinstance(obj, list):
            self.result.append("")
            for item in obj:
                self._add_object(name, item)
        else:
            self.result.append(obj)

    def _add_desc(self, tag_text=""):
        self.result.append("")
        self.result.append(tag_text)


class JsonRssViewBuilder(RssViewBuilder):
    def __init__(self, root_tag):
        super().__init__(root_tag)
        self.json = {}

    def build(self):
        return self.json

    def get_lines(self):
        return json.dumps(self.json, indent=2).splitlines()

    def with_join_tags(self, name, tag_name):
        tags = self.root_tag.findall(tag_name)
        tag_texts = list(map(lambda el: el.text, tags))
        if len(tag_texts):
            self._set_property(tag_name, tag_texts)

    def _add_tag(self, name, tag_name, tag_text):
        self._set_property(tag_name, tag_text)

    def _add_object(self, name, obj):
        if obj is not None:
            self._set_property(name, obj)

    def _add_desc(self, tag_text):
        self._add_tag("description", "description", tag_text)

    def _set_property(self, prop_name: str, value):
        self.json[prop_name] = value


def parse_news_item(item, is_json: bool):
    builder = RssViewBuilder.builder(item, is_json)
    builder.with_tags({
        "Title": "title",
        "Author": "author",
        "Published": "pubDate",
        "Link": "link"
    })
    builder.with_join_tags("Categories", "category")
    builder.with_desc()

    return builder.build()


# keep signature
def rss_parser(
        xml: str,
        limit: Optional[int] = None,
        json: bool = False,
) -> List[str]:
    root = ET.fromstring(xml)
    channel_tag = root.find('.//channel')

    builder = RssViewBuilder.builder(channel_tag, json)
    builder.with_tags({
        "Feed": "title",
        "Link": "link",
    }, is_required=True)
    builder.with_tags({
        "Last Build Date": "lastBuildDate",
        "Publish Date": "pubDate",
        "Language": "language",
    })
    builder.with_join_tags("Categories", "category")
    builder.with_tags({"Editor": "managinEditor"})
    builder.with_tags({"Description": "description"}, is_required=True)

    news_tags = channel_tag.findall('.//item')
    news_len = len(news_tags) if limit is None else min(limit, len(news_tags))

    news = [parse_news_item(news_tags[i], json) for i in range(0, news_len)]
    if len(news):
        builder.with_object("items", news)

    return builder.get_lines()


# keep signature
def main(argv: Optional[Sequence] = None):
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided",
        type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text

    try:
        res = rss_parser(xml, args.limit, args.json)
        print("\n".join(res))
        return 0
    except MissingRequiredTagsException as e:
        print(f"Error: {e.message}")


if __name__ == "__main__":
    main()
