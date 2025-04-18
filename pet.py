class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Scale from 0 (not hungry) to 10 (very hungry)
        self.energy = 5  # Scale from 0 (exhausted) to 10 (full of energy)
        self.happiness = 5  # Scale from 0 (sad) to 10 (very happy)
        self.tricks = []

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 1
            self.energy += 1
            print(f"{self.name} has eaten. Hunger level: {self.hunger}")
        else:
            print(f"{self.name} is not hungry.")

    def sleep(self):
        self.energy = 10
        print(f"{self.name} has slept and restored energy.")

    def play(self):
        if self.energy > 0 and self.hunger < 10:
            self.energy -= 1
            self.happiness += 1
            self.hunger += 1
            print(f"{self.name} played and is now happier! Happiness level: {self.happiness}")
        else:
            print(f"{self.name} is too tired or hungry to play.")

    def get_status(self):
        return {
            "name": self.name,
            "hunger": self.hunger,
            "energy": self.energy,
            "happiness": self.happiness
        }

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness += 1
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            return f"{self.name} knows the following tricks: {', '.join(self.tricks)}"
        else:
            return f"{self.name} hasn't learned any tricks yet."