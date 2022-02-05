class Wizard:
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def change_rating(self, value):
        if self.rating + value > 100:
            self.rating = 100
        elif self.rating + value < 1:
            self.rating = 1
        else:
            self.rating += value

        if value > 0:
            if (self.age - value // 10) < 18:
                self.age = 18
            else:
                self.age -= value // 10
        else:
            self.age += abs(value) // 10

    def __add__(self, other):
        if isinstance(other, str):
            if self.rating + len(other) > 100:
                self.rating = 100
            else:
                self.rating += len(other)

            if self.age - len(other) // 10 < 18:
                self.age = 18
            else:
                self.age -= len(other) // 10

            return self

    def __call__(self, x):
        return (x - self.age) * self.rating

    def __str__(self):
        return f"Wizard {self.name} with {self.rating} rating looks {self.age} years old"

    def __eq__(self, other):
        return [self.rating, self.age, self.name] == [other.rating, other.age, other.name]

    def __ne__(self, other):
        return [self.rating, self.age, self.name] != [other.rating, other.age, other.name]

    def __gt__(self, other):
        return [self.rating, self.age, self.name] > [other.rating, other.age, other.name]

    def __ge__(self, other):
        return [self.rating, self.age, self.name] >= [other.rating, other.age, other.name]

    def __lt__(self, other):
        return [self.rating, self.age, self.name] < [other.rating, other.age, other.name]

    def __le__(self, other):
        return [self.rating, self.age, self.name] <= [other.rating, other.age, other.name]
