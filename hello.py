
def print_menu(menu):
    for name, price in menu.items():
        print(name, ":$", format(price, '.2f'))

def get_order(menu):
    orders =[]
    order = input("what would you like to order? (Q for exit)")

    while (order.upper() !='Q'):
        found =menu.get(order)
        if found:
            orders.append(order)
        else:
            print("Menu item does not exists")

        order = input("Anything else (Q for exit)")
    return orders


# main function
def main():
    print("Hello Python .......")
    menu={
        'watermalon': 50,
        'apple': 100
    }
    print_menu(menu)
    order= get_order(menu)
    print(order)


if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement
    # Some modules contain code that is intended for script use only, like parsing command-line arguments or fetching data from standard input. If a module like this was imported from a different module, for example to unit test it, the script code would unintentionally execute as well.
    main()

print("Hello from the hello python file")
