menu_price = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main ():
    total_price = 0
    while True :
        try :
            menu_input = input("Item: ").title()
            if menu_input not in menu_price :
                continue
        except EOFError :
                break
        else :
            total_price += menu_price.get(menu_input)
            print (f"Total: ${total_price:.2f}")

main ()
