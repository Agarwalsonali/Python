class Animals:
    def legs(self):
        print("Almost all animals have four legs")


class Pets(Animals):
    print("Pets are the animlals which we can kept in home")


class Dog(Pets):

    @staticmethod
    def bark():
        print("Dogs express their emotions using barking.")


d1 = Dog()
d1.bark()