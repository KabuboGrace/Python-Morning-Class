# Local variable
def car():
    x = "volvo"
    del x
    print(x)

car()

# Global variable

y = "phone"
def device():
    global y
    print(y)

device()