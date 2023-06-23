from items import *

def printName(name):
    print(f"Hello Mr/Ms {name}...we've been waiting for you!")
    
def sqft(length, width):
    return f"Area is {length * width}sq ft"

def circumference(r):
    return f"Circumference of circle is {3.14159 * 2 * r}"

def prompt(user_prompt, err_msg, *args):
    while True:
        user_input = input(f"{user_prompt} ").lower()
        if user_input == 'f' or user_input == 'F':
            break
        if user_input in args:
            return user_input
        else:
            print(f"{err_msg}")
            continue

def int_prompt(user_prompt, err_msg, list):
    while True:
        user_input = input(f"{user_prompt} ")
        if user_input == 'f':
            return user_input
        user_input = int(user_input)
        if user_input in list:
            return user_input
        else:
            print(f"{err_msg}")
            continue       

def display_items(list, ch):
        if ch == 'r':
            print("\nThanks for shopping with Spinj's Food Delivery Service!")
        for item in list:
            if ch == 'a':
                item_info = f"{list.index(item) + 1} {item['name']} ({item['oz']})"
            elif ch == 'c' or ch == 'r':
                item_info = f"{item['count']} {item['name']} ({item['oz']})"
            elif ch == 'd':
                item_info = f"{list.index(item) + 1} {item['count']} {item['name']} ({item['oz']})"
            for num in range(len(item_info),(40 - len(str(item['price'] * item['count'])))):
                item_info += ' '
            item_info += f"...${round(item['price']*item['count'], 2)}"
            print(item_info)
        if ch == 'r':
            global total_cost
            [print(' ', end='') for num in range(0,24)]
            print(f"Total cost: ${round(total_cost, 2)}\n")

def add_item():
    user_input = prompt(f"Would you like to see Oats, Cheese, or Soda? 'F' to go back","Sorry, that's not an available option.",'oats','cheese','soda','other','o','c','s','f')
    if user_input == 'f':
        return
    elif user_input == 'oats' or user_input == 'o':
        display_items(oats, 'a')
        sec_input = int_prompt(f"Which would you like to add? 1,2,3,.. 'F' to go back ", "Please enter a valid number:", [num for num in range(1, len(oats) + 1)])
        if sec_input == 'f' or sec_input == 'F':
            return
        add_to_cart(sec_input, oats)
    elif user_input == 'cheese' or user_input == 'c':
        display_items(cheeses, 'a')
        sec_input = int_prompt(f"Which would you like to add? 1,2,3,.. 'F' to go back ", "Please enter a valid number:", [num for num in range(1, len(cheeses) + 1)])
        if sec_input == 'f' or sec_input == 'F':
            return
        add_to_cart(sec_input, cheeses)
    elif user_input == 'soda' or user_input == 's':
        display_items(sodas, 'a')
        sec_input = int_prompt(f"Which would you like to add? 1,2,3,.. 'F' to go back ", "Please enter a valid number:", [num for num in range(1, len(sodas) + 1)])
        if sec_input == 'f' or sec_input == 'F':
            return
        add_to_cart(sec_input, sodas)

def add_to_cart(i, list):
    i -= 1
    new_item = list[i].copy()
    new_count = int_prompt(f"How many of {list[i]['name']} would you like to add? 1-10 ","Please enter a valid number:", [num for num in range(1, 11)])
    if new_count == 'f':
        return
    new_item['count'] = new_count
    cart.append(new_item)
    global total_cost
    total_cost += (new_count * new_item['price'])
    print(f"{new_count} {new_item['name']} added to cart!")
    
def delete_item(list, i):
    global total_cost
    total_cost -= (list[i]['price'] * list[i]['count'])
    del list[i]
    
    
def del_display():
    display_items(cart , 'd')
    del_num = int_prompt(f"Which item would you like to delete from your cart? 'f' to cancel ")
    if del_num == 'f' or del_num =='F':
        return
    del_num -= 1
    user_confirm = prompt("Are you sure you want to remove this item? Y/N ", "Invalid Response", 'y','n')
    if user_confirm == 'n':
        return
    delete_item(cart, del_num)
    
    