starters = ["garlic bread", "calamari", "cheese balls", "prawn cocktail", "soup"]
mains = ["spaghetti alfredo", "hunters chicken", "sausage and mash", "burger and chips", "steak"]
desserts = ["chocolate cake", "eton mess", "cheesecake", "victoria sponge", "sticky toffee pudding"]

order = []

print('''
Starters:         
garlic bread      
calamari
cheese balls
prawn cocktail
soup
''')

starter_choice = input('''What starter would you like to order? 
                       : ''')
order.append(starter_choice)

print('''
Mains:         
spaghetti alfredo      
hunters chicken
sausage and mash
burger and chips
steak
''')

main_choice = input('''What main would you like to order? 
                       : ''')
order.append(main_choice)

print('''
Desserts:         
chocolate cake      
eton mess
cheesecake
victoria sponge
sticky toffee pudding
''')

dessert_choice = input('''What dessert would you like to order? 
                       : ''')
order.append(dessert_choice)

print('''
Drinks:         
water      
coke
lemonade
beer
wine
''')

drink_choice = input('''What drink would you like to order? 
                       : ''')
order.append(drink_choice)

print(f'''Here is your order:
Starter: {order[0]}
Main:    {order[1]}
Dessert: {order[2]}
Drink:   {order[3]}
Thank you so much for ordering with us, we hope you enjoy your meal!''')
