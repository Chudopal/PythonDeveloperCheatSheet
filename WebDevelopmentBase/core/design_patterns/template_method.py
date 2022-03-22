"""An application for car management with factory method."""
from abc import ABC, abstractmethod


class DriveStrategy(ABC):

    def execute(self, name: str):
        self.print_car_info(name=name)
        self.print_weight()
        self.drive()
        self.stop()

    def print_car_info(self, name: str):
        print(f"""Now the car {name} is launching""")

    @abstractmethod
    def print_weight(self):
        """Print the car weight."""

    @abstractmethod
    def drive(self):
        """Drive the car."""

    def stop(self):
        print("""Now the car is stopping""")

class Car():

    def __init__(self, name: str, strategy: DriveStrategy):
        self._strategy = strategy
        self._name = name

    def drive(self):
        """Drive car."""
        self._strategy.execute(self._name)


class CarRoad(ABC):

    def put_in(self, car: Car):
        """Put your car there."""
        self.separate()
        self.print_road_kind()
        self.drive(car)
        self.end()

    def separate(self):
        print("-"*80)

    @abstractmethod
    def print_road_kind(self):
        """Printing the road kind."""

    def drive(self, car: Car):
        car.drive()

    def end(self):
        print("The way is over.")


class Supplier(ABC):

    @abstractmethod
    def create_car(self) -> Car:
        """Create a car."""

    @abstractmethod
    def build_road(self) -> CarRoad:
        """Create road for the car."""


class PassengerCarDriveStrategy(DriveStrategy):

    def print_weight(self):
        print(f"Max weight 50 kg.")

    def drive(self):
        for i in range(0, 100, 5):
            print(f"{i} km.")


class PassengerCarRoad(CarRoad):

    def print_road_kind(self):
        print("This is passenger car road")


class PassengerCarSupplier(Supplier):

    def __init__(self, name: str):
        self._name = name

    def create_car(self) -> Car:
        """Returns the passenger car."""
        return Car(name=self._name, strategy=PassengerCarDriveStrategy())

    def build_road(self) -> PassengerCarRoad:
        return PassengerCarRoad()



class TruckDriveStrategy(DriveStrategy):

    def print_weight(self):
        print(f"Max weight 500 kg.")


    def drive(self):
        for i in range(0, 100, 1):
            print(f"{i} km.")



class TruckRoad(CarRoad):

    def print_road_kind(self):
        print("This is truck road")


class TruckSupplier(Supplier):

    def __init__(self, name: str):
        self._name = name

    def create_car(self) -> Car:
        """Returns the passenger car."""
        return Car(name=self._name, strategy=PassengerCarDriveStrategy())

    def build_road(self) -> TruckRoad:
        return TruckRoad()


class RacingCarDriveStrategy(DriveStrategy):

    def print_weight(self):
        print(f"Max weight 5 kg.")


    def drive(self):
        for i in range(0, 100, 10):
            print(f"{i} km.")


class RacingCarRoad(CarRoad):

    def print_road_kind(self):
        print("This is racing car road")


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
