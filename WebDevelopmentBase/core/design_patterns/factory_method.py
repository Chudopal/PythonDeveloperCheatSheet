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


class CarShop(ABC):

    @abstractmethod
    def create_car(self, name: str) -> Car:
        """Create a car."""


class CarRoadBuilder(ABC):

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


class PassengerCarShop(CarShop):

    def create_car(self, name: str) -> Car:
        """Returns the passenger car."""
        return PassengerCar(name=name)


class PassengerCarRoadBuilder():

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


class TruckShop(CarShop):

    def create_car(self, name: str) -> Car:
        """Returns the passenger car."""
        return Truck(name=name)


class TruckRoadBuilder(CarRoadBuilder):

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


class RacingCarShop(CarShop):

    def create_car(self, name: str) -> Car:
        """Returns the passenger car."""
        return RacingCar(name=name)


class RacingCarRoadBuilder(CarRoadBuilder):

    def build_road(self) -> RacingCarRoad:
        return RacingCarRoad()


class Infrastructure():

    def __init__(self, cars: list):
        self._cars = cars

    def launch(self):
        for car in self._cars:
            if isinstance(car, PassengerCar):
                PassengerCarRoadBuilder().build_road().put_in(car)
            elif isinstance(car, Truck):
                TruckRoadBuilder().build_road().put_in(car)
            elif isinstance(car, RacingCar):
                RacingCarRoadBuilder().build_road().put_in(car)


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
