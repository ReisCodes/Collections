starters = ["garlic bread", "calamari", "cheese balls", "prawn cocktail", "soup"]
mains = ["spaghetti alfredo", "hunters chicken", "sausage and mash", "burger and chips", "steak"]
desserts = ["chocolate cake", "eton mess", "cheesecake", "victoria sponge", "sticky toffee pudding"]
drinks = ["water", "coke", "lemonade", "beer", "wine"]

order = []

print("Starters:")
for starter in starters:
    print(starter)

while True:
    starter_choice = input('''What starter would you like to order? 
                       : ''')
    if starter_choice not in starters:
        print("This isn't a valid option, please try again")
    else:
        order.append(starter_choice)
        break

print("Mains:")
for main in mains:
    print(main)

while True:
    main_choice = input('''What main would you like to order? 
                       : ''')
    if main_choice not in mains:
        print("This isn't a valid option, please try again")
    else:
        order.append(main_choice)
        break

print("Desserts:")
for dessert in desserts:
    print(dessert)

while True:
    dessert_choice = input('''What dessert would you like to order? 
                       : ''')
    if dessert_choice not in desserts:
        print("This isn't a valid option, please try again")
    else:
        order.append(dessert_choice)
        break

print("Drinks:")
for drink in drinks:
    print(drink)

while True:
    drink_choice = input('''What drink would you like to order? 
                       : ''')
    if drink_choice not in drinks:
        print("This isn't a valid option, please try again")
    else:
        order.append(drink_choice)
        break

print(f'''Here is your order:
Starter: {order[0]}
Main:    {order[1]}
Dessert: {order[2]}
Drink:   {order[3]}
Thank you so much for ordering with us, we hope you enjoy your meal!''')
