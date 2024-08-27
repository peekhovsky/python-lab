from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


# Query data with column selection and filters
def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    selected_data = selector(data)

    for filter_by_field in filters:
        selected_data = filter_by_field(selected_data)

    return selected_data


# Return function that selects only specific columns from dataset
def select(*columns: str) -> ModifierFunc:
    def filter_by_columns(data):
        selected_data = []

        for data_line in data:
            selected_line = {}

            for column in columns:
                if column in data_line:
                    selected_line.update({column: data_line[column]})

            selected_data.append(selected_line)

        return selected_data

    return filter_by_columns


# Return function that filters specific column to be one of `values`
def field_filter(column: str, *values: Any) -> ModifierFunc:
    def filter_by_field(data: DataType):
        return [data_line for data_line in data if data_line.get(column) in values]

    return filter_by_field


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    print(value)
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()
