"""An application for car management with factory method."""
from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def drive(self):
        """Drive car."""


class CarShop(ABC):

    @abstractmethod
    def create_car(self, name: str) -> Car:
        """Create a car."""


class PassengerCar(Car):

    def __init__(self, name: str):
        self._name = name

    def drive(self):
        print("-"*80)
        print(f"""Now the car {self._name} is launching""")
        print(f"Max weight 50 kg.")

        for i in range(0, 100, 5):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class PassengerCarShop(CarShop):

    def create_car(self, name: str) -> Car:
        """Returns the passenger car."""
        return PassengerCar(name=name)


class Truck(Car):

    def __init__(self, name: str):
        self._name = name

    def drive(self):
        print("-"*80)
        print(f"""Now the car {self._name} is launching""")
        print(f"Max weight 500 kg.")

        for i in range(0, 100, 1):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class TruckShop(CarShop):

    def create_car(self, name: str) -> Car:
        """Returns the passenger car."""
        return Truck(name=name)


class RacingCar(Car):

    def __init__(self, name: str):
        self._name = name

    def drive(self):
        print("-"*80)
        print(f"""Now the car {self._name} is launching""")
        print(f"Max weight 5 kg.")

        for i in range(0, 100, 10):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class RacingCarShop(CarShop):

    def create_car(self, name: str) -> Car:
        """Returns the passenger car."""
        return RacingCar(name=name)


class Infrastructure():

    def __init__(self, cars: list):
        self._cars = cars

    def launch(self):
        for car in self._cars:
            car.drive()


def main():
    cars = [
        PassengerCarShop().create_car(name="Hanna"),
        TruckShop().create_car(name="Marry"),
        RacingCarShop().create_car(name="Bob")
    ]
    infrastructure = Infrastructure(cars=cars)
    infrastructure.launch()


if __name__ == "__main__":
    main()
