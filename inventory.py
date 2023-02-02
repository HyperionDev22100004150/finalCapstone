# Follow these steps:
# ● Code a Python program that will read from the text file inventory.txt and perform the following on the data,
#   to prepare for presentation to your managers:
# o We’ve provided a template for you in a file named inventory.py, where a Shoe class should be defined.

# o Inside this file, create a class named Shoes with the following attributes:
# ● country,
# ● code,
# ● product,
# ● cost, and
# ● quantity.
 
#========The beginning of the class==========

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
# o Inside this class define the following methods:
# ▪ get_cost - Returns the cost of the shoes.
    def get_cost(self):
        return self.cost

# ▪ get_quantity -Returns the quantity of the shoes.
    def get_quantity(self):
        return self.quantity

# ▪ __str__ - This method returns a string representation of a class.
    def __str__(self):
        return f'''{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}'''


#=============Shoe list===========

# o Outside this class create a variable with an empty list. This variable will be used to store a list of shoes objects
shoe_list = []

#==========Functions outside the class==============
# o Then you must define the following functions outside the class:

# ▪ read_shoes_data
#   This function will open the file inventory.txt and read the data from this file,
#   then create a shoes object with this data and append this object into the shoes list.
#   One line in this file represents data to create one object of shoes. 
#   You must use the try-except in this function for error handling. 
#   Remember to skip the first line using your code.
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as inventory:
            for line_nr, line in enumerate(inventory):
                if line_nr != 0:
                    country, code, product, cost, quantity = line.split(',')
                    shoe_list.append(Shoe(country, code, product, int(cost), int(quantity.replace('\n', ''))))
    except FileNotFoundError:
            print("The file that you are trying to open does not exist.")

# ▪ capture_shoes - 
#   This function will allow a user to capture data about a shoe and use this data to create a shoe object and append this object inside the shoe list.
def capture_shoes():
    print('Enter the shoe details')
    country = input('Enter the country: ')
    code = input('Enter the code: ')
    product = input('Enter the product name: ')
    cost = int(input('Enter the product cost: '))
    quantity = int(input('Enter the product quantity'))
    shoe_list.append(Shoe(country, code, product, cost, quantity))

# ▪ view_all 
#   This function will iterate over the shoes list and print the details of the shoes returned from the __str__ function. 
#   Optional: you can organise your data in a table format by using Python’s tabulate module.
def view_all():
    for shoe in shoe_list:
        print(shoe.__str__())
    

# ▪ re_stock
#   This function will find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked. 
#   Ask the user if they want to add this quantity of shoes and then update it. This quantity should be updated on the file for this shoe.
def re_stock():
    lowest_quantity = shoe_list[0].quantity
    for shoe in shoe_list:
        if shoe.quantity < lowest_quantity:
            lowest_quantity_code = shoe.code
    print('The lowest quantity shoe is: ')
    seach_shoe(lowest_quantity_code)
    update_quantity = int(input('How much do you want to add to this stock quantity? '))
    with open('inventory.txt', 'w+') as inventory:
        inventory.write('Country,Code,Product,Cost,Quantity\n')
        for shoe in shoe_list:
            if shoe.code != lowest_quantity_code:
                inventory.write(f'{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n')
            else:
                inventory.write(f'{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity + update_quantity}\n')

    


# ▪ seach_shoe - This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.
def seach_shoe(code):
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe.__str__())


# ▪ value_per_item - This function will calculate the total value for each item. 
#   Please keep the formula for value in mind; value = cost * quantity. Print this information on the console for all the shoes.
def value_per_item():
    for shoe in shoe_list:
        print(f'The {shoe.product} total value is {shoe.cost * shoe.quantity}')


# ▪ highest_qty - Write code to determine the product with the highest quantity and print this shoe as being for sale.
def highest_qty():
    highest_qty = 0
    for shoe in shoe_list:
        if shoe.quantity > highest_qty:
            shoe_for_sale = shoe.product
    print(f'The {shoe_for_sale} is for sale!')


#==========Main Menu=============

# o Now in your main create a menu that executes each function above. This menu should be inside the while loop. Be creative!

menu = '''
Shoe inventory menu

1.  Read shoes data
2.  Capture shoes
3.  View all
4.  Re-stock
5.  Search shoes
6.  Value per item
7.  Highest quantity
0.  Exit

'''

while True:
    print(menu)
    user_choice = input('Enter the menu number to use: ')
    if user_choice == '1':
        read_shoes_data()
    elif user_choice == '2':
        capture_shoes()
    elif user_choice == '3':
        view_all()
    elif user_choice == '4':
        re_stock()
    elif user_choice == '5':
        code = input('Enter the shoe code to search: ')
        seach_shoe(code)
    elif user_choice == '6':
        value_per_item()
    elif user_choice == '7':
        highest_qty()
    elif user_choice == '0':
        break
    else:
        print('Invalid menu selection, please try again.')
