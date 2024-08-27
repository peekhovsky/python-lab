class Bird:
    def __init__(self, name):
        print(f'\nName: {name}')
        self.name = name

    def walk(self):
        return f"{self.name} bird can walk"

    def __str__(self):
        return f"{self.name} bird can walk"


class FlyingBird(Bird):
    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration

    def fly(self):
        return f"{self.name} bird can fly"

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class NonFlyingBird(Bird):
    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can walk and swim"


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"


if __name__ == '__main__':
    b = Bird("Any")
    res = b.walk()
    print(f'res={res}')
    assert res == "Any bird can walk"

    p = NonFlyingBird("Penguin", "fish")
    res = p.swim()
    print(f'res={res}')
    assert res == "Penguin bird can swim"
    res = p.eat()
    print(f'res={res}')
    assert res == "It eats mostly fish"

    c = FlyingBird("Canary")
    res = str(c)
    print(f'res={res}')
    assert res == "Canary bird can walk and fly"
    res = c.eat()
    print(f'res={res}')
    assert res == "It eats mostly grains"

    s = SuperBird("Gull")
    res = str(s)
    print(f'res={res}')
    assert res == "Gull bird can walk, swim and fly"
    res = s.eat()
    print(f'res={res}')
    assert res == "It eats mostly fish"

    # print(SuperBird.__mro__)
