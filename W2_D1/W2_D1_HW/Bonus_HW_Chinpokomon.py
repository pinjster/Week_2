import random

furrycat = {
    "name" : "Furrycat",
    "health" : 100,
    "atk" : [8, 8 , 8 , 8 , 8, 7, 7, 7, 7 ,7, 7, 6, 10, 10]
}
pengin = {
    "name" : "Pengin",
    "health" : 400,
    "atk" : [4, 4, 4, 4, 5, 5, 5, 7, 7, 10]
}
shoe = {
    "name" : "Shoe",
    "health" : 500,
    "atk" : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 2, 2, 50]
}
enemy = {
    "name" : "The Evil Power",
    "health" : 50,
    "atk" : [4, 4, 4, 4, 5, 5, 5, 7, 10]
}

my_chinpokomon = {}
evil = {}
bully = True

def chinpokomon_info(chinpokomon):
    print("Type: " + chinpokomon.get("name"))
    print("Health: " + str(chinpokomon.get("health")) + "\n")

print("Welcome to Chinpokomon! You can pick Furrycat, Pengin, or Shoe.")

while True:
    chosen_chinpokomon = input("Which Chinpokomon will you choose? ").lower()
    print("\n")  
    if chosen_chinpokomon == 'furrycat':
        print("You picked Furrycat! Let's go!")
        my_chinpokomon = furrycat.copy()
        break
    elif chosen_chinpokomon == 'pengin':
        print("You picked Pengin! Let's have an adventure!")
        my_chinpokomon = pengin.copy()
        break
    elif chosen_chinpokomon == 'shoe':
        print("You picked Shoe!? What a peculiar chinpokomon!" )
        my_chinpokomon = shoe.copy()
        break
    else: 
        print("Gosh, that chinpokomon isn't here.")
print("You're out in the world of chinpokomon! What will you do?\n")

while True:
    action = input("You can check status, explore, or go home (ends game) ").lower()
    print("\n")
    if action == 'status' or action == 'check status':
        chinpokomon_info(my_chinpokomon)
    elif action == 'explore':
        print("you go out into the wild to find more chinpokomon!")
        print("You come across The Evil Power. Now you must fight!")
        while bully:
            evil = enemy.copy()
            choice = input("status or fight? ").lower()
            print("\n")
            if choice == 'status':
                chinpokomon_info(my_chinpokomon)
                chinpokomon_info(evil)
            elif choice == 'fight': 
                chinpokomon_atk = random.choice(my_chinpokomon.get("atk"))
                evil["health"] -= chinpokomon_atk
                print(my_chinpokomon.get("name") + " just attacked " + evil.get("name") + " by " + str(chinpokomon_atk) + "!\n")
                evil_atk = random.choice(evil.get("atk"))
                my_chinpokomon["health"] -= evil_atk
                print(evil.get("name") + " just attacked " + my_chinpokomon.get("name") + " by " + str(evil_atk) + "!\n")
                if my_chinpokomon["health"] <= 0:
                    print("Oh no! your chinpokomon passed out! The evil power has won! GAME OVER")
                    quit()
                elif evil["health"] <= 0:
                    print(my_chinpokomon["name"] + " defeated " + evil["name"] + "! Way to go!\n")
                    break
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