class Superhero:
    def __init__(self, name, power, weakness, level=1):
        self.name = name
        self.power = power
        self.weakness = weakness
        self.level = level
        self.experience = 0

    def display_status(self):
        print(f" Name: {self.name}")
        print(f" Power: {self.power}")
        print(f" Weakness: {self.weakness}")
        print(f" Level: {self.level}")
        print(f" Experience: {self.experience}")

    def fight_crime(self, difficulty):
        print(f"{self.name} is fighting a crime of difficulty {difficulty}!")
        self.experience += difficulty * 10
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        print(f" {self.name} leveled up! Now at level {self.level}!")



