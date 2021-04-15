import controller as con

def constant_order():
    return con.constant_order()

def linear_order():
    return con.linear_order()

def quadratic_order():
    return con.quadratic_order()


def menu():
    print("1. Constant")
    print("2. Linear")
    print("3. Quadratic")
    print("4. salir")


end = True
while end :
    menu()
    option =int(input("Digite su opcion: "))
    if option == 1:
        print(constant_order())
    elif option == 2:
        print(linear_order())
    elif option == 3:
        print(quadratic_order())
    else:
        end = False 

print("hello")
