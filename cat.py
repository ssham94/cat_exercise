class Cat:
    def __init__(self, name, preferred_food, meal_time):
        self.full_name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return f"{self.full_name} likes to eat {self.preferred_food} around {self.meal_time}"

    def eats_at(self):
        if self.meal_time > 12:
            return f"{self.meal_time - 12} PM"
        elif self.meal_time == 12:
            return(f"{self.meal_time} PM")
        else:
            return f"{self.meal_time} AM"
    
    def meow(self):
        return f"My name is {self.full_name} and I eat {self.preferred_food} at {self.eats_at()}"

jarvey = Cat('Jarvey', 'Tuna', 12)
shadow = Cat('Shadow', 'Salmon', 15)
tubby = Cat('Tubby', 'Chicken', 9)

# Testing that they have been instanciated correctly
print(jarvey)
print(shadow)
print(tubby)

# Testing to see that the eats_at method is working correctly
print(jarvey.eats_at())
print(shadow.eats_at())
print(tubby.eats_at())

# Testing to see if the meow method is working correctly
print(jarvey.meow())
print(shadow.meow())
print(tubby.meow())