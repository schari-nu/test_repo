def hello():
    print("Hello")



hello()
hello()
hello()

def hello_name(name):
    print(f"Hi There {name}")


hello_name("Jack")
hello_name("Sandra")

# Functions can have more than one parameter
def make_quesadilla(protein, topping):
    # Define: This function prepares quasadill
    #Parameters:
    #1. Protin - Such as 
    #2. Topping
    quesadilla = f"Here is a {protein} quesadilla with {topping} topping"
    print(quesadilla)


make_quesadilla("beef", "guacamole")
make_quesadilla("chicken", "salsa")
make_quesadilla("cheese", "grilled Vegetables")    

make_quesadilla( "guacamole", "beef")


def square(number):
    return number * number

ans = square(5)
print(f"square of 5 is {ans}")
print(square(2))

