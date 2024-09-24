class Robot:
    species = "robot"
    def __init__(self, name, fav):
        self.name = name
        self.fav = fav
    def intro(self):
        print("Hello, my name is {}. My favorite robot is {}.".format(self.name, self.fav))
tom = Robot("Tom", "Jerry")
jerry = Robot("Jerry", "Tom")
print("Tom is a {}".format(tom.species))
print("Jerry is also a {}".format(jerry.species))
tom.intro()
jerry.intro()
class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def introduce(self):
        print("Hello! My name is {self.name} and I am a {self.model} robot.")    
    def move(self):
        print("{self.name} is moving...")
    def perform_task(self, task):
        print("{self.name} is performing task: {task}")
my_robot = Robot("Robo1", "humanoid")
my_robot.introduce()
my_robot.move()
my_robot.perform_task("cleaning")