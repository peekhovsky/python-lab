class Pagination:
    def __init__(self, data, items_on_page: int):
        self.data = data
        self.items_on_page = items_on_page
        pass

    @property
    def page_count(self):
        return len(self.data) // self.items_on_page + 1

    @property
    def item_count(self):
        return len(self.data)

    def count_items_on_page(self, page_number):
        return len(self.display_page(page_number))

    def find_page(self, data_slice):
        page_indexes1 = set([i for i in range(0, self.page_count)
                             if data_slice in self.display_page(i)])

        split_indexes = [list(range(i, i + len(data_slice)))
                         for i in range(0, len(self.data))
                         if self.data.startswith(data_slice, i)]

        page_indexes2 = set(map(lambda index: self.get_page_num(index), self.__flat(split_indexes)))

        result = list(page_indexes1 | page_indexes2)

        if not result:
            raise Exception(f"'{data_slice}' is missing on the pages")

        return result

    @staticmethod
    def __flat(data):
        return [num for item in data for num in item]

    def get_page_num(self, index: int):
        return index // self.items_on_page

    def display_page(self, page_number):
        if page_number >= self.page_count:
            raise Exception('Invalid index. Page is missing.')

        start = page_number * self.items_on_page
        end = start + self.items_on_page
        return self.data[start:end]


if __name__ == '__main__':
    pages = Pagination('Your beautiful text', 5)
    print(f'page_count={pages.page_count}')
    assert pages.page_count == 4
    print(f'item_count={pages.item_count}')
    assert pages.item_count == 19

    print(f'count_items_on_page(0)={pages.count_items_on_page(0)}')
    assert pages.count_items_on_page(0) == 5

    print(f'count_items_on_page(3)={pages.count_items_on_page(3)}')
    assert pages.count_items_on_page(3) == 4

    # pages.count_items_on_page(4)
    # Exception: Invalid index. Page is missing.

    print(f'pages.find_page("Your")={pages.find_page("Your")}')
    assert pages.find_page('Your') == [0]

    print(f'count_find_page("e")={pages.find_page("e")}')
    assert pages.find_page('e') == [1, 3]

    print(f'find_page("beautiful")={pages.find_page("beautiful")}')
    assert pages.find_page('beautiful') == [1, 2]
    # assert pages.find_page('great')
    # Exception: 'great' is missing on the pages
    assert pages.display_page(0) == 'Your '
