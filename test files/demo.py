

class Cat:
    def __init__(self):
        self.hearts_max = 3
        self.hearts = 3
        self.willpower_max = 2
        self.willpower = 2
        self.attack = 1
        self.defense = 1
        self.weapon = Weapon('fists',1)

    def hurt_hearts(self, hearts):
        self.hearts -= hearts

    def heal_hearts(self, hearts):
        self.hearts += hearts
        if self.hearts > self.hearts_max:
            self.hearts = self.hearts_max

    def hurt_willpower(self, willpower):
        self.willpower -= willpower

    def heal_willpower(self, willpower):
        self.willpower += willpower
        if self.willpower > self.willpower_max:
            self.willpower = self.willpower_max

    def get_hearts(self):
        return self.hearts

    def get_willpower(self):
        return self.willpower

    def get_attack(self):
        self.attack = int(0.5 * (self.willpower + self.weapon.get_strength()))
        return int(self.attack)

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_willpower(self, willpower):
        self.willpower_max += willpower
        self.willpower = self.willpower_max


class Weapon:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
    def get_strength(self):
        return self.strength



bella = Cat()

print bella.weapon.name
print bella.get_attack()

bella.add_weapon(Weapon('slingshot', 13))

print bella.weapon.name
print bella.get_attack()

bella.add_willpower(1)

print bella.weapon.name
print bella.get_attack()

bella.add_weapon(Weapon('staff', 5))

print bella.weapon.name
print bella.get_attack()

bella.add_willpower(1)

print bella.weapon.name
print bella.get_attack()

bella.add_weapon(Weapon('knife', 10))

print bella.weapon.name
print bella.get_attack()

bella.add_willpower(1)

print bella.weapon.name
print bella.get_attack()
print bella.get_willpower()
