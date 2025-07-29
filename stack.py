stack = []
maxsize = int(input("Input the Max size of your stack: "))

def push():
    if len(stack) >= maxsize:
        print("Stack is full")
    else:
        item = (input("Enter the element to be pushed: "))
        stack.append(item)
        print("Element pushed to the stack", item )
def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        item = stack.pop()
        print("Element popped from the stack", item)
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements: ", stack)
def topdisplay():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element of the stack: ", stack[-1])
def bottomdisplay():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Bottom element of the stack: ", stack[0])

def displaytb():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack (top to bottom):")
        for item in reversed(stack):
            print(item)

while True:
    print("Stack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Top element")
    print("5. Bottom element")
    print("6. Stack (top to bottom)")
    print("7. Exit")
    option = (input("Enter option:"))

    if option == "1":
        push()
    elif option == "2":
        pop()
    elif option == "3":
        display()
    elif option == "4":
        topdisplay()
    elif option == "5":
        bottomdisplay()
    elif option == "6":
        displaytb()
    elif option == "7":
        print("Exiting the program...")
        break
    else:
        print("Invalid option")
