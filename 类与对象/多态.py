class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


"""构建抽象类"""

class AC:
    def cool_wind(self):    # 制冷
        pass

    def hot_wind(self):     # 制热
        pass

    def swing_l_r(self):    # 左右送风
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的制冷")

    def hot_wind(self):
        print("美的制热")

    def swing_l_r(self):
        print("美的送风")


class Gree_AC(AC):
    def cool_wind(self):
        print("格力制冷")

    def hot_wind(self):
        print("格力制热")

    def swing_l_r(self):
        print("格力送风")

def make_cool(ac: AC):
    ac.cool_wind()


midea = Midea_AC()
gree = Gree_AC()


make_cool(midea)
make_cool(gree)