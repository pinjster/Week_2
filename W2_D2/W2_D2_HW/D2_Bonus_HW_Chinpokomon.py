import random


furrycat = {
    "name" : "Furrycat",
    "level" : 6,
    "health" : 100,
    "atk" : [8, 8 , 8 , 8 , 8, 7, 7, 7, 7 ,7, 7, 6, 10, 10]
}
pengin = {
    "name" : "Pengin",
    "level" : 4,
    "health" : 400,
    "atk" : [4, 4, 4, 4, 5, 5, 5, 7, 7, 10]
}
shoe = {
    "name" : "Shoe",
    "level" : 10,
    "health" : 500,
    "atk" : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 2, 2, 50]
}
donkeytron = {
    "name" : "Donkeytron",
    "level" : 3,
    "health" : 100,
    "atk" : [8, 8 , 8 , 8 , 8, 7, 7, 7, 7 ,7, 7, 6, 10, 10]
}
roo_stor = {
    "name" : "Roo-stor",
    "level" : 4,
    "health" : 100,
    "atk" : [8, 8 , 8 , 8 , 8, 7, 7, 7, 7 ,7, 7, 6, 10, 10]
}
accountafish = {
    "name" : "Accountafish",
    "level" : 5,
    "health" : 100,
    "atk" : [8, 8 , 8 , 8 , 8, 7, 7, 7, 7 ,7, 7, 6, 10, 10]
}
monkay = {
    "name" : "Monkay",
    "level" : 6,
    "health" : 100,
    "atk" : [8, 8 , 8 , 8 , 8, 7, 7, 7, 7 ,7, 7, 6, 10, 10]
}
lambtron = {
    "name" : "Lambtron",
    "level" : 8,
    "health" : 100,
    "atk" : [8, 8 , 8 , 8 , 8, 7, 7, 7, 7 ,7, 7, 6, 10, 10]
}
roidrat = {
    "name" : "Roidrat",
    "level" : 9,
    "health" : 100,
    "atk" : [8, 8 , 8 , 8 , 8, 7, 7, 7, 7 ,7, 7, 6, 10, 10]
}

evil = {
    "name" : "The Evil Power",
    "level" : 15,
    "health" : 150,
    "atk" : [4, 4, 4, 4, 5, 5, 5, 7, 10],
    "catchphrase" : ["I've got to buy it!", "I've got to buy it! Chinpokomon!", "you're gonna love... Alabama Man!"]
}
memberberries = {
    "name" : "Memberberries",
    "level" : 11,
    "health" : 100,
    "atk" : [4, 4, 4, 4, 5, 5, 5, 7, 10],
    "catchphrase" : ["Yeah, I 'member...", "'Member the Millennium Falcon? 'member Chewbacca again?", "Ohh, I 'member. Ooo, 'member? Ooo, 'member?"]
}
pip = {
    "name" : "Pip",
    "level" : 1,
    "health" : 20,
    "atk" : [4, 4, 4, 4, 5, 5, 5, 7, 10],
    "catchphrase" : ["My, how lovely.","Lunchy munchies, hmmm?","Cheerio! My name is Pip. I would like to see if you would mind not smashing our little town into bits."]
}
chtulhu = {
    "name" : "Chtulhu",
    "level" : 9,
    "health" : 90,
    "atk" : [4, 4, 4, 4, 5, 5, 5, 7, 10],
    "catchphrase" : ["...", "@#($*??&@#6@?#%6?", "Grrrr"]
}
chuck_chuck = {
    "name" : "Chuck Chuck",
    "level" : 5,
    "health" : 50,
    "atk" : [4, 4, 4, 4, 5, 5, 5, 7, 10],
    "catchphrase" : ["Chuck Chuck!","Chuck Chuck!"]
}
gs_401 = {
    "name" : "GS-401",
    "level" : 8,
    "health" : 80,
    "atk" : [4, 4, 4, 4, 5, 5, 5, 7, 10],
    "catchphrase" : ["Don't forget to bring a towel!", "It is the towels' turn now.","Welcome to the party, boys!"]
}

enemy_list = {
    1 : evil,
    2 : memberberries,
    3 : pip,
    4 : chtulhu,
    5 : chuck_chuck,
    6 : gs_401, 
}
chinpokomon_list = {
    1 : furrycat,
    2 : pengin,
    3 : shoe,
    4 : donkeytron,
    5 : roo_stor, 
    6 : accountafish,
    7 : monkay,
    8 : lambtron, 
    9 : roidrat,
}

my_chinpokomon = {}
bully = True

player_inv = {
    "inventory1" : [],
    "inventory2" : [],
    "max_inventory" : 8,

}

def display_inv_info():
    print(f"Inventory 1: {[chin['name'] for chin in player_inv['inventory1']]}")
    print(f"Inventory 2: {[chin['name'] for chin in player_inv['inventory2']]}")
    print(f"{player_inv['max_inventory']}\n")

def get_info(chinpokomon):
    print(f"Type: {chinpokomon['name']}")
    print(f"Health: {chinpokomon['health']}\n")

def atk(attacker, attackee):
    atk_val = random.choice(attacker["atk"])
    attackee["health"] -= atk_val
    print(f"{attacker['name']} just attacked {attackee['name']} by {atk_val}!\n")

def check_health(unit):
    if unit["health"] <= 0:
        return True
    else:
        return False
    
def catchprase(unit):
    print(f'"{random.choice(unit["catchphrase"])}" -{unit["name"]}\n')

def battle():
    enemy = random.choice([each.copy() for each in enemy_list.values() if each['level'] < 10])
    print("you go out into the wild to find more chinpokomon!")
    print(f"You come across {enemy['name']}. Now you must fight!")  
    while bully:
        choice = input("status or fight? ").lower()
        print("\n")
        if choice == 'status':
            get_info(main_chinpokomon)
            get_info(enemy)
        elif choice == 'fight': 
            atk_num = atk(main_chinpokomon, enemy) 
            if check_health(enemy):
                print(f"{main_chinpokomon['name']} has defeated {enemy['name']}!\n")
                return
            atk_num = atk(enemy, main_chinpokomon)
            catchprase(enemy)
            if check_health(main_chinpokomon):
                print(f"Oh no! {enemy['name']} has defeated {main_chinpokomon['name']}! You've lost!\nGAME OVER\n")
                quit()

def explore():
    wild_chinpokomon  = random.choice([each.copy() for each in chinpokomon_list.values()])
    user_input = while_input(f"You've stumbled across a {wild_chinpokomon['name']}! Would you like to collect it? (Y/N)", "ERR: Yes or No?", 'y', 'n')
    if proper_input(user_input,"y"):
        check_inv(wild_chinpokomon)

def lvl_sort(e):
    return e["level"]

def check_inv(chinpokomon):
    print(f"Inventory 1: {[chin['name'] for chin in player_inv['inventory1']]}")
    print(f"Inventory 2: {[chin['name'] for chin in player_inv['inventory2']]}")
    if len(player_inv["inventory1"]) >= player_inv["max_inventory"] and len(player_inv["inventory2"]) >= player_inv["max_inventory"]:
        user_input = while_input(f"Both your inventories are full. Would you like to merge them? (Your strongest chinpokomon will be kept) Y/N \n-if N, you will lose your new chinpokomon."
                               , "ERR: Invalid Answer", 'y','n')
        if user_input == 'y':
            player_inv["inventory1"] += player_inv["inventory2"].copy()
            player_inv["inventory1"].sort(key=lvl_sort) 
            [player_inv["inventory1"].pop(num) for num in range(0,8)]
            print(f"\nInventory 1: {[chin['name'] for chin in player_inv['inventory1']]}")
            while player_inv["inventory2"]:
                del(player_inv["inventory2"][0])
            print(f"Inventory 2: {[chin['name'] for chin in player_inv['inventory2']]}\n")
            
            return
        else:
            return
    user_input = while_input(f"Would you like to put {chinpokomon['name']} in inventory 1 or 2?", "ERR: Invalid Answer", '1' ,'2')
    if user_input == '1' and len(player_inv["inventory1"]) < player_inv["max_inventory"]:
        player_inv["inventory1"].append(chinpokomon)
        print(f"{chinpokomon['name']} added to Inventory 1!\n")
        return
    elif user_input == '1' and len(player_inv["inventory1"]) >= player_inv["max_inventory"]:
        print(f"Inventory 1 is full: {player_inv['inventory1']}")
        user_input = while_input(f"Would you like to put {chinpokomon['name']} in inventory 1 or 2?", "ERR: Invalid Answer", '1' ,'2')
    elif user_input == '2' and len(player_inv["inventory2"]) < player_inv["max_inventory"]:
        player_inv["inventory2"].append(chinpokomon)
        print(f"{chinpokomon['name']} added to Inventory 2!\n")
        return
    elif user_input == '2' and len(player_inv["inventory2"]) >= player_inv["max_inventory"]:
        print(f"Inventory 2 is full: {player_inv['inventory1']}")
        user_input = while_input(f"Would you like to put {chinpokomon['name']} in inventory 1 or 2?", "ERR: Invalid Answer", '1' ,'2')  

def while_input(text_input, err_msg='', *args):
    while True:
        user_input = input(f"{text_input} ").lower()
        if proper_input(user_input, args):
            return user_input
        else:
            print(f"{err_msg}")
            continue

def proper_input(user_input, desired_input):
    if user_input.lower() == desired_input or user_input in desired_input:
        return user_input
    else:
        return False
    
print("Welcome to Chinpokomon! You can pick Furrycat, Pengin, or Shoe.")

while True:
    chosen_chinpokomon = input("Which Chinpokomon will you choose? ").lower()
    print("\n")  
    if chosen_chinpokomon == 'furrycat':
        print("You picked Furrycat! Let's go!")
        main_chinpokomon = furrycat.copy()
        break
    elif chosen_chinpokomon == 'pengin':
        print("You picked Pengin! Let's have an adventure!")
        main_chinpokomon = pengin.copy()
        break
    elif chosen_chinpokomon == 'shoe':
        print("You picked Shoe!? What a peculiar chinpokomon!" )
        main_chinpokomon = shoe.copy()
        break
    else: 
        print("Gosh, that chinpokomon isn't here.")
print("You're out in the world of chinpokomon! What will you do?\n")

while True:
    action = input("You can check status, explore, or go home (ends game) ").lower()
    print("\n")
    if action == 'status' or action == 'check status':
        get_info(main_chinpokomon)
        display_inv_info()
    elif action == 'explore':
        if random.choice([True, False]):
            battle()
            continue
        else:
            explore()
            continue
    elif action == 'home' or action == 'go home':
        while True:
            double_check = input("Are you sure you want to go home? Y or N ").lower()
            if double_check == 'y':
                print("\nThanks for playing!\n")
                quit()
            elif double_check == 'n':
                break
            else:
                print("Sorry, that's not a valid command")
    else:
        print("Sorry, that's not a valid command")