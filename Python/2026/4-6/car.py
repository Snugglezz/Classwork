#Isaiah Hensley
#April 6th, 2026
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
def main():
    Suzuki = Car("Suzuki", "GSX-S1000GT+", 2026, "Blue")
    Toyota = Car("Toyota", "GR Supra", 2026, "Red")
    Porsche = Car("Porsche", "718 Cayman S", 2026, "Black")

    print(Suzuki.make)

if __name__ == '__main__':
    main()