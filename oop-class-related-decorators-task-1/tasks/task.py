from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(
            self,
            brand_name: str,
            year_of_issue: int,
            base_price: int,
            mileage: int
    ):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    def vehicle_type(self) -> str:
        return f'{self.brand_name} {self.__class__.__name__}'

    def is_motorcycle(self) -> bool:
        return self.wheels_num() == 2

    @abstractmethod
    def wheels_num(self) -> int:
        raise NotImplementedError()

    @property
    def purchase_price(self) -> float:
        price = self.base_price - 0.1 * self.mileage
        return price if price >= 100_000 else 100_000


# Don't change class implementation
class Car(Vehicle):
    def wheels_num(self):
        return 4


# Don't change class implementation
class Motorcycle(Vehicle):
    def wheels_num(self):
        return 2


# Don't change class implementation
class Truck(Vehicle):
    def wheels_num(self):
        return 10


# Don't change class implementation
class Bus(Vehicle):
    def wheels_num(self):
        return 6


if __name__ == '__main__':
    vehicles = (
        Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
        Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
        Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
        Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
    )

    res = [
        f"Vehicle type={v.vehicle_type()}, Is motorcycle={v.is_motorcycle()}, Purchase price={v.purchase_price}"
        for v in vehicles]

    print(res)

    assert res == ['Vehicle type=Toyota Car, Is motorcycle=False, Purchase price=985000.0',
                   'Vehicle type=Suzuki Motorcycle, Is motorcycle=True, Purchase price=796500.0',
                   'Vehicle type=Scania Truck, Is motorcycle=False, Purchase price=14915000.0',
                   'Vehicle type=MAN Bus, Is motorcycle=False, Purchase price=9905000.0']
