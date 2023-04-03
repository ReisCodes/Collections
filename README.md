# Lists Task 
### Create a list of things a millionaire would buy

```python
buy_list = ["Private Jet", "Mansion", "Super Car", "Private Chef", "An Island"]
```

### Printing elements from this using indexing
To print out individual elements from the list you can index the item you wish to 
print using `[]` brackets.

```python
print(buy_list[0])
print(buy_list[1])
print(buy_list[-1])
```

### Replacing items within the list 
To replace items within a list you have to use indexing to show python which item you would like 
to replace and then assign it to its new variable by equating it as shown below:

```python
buy_list[0] = "Yacht"

buy_list[2] = "Super Bike"
```

### Adding and Replacing items 
adding and replacing items from a list both make use of list methods, the first being `.append()`. This method will
add another element to the list. 

```python
buy_list.append("A Doberman puppy")
```
The way to remove an item can be done by the `.remove()` method,
which requires you to state the item to remove, or you can use the 
`.pop()` method which automatically removes the last item from the list.

```python
buy_list.remove("Yacht")
buy_list.pop()
```

## User Story
The Goals of the user story were: 

- As a user, I want to be able to see the menu in a formatted way so that I can order my meal.

- As a user, I want to be able to order three separate times and have my responses added to a list, 
so they are not forgotten.

- As a user, I want to have my order read back to me in a formatted way, so I know what I ordered.

### Empty List
To start this user story it is essential to start with an empty list to append the 
user options to it later in the program.

```python
order = []
```

### Printed menu and User choices
The menu is printed with triple quotation marks to allow it to be displayed in an easy-to-read manner 
for the user. The program then asks for the users input on their selection of starter, main, dessert and drink. These 
options are then appended to the empty list stated earlier.

```python
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
```

### Displaying User Options 
The use of f-strings and list indexing means the user options can be easily
displayed back to the user. 

```python
print(f'''Here is your order:
Starter: {order[0]}
Main:    {order[1]}
Dessert: {order[2]}
Drink:   {order[3]}
Thank you so much for ordering with us, we hope you enjoy your meal!''')
```

# Dictionary

### Defining a dictionary 

```python
story1 = {"start": "There once was a boy who was an orphan, raised by a pack of  Wolves.",
          "middle": "He must fight for his and his families lives as their home is threatened by raging hippos",
          "end": "The boy shows great strength and resolve earning the respect of the hippos and saving his family"}

```

### Printing: the entire dictionary, its Type, Keys and Values
printing the entire dictionary just makes use of the `print()` statement, similarly its type can be found
by using the `type()` function. Printing the dictionary's Keys and Values combines a `print()` statement
with 2 dictionary methods, `.keys()` & `values()`.

```python
print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())
```

### Printing individual Values
Using a `for ... in ...` statement you can loop through the values of the dictionary to print its individual values.

```python
for key in story1:
    print(story1[key])
```

### Adding a new key:value pair 
adding a new key:value pair to your dictionary is achieved by stating your dictionary name
using `[]` to define your key and equating it to the value you want to assign it as shown below:

```python
story1["hero"] = "Wolf Boy"
```