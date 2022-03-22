"""An application for car management"""


class PassengerCar():

    def __init__(self, name: str):
        self._name = name

    def drive(self):
        print("-"*80)
        print(f"""Now the car {self._name} is launching""")
        print(f"Max weight 50 kg.")

        for i in range(0, 100, 5):
            print(f"{i} km.")
        
        print("""Now the car is stopping""")


class Truck():

    def __init__(self, name: str):
        self._name = name

    def drive(self):
        print("-"*80)
        print(f"""Now the car {self._name} is launching""")
        print(f"Max weight 500 kg.")

        for i in range(0, 100, 1):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class RacingCar():

    def __init__(self, name: str):
        self._name = name

    def drive(self):
        print("-"*80)
        print(f"""Now the car {self._name} is launching""")
        print(f"Max weight 5 kg.")

        for i in range(0, 100, 10):
            print(f"{i} km.")

        print("""Now the car is stopping""")


class Infrastructure():

    def __init__(self, cars: list):
        self._cars = cars

    def launch(self):
        for car in self._cars:
            car.drive()


def main():
    cars = [PassengerCar(name="Hanna"), Truck(name="Marry"), RacingCar(name="Bob")]
    infrastructure = Infrastructure(cars=cars)
    infrastructure.launch()


if __name__ == "__main__":
    main()
