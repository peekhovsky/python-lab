class Field:
    __value = None

    def __init__(self):
        self.__value = None

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value


if __name__ == '__main__':
    obj = Field()
    print(f"obj: {obj}")

    obj.set_value('val')
    print(f"obj.get_value(): {obj.get_value()}")
