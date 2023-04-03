w = 3
z = 24


def add (w, z):
    return w + z

def subtract (z, w):
    return z - w

def divide (z, w):
    return z / w

def multiply (z, w):
    return z * w

print("Choose an operation")
print("1.Add")
print("2.Subtract")
print("3.Divide")
print("4.Multiply")

choice = input("Enter Choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    try:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
    except ValueError:
        print("Please enter a number.")


        if choice == '1' :
            print('w', "+" , 'z' , "=", add(w,z))

        elif choice == '2' :
            print( 'z', "-", 'w' , "=", subtract(z,w))

        elif choice == '3' :
            print( 'z', "/", 'w', "=", divide(z,w))

        elif choice == '4' :
            print( 'z', "*", "w", "=", multiply(z,w))





