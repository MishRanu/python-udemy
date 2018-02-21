class Duck:

    def walk(self):
        print("waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water is lovely")

    def quack(self):
        print("Quack quack")


class Penguin:

    def walk(self):
        print("waddle, waddle, I waddle too")

    def swim(self):
        print("come on in, but it is a bit chilly this far south")

    def quack(self):
        print("Are you 'avin; a larf? I am a penguin ")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == "__main__":
    donald = Duck()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)