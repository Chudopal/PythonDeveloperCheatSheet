"""An application for car management"""
from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def drive(self) -> None:
        """This method allows to move car."""


class CarRoad(ABC):

    @abstractmethod
    def put_in(self, car: Car) -> None:
        """This method allows to put car into road"""


class Supplier(ABC):

    @abstractmethod
    def supply_car(self) -> Car:
        """Creates a car."""

    @abstractmethod
    def supply_road(self) -> CarRoad:
        """Creates a road."""



class PassengerCar():

    def __init__(self, name: str):
        self._name = name

    def drive(self):
        print(f"""Now the car {self._name} is launching""")
        print(f"Max weight 50 kg.")

        for i in range(0, 100, 5):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class Passenger CarRoad():

    def put_in(self, passenger_car: PassengerCar):
        print("-"*80)
        print("This is passenger car road")
        passenger_car.drive()
        print("The way is over.")


class Truck():

    def __init__(self, name: str):
        self._name = name

    def transport(self):
        print(f"""Now the car {self._name} is launching""")
        print(f"Max weight 500 kg.")

        for i in range(0, 100, 1):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class TruckRoad():

    def put_in(self, truck: Truck):
        print("-"*80)
        print("This is truck car road")
        truck.transport()
        print("The way is over.")


class RacingCar():

    def __init__(self, name: str):
        self._name = name

    def drive_fast(self):
        print(f"""Now the car {self._name} is launching""")
        print(f"Max weight 5 kg.")

        for i in range(0, 100, 10):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class RacingCarRoad():

    def put_in(self, racing_car: RacingCar):
        print("-"*80)
        print("This is racing car road")
        racing_car.drive_fast()
        print("The way is over.")


class Infrastructure():

    def __init__(self, cars: list):
        self._cars = cars

    def launch(self):
        for car in self._cars:
            if isinstance(car, PassengerCar):
                PassengerCarRoad().put_in(car)
            elif isinstance(car, Truck):
                TruckRoad().put_in(car)
            elif isinstance(car, RacingCar):
                RacingCarRoad().put_in(car)


def main():
    cars = [PassengerCar(name="Hanna"), Truck(
        name="Marry"), RacingCar(name="Bob")]
    infrastructure = Infrastructure(cars=cars)
    infrastructure.launch()


if __name__ == "__main__":
    main()
