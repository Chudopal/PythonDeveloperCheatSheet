"""An application for car management with factory method."""
from abc import ABC, abstractmethod


class DriveStrategy(ABC):

    @abstractmethod
    def execute(self, name: str):
        pass


class Car():

    def __init__(self, name: str, strategy: DriveStrategy):
        self._strategy = strategy
        self._name = name

    def drive(self):
        """Drive car."""
        self._strategy.execute(self._name)


class CarRoad(ABC):

    @abstractmethod
    def put_in(self):
        """Put your car there."""


class Supplier(ABC):

    @abstractmethod
    def create_car(self) -> Car:
        """Create a car."""

    @abstractmethod
    def build_road(self) -> CarRoad:
        """Create road for the car."""


class PassengerCarDriveStrategy(DriveStrategy):

    def execute(self, name: str):
        print(f"""Now the car {name} is launching""")
        print(f"Max weight 50 kg.")

        for i in range(0, 100, 5):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class PassengerCarRoad(CarRoad):

    def put_in(self, car: Car):
        print("-"*80)
        print("This is passenger car road")
        car.drive()
        print("The way is over.")


class PassengerCarSupplier(Supplier):

    def __init__(self, name: str):
        self._name = name

    def create_car(self) -> Car:
        """Returns the passenger car."""
        return Car(name=self._name, strategy=PassengerCarDriveStrategy())

    def build_road(self) -> PassengerCarRoad:
        return PassengerCarRoad()



class TruckDriveStrategy(DriveStrategy):

    def execute(self, name: str):
        print(f"""Now the car {name} is launching""")
        print(f"Max weight 500 kg.")

        for i in range(0, 100, 1):
            print(f"{i} km.")

        print("""Now the car is stopping""")



class TruckRoad(CarRoad):

    def put_in(self, car: Car):
        print("-"*80)
        print("This is truck car road")
        car.drive()
        print("The way is over.")


class TruckSupplier(Supplier):

    def __init__(self, name: str):
        self._name = name

    def create_car(self) -> Car:
        """Returns the passenger car."""
        return Car(name=self._name, strategy=PassengerCarDriveStrategy())

    def build_road(self) -> TruckRoad:
        return TruckRoad()


class RacingCarDriveStrategy(DriveStrategy):

    def execute(self, name: str):
        print(f"""Now the car {name} is launching""")
        print(f"Max weight 5 kg.")

        for i in range(0, 100, 10):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class RacingCarRoad(CarRoad):

    def put_in(self, car: Car):
        print("-"*80)
        print("This is racing car road")
        car.drive()
        print("The way is over.")


class RacingCarSupplier(Supplier):

    def __init__(self, name: str):
        self._name = name

    def create_car(self) -> DriveStrategy:
        """Returns the passenger car."""
        return Car(name=self._name, strategy=RacingCarDriveStrategy())

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
