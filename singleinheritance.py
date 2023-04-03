class animal:
    age = 3
    def speak(self):
        print("Speaking")

class dog(animal):
    def eat(self):
      print("Eating")

d = dog()
d.speak()

print(issubclass(dog,animal))
print(isinstance(d,dog))