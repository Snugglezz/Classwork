class Bank:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
class Smartphone:
    def __init__(self, brand, model, color, length, name):
        self.brand = brand
        self.model = model
        self.color = color
        self.length = length
        self.name = name
def main():
    IOS = Smartphone("Apple", 13, "Red", 6.12, "Iphone 13")
    Android = Smartphone("Sameung", "A36", "Black", 6.41, "Samsung Galaxy A36 5G")
    Google = Smartphone("Google", 10, "Green", 6.0, "Google Pixel 10 Pro")
    print(IOS.brand, IOS.model, IOS.color, IOS.length, IOS.name)
    print(Android.brand, Android.model, Android.color, Android.length, Android.name)
    print(Google.brand, Google.model, Google.color, Google.length, Google.name)
if __name__ == '__main__':
    main()