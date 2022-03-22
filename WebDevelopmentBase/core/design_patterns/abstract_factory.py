"""An application for car management with factory method."""
from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def drive(self):
        """Drive car."""


class CarRoad(ABC):

    @abstractmethod
    def put_in(self):
        """Put your cat there."""


class Supplier(ABC):

    @abstractmethod
    def create_car(self) -> Car:
        """Create a car."""

    @abstractmethod
    def build_road(self) -> CarRoad:
        """Create road for the car."""


class PassengerCar(Car):

    def __init__(self, name: str):
        self._name = name

    def drive(self):
        print(f"""Now the car {self._name} is launching""")
        print(f"Max weight 50 kg.")

        for i in range(0, 100, 5):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class PassengerCarRoad(CarRoad):

    def put_in(self, passenger_car: PassengerCar):
        print("-"*80)
        print("This is passenger car road")
        passenger_car.drive()
        print("The way is over.")


class PassengerCarSupplier(Supplier):

    def __init__(self, name: str):
        self._name = name

    def create_car(self) -> Car:
        """Returns the passenger car."""
        return PassengerCar(name=self._name)

    def build_road(self) -> PassengerCar:
        return PassengerCarRoad()


class Truck(Car):

    def __init__(self, name: str):
        self._name = name

    def drive(self):
        print(f"""Now the car {self._name} is launching""")
        print(f"Max weight 500 kg.")

        for i in range(0, 100, 1):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class TruckRoad(CarRoad):

    def put_in(self, truck: Truck):
        print("-"*80)
        print("This is truck car road")
        truck.drive()
        print("The way is over.")


class TruckSupplier(Supplier):

    def __init__(self, name: str):
        self._name = name

    def create_car(self) -> Car:
        """Returns the passenger car."""
        return Truck(name=self._name)

    def build_road(self) -> TruckRoad:
        return TruckRoad()


class RacingCar(Car):

    def __init__(self, name: str):
        self._name = name

    def drive(self):
        print(f"""Now the car {self._name} is launching""")
        print(f"Max weight 5 kg.")

        for i in range(0, 100, 10):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class RacingCarRoad(CarRoad):

    def put_in(self, racing_car: RacingCar):
        print("-"*80)
        print("This is racing car road")
        racing_car.drive()
        print("The way is over.")


class RacingCarSupplier(Supplier):

    def __init__(self, name: str):
        self._name = name

    def create_car(self) -> Car:
        """Returns the passenger car."""
        return RacingCar(name=self._name)

    def build_road(self) -> RacingCarRoad:
        return RacingCarRoad()


class Infrastructure():

    def __init__(self, suppliers: list):
        self._suppliers = suppliers

    def launch(self):
        for supplier in self._suppliers:
            road = supplier.build_road()
            car = supplier.create_car()
            road.put_in(car)


def main():
    suppliers = [
        PassengerCarSupplier(name="Hanna"),
        TruckSupplier(name="Marry"),
        RacingCarSupplier(name="Bob"),
    ]
    infrastructure = Infrastructure(suppliers=suppliers)
    infrastructure.launch()


if __name__ == "__main__":
    main()
