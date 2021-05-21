from time import sleep
from random import randint
import sys, random

print()
message = "Welcome to..."
def typewriter(message):
  for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !="\n":
            sleep(0.1)
        else:
         sleep(1)
typewriter(message)
print()
sleep(1)
print(""" 
           _____
         .'     '.
        |  .__._  |     
        \ ;_____\ /
        (|| 0|0 ||)
         |'-(_)-'|
         \ .___. /
          '.-  .'
            '-'
___     ___ _______ __   __ __ _______   ______   _______ __   __ _______ __    _ _______ _______ 
|   |   |   |   _   |  |_|  |  |       | |    _ | |       |  | |  |       |  |  | |       |       |
|   |   |   |  |_|  |       |__|  _____| |   | || |    ___|  |_|  |    ___|   |_| |    ___|    ___|
|   |   |   |       |       |  | |_____  |   |_||_|   |___|       |   |___|       |   | __|   |___ 
|   |___|   |       |       |  |_____  | |    __  |    ___|       |    ___|  _    |   ||  |    ___|
|       |   |   _   | ||_|| |   _____| | |   |  | |   |___ |     ||   |___| | |   |   |_| |   |___ 
|_______|___|__| |__|_|   |_|  |_______| |___|  |_|_______| |___| |_______|_|  |__|_______|_______|""")
sleep(3)
print()
print("by Coders-Anonymous")
sleep(3)

global game_lives
game_lives = 3
global inventory
inventory = []
global game_stage
game_stage = "1"
global table
table = [1,2,3,4,5]

def start_game():
    print()
    start = input("Ready to start? [Y/N] ")
    if start.upper() == "YES" or start.upper() == "Y":
        print()
        name_entry()
    elif start.upper() == "NO" or start.upper() == "N":
        typewriter("Oh.\n")
        typewriter("Ok.\n")
        typewriter("Fair enough.\n")
        typewriter("Let's try that again... \n")
        start_game()

def name_entry():
    global name  
    name = input("Welcome, what is your name? ").capitalize()
    sleep(0.5)
    print(f"Welcome, {name}.")
    print()
    start_basement()

def start_basement():
    sleep(1)
    print("You awaken in a haze...")
    sleep(1)
    print("You last recall Liam shutting you in his basement for forgetting to use snakecase... Again.")
    sleep(2)
    print("While you contemplate your transgressions against the coding gods, you notice...")
    print()
    print("                      'The Table of Lazy Writing'.")
    sleep(3)
    print()
    print("What should you do?")
    sleep(1)
    print("[1] Stay and await further instruction.")
    print("[2] Scurry over to Chekov's table.")
    choice_one = input("Make your first choice... [1/2] ")
    print()
    if choice_one == "2":
        basement_table()
    elif choice_one == "1":
        print("You choose to wait for further information.")
        sleep(5)
        print("Still waiting.")
        sleep(3)
        print("Still...")
        sleep(3)
        print("Waiting...")
        sleep(3)
        liam_appears()
    else:
        print(f"This would all be much easier if you could just answer the bleddy questions properly, {name}.")
        sleep(2)
        print("You know what, I'm sorry for shouting.")
        sleep(2)
        print("I've had a long day.")
        sleep(2)
        print("You just head on over to the table.")
        sleep(2)
        print("Obviously...")
        print()
        basement_table()
        
def basement_table():
    sleep(1)
    print("You arrive at the 'obviously-correct-place-to-go' table.")
    sleep(2)
    print("You notice five clichés.")
    sleep(1)
    print("OBJECTS. I said objects.")
    print()
    sleep(2)
    print("[1] A comfort pillow.")
    print("[2] A watering can full of coffee.")
    print("[3] Three Pokéballs.")
    print("[4] A SIM card.")
    print("[5] The Squeaky Toy of Justice.")
    sleep(1)
    print()
    print("Choose three objects.")
    item_pickup()

def check_is_digit(input_str):
    global digit
    if input_str.strip().isdigit():
        digit = True
    else:
        digit = False

def item_pickup():
    print()
    while len(inventory) < 1:
        take = input("Take your first item. ")
        check_is_digit(take)
        if digit == True:
            t = table.count(int(take))
            i = inventory.count(int(take))
            if t > i:
                inventory.append(int(take))
                table.remove(int(take))
            else:
                print("Look at the list and try again.")
                sleep(1)
        else:
            print("Look at the list and try again.")
            sleep(1)
    while len(inventory) < 2:
        take = input("Take your second item. ")
        check_is_digit(take)
        if digit == True:
            t = table.count(int(take))
            i = inventory.count(int(take))
            if t > i:
                inventory.append(int(take))
                table.remove(int(take))
            elif t < i:
                print("You've already taken that one, you muppet.")
                sleep(1)
            else:
                print("That was not on the list.")
                sleep(1)
        else:
            print("Look at the list and try again.")
            sleep(1)
    while len(inventory) < 3:
        take = input("Take your third and final item. ")
        check_is_digit(take)
        if digit == True:
            t = table.count(int(take))
            i = inventory.count(int(take))
            if t > i:
                inventory.append(int(take))
                table.remove(int(take))
            elif t < i:
                print("You have that one already. Is this really that hard?")
                sleep(1)
            else:
                print("Nope. Try again.")
                sleep(1)
        else:
            print("Look at the list and try again.")
            sleep(1)
    inventory_check()
    
def inventory_check():
    global game_stage
    print()
    if len(inventory) > 0:
        print("In your bag you have:")
        print()
        if inventory.count(1) == 1:
            print("A comfort pillow.")
        if inventory.count(2) == 1:
            print("A watering can full of coffee.")
        if inventory.count(3) == 1:
            print("Three Pokéballs.")
        if inventory.count(4) == 1:
            print("A SIM card.")
        if inventory.count(5) == 1:
            print("The Squeaky Toy of Justice.")
    else:
        print("Your bag is empty.")
    if game_stage == "1":
        liam_appears()
    elif game_stage == "2":
        snake_case()
    elif game_stage == "3":
        pythondogs()
    elif game_stage == "4":
        phone()
    
def liam_appears():
    global game_lives
    global game_stage
    game_stage = "2"
    sleep(1)
    print()
    print("You hear a sound.")
    sleep(1)
    print("He's here.")
    sleep(3)
    print()
    print("A screen of smoke rolls around you as Liam appears...")
    sleep(2)
    typewriter("\"Do you wanna play a game?\" he whispers.")
    print()
    print()
    sleep(3)
    want_to_play = input("Well, do you? [Y/N] ").upper()
    print()
    if want_to_play == "Y" or want_to_play == "YES":
        typewriter("\"Good, it's time you REALLY learned how to use snakecase.\"")
        snake_case()
    else:
        print("\"You will pay for your arrogance!\"")
        sleep(3)
        print()
        print("Liam looks furious as he pulls out a giant cartoon mallet and beats it off the side of your head.")
        sleep(3)
        if inventory.count(1) == 1:
            print("You pull out the comfort pillow just in time. The cartoon mallet makes a 'pwif' sound as it fails to have any effect on you.")
            sleep(3)
            print("The comfort pillow is destroyed.")
            sleep(1)
            inventory.remove(1)
            inventory_check()
        else:
            print("You lose a life. Liam's hilarious cartoon mallet actually really hurt.")
            sleep(3)
            game_lives -= 1
            life_check()

def life_check():
    print()
    global game_lives
    if game_lives == 2:
        print("You are still alive.")
        sleep(1)
        print(f"You have {game_lives} lives left.")
        if game_stage == "2":
            snake_case()
        elif game_stage == "3":
            pythondogs()
        elif game_stage == "4":
            fight_dogs()
        elif game_stage == "5":
            phone()
        elif game_stage == "6":
            pythongod()
        elif game_stage == "7":
            game()
        elif game_stage == "8":
            reset_board()
    elif game_lives == 1:
        print("This is your last life! Don't mess up!")
        if game_stage == "2":
            snake_case()
        elif game_stage == "3":
            pythondogs()
        elif game_stage == "4":
            fight_dogs()
        elif game_stage == "5":
            phone()
        elif game_stage == "6":
            pythongod()
        elif game_stage == "7":
            game()
        elif game_stage == "8":
            reset_board()
    elif game_lives == 0:
        gameover()

def gameover():
    print("Nooooooo!!! You imbecile!!! You're dead!!!")
    print()
    exit()

def snake_case():
    global game_stage
    global game_lives
    global snake_case_correct
    sleep(3)
    print()
    typewriter("\"You have a chance to prove yourself, my coding friend!\"")
    print()
    print()
    game_stage = "3"
    typewriter("\"I want you to show me a variable in snakecassssse!\"\n")
    print()
    sleep(2)
    snake = input("Type your answer now! ")
    print()
    if "_" in snake and " " not in snake:
        typewriter("\"You are correct, my student!\"")
        print()
        snake_case_correct = 1
        pythondogs()
    else:
        typewriter("\"You clearly have not learned from your transgressions!\"")
        print()
        snake_case_correct = 0
        sleep(2)
        print()
        print("Liam looks furious and slaps you with a snake.")
        sleep(3)
        if inventory.count(1) == 1:
            print("You pull out the comfort pillow just in time. The snake is repulsed by the comfiness of the pillow and it fails to have any effect on you.")
            sleep(3)
            print("The comfort pillow is destroyed.")
            sleep(1)
            inventory.remove(1)
            inventory_check()
        else:
            print("You lose a life. Liam's snake is super effective!")
            sleep(3)
            game_lives -= 1
            life_check()

def pythondogs():
    global game_stage
    global game_lives
    global snake_case_correct
    global python_dog_answer
    sleep(1)
    if snake_case_correct == 1:
        typewriter("\"You might know your stuff, but you're in my swamp now. Be prepared to meet my python_dog army!\"")
    else:
        typewriter("\"Fear my python_dog army!\"")
    print()
    print()
    sleep(3)
    print("Despite his claim, there are only three of them.")
    sleep(2)
    print("As Liam fades away, you must choose what to do next...")
    print()
    sleep(2)
    print("[1] Fight the python_dogs.")
    print("[2] Calm the python_dogs.")
    print("[3] Run away from the python_dogs.")
    print()
    sleep(3)
    catch = 0
    while catch == 0:
        python_dog_answer = input("Make your decision. ")
        if python_dog_answer == "1":
            print()
            catch = 1
            fight_dogs()
        elif python_dog_answer == "2":
            print()
            catch = 1
            calm_dogs()
        elif python_dog_answer == "3":
            print()
            catch = 1
            run_dogs()
        else:
            print("Answer properly, please.")

def fight_dogs():
    global python_dog_answer
    global difficulty_lower
    difficulty_lower = 0
    print("You choose to fight the bastards.")
    print()
    sleep(3)
    if inventory.count(3) == 1 and inventory.count(5) == 1:
        print("You remember, you have three Pokéballs and the Squeaky Toy of Justice.")
        print()
        fight_choice = input("Would you like to use either of these? [Y/N] ").upper()
        if fight_choice == "Y" or fight_choice == "YES":
            fight_choice = input("Which one? The Pokéballs [1] or the Squeaky Toy [2]. ")
            print()
            if fight_choice == "1":
                pokeballs()
            elif fight_choice == "2":
                squeaky_toy()
            else:
                print("You decide against it and try to beat them down yourself.")
                dice_roll()
        elif fight_choice == "N" or fight_choice == "NO":
            print("You decide against it and try to beat them down yourself")
            dice_roll()
    elif inventory.count(3) == 1:
        print("You remember, you have three Pokéballs.")
        fight_choice = input("Would you like to use these? [Y/N] ").upper()
        if fight_choice == "Y" or fight_choice == "YES":
            pokeballs()
        else:
            print("You decide against it and try to beat them down yourself.")
            dice_roll()
    elif inventory.count(5) == 1:
        print("You remember, you have the Squeaky Toy of Justice.")
        fight_choice = input("Would you like to use these? [Y/N] ").upper()
        if fight_choice == "Y" or fight_choice == "YES":
            squeaky_toy()
        else:
            print("You decide against it and try to beat them down yourself.")
            dice_roll()
    else:
        print("You have nothing useful to fight them with, but GOD DAMN YOU ARE READY TO BEAT SOME MYTHICAL MONSTERS.")
        dice_roll()

def pokeballs():
    global name
    global difficulty_lower
    inventory.remove(3)
    print("You turn your cap around; intense rock music plays behind you; you launch the three Pokéballs with the overwhelming power of anime coarsing through your every molecule.")
    sleep(3)
    print("You just gotta...")
    sleep(1)
    print("Catch...")
    sleep(1)
    print("Them...")
    sleep(1)
    print("ALLLLLL!!!!!")
    print()
    sleep(5)
    print("They are super ineffective.")
    sleep(2)
    print("Liam reappears for a moment...")
    sleep(1)
    typewriter(f"\"This is not Pokémon, {name}.\"")
    sleep(2)
    print()
    print()
    print("One of the python_dogs seems distracted by the whole ordeal, so I guess it was worth it.")
    difficulty_lower = 1
    dice_roll()

def dice_roll():
    global difficulty_lower
    global game_lives
    global game_stage
    print()
    sleep(3)
    print("You go absolutely mad, throwing punches and kicks that defy description.")
    sleep(2)
    print("People watch on, jaws wide, eyes even wider, as you fight these giant monsters with your bare fists.")
    sleep(3)
    print("The python_dogs fight back and things are even, until you hear a voice in your head...")
    sleep(3)
    print("Throw the random probability punch, my padawan.")
    print()
    sleep(3)
    go = input("Type what you want; this is the most important moment of your life, you best make it sound cool. ")
    print()
    sleep(3)
    if go != "":
        print("Nice.")
        sleep(1)
        print("You throw the random probability punch.")
        sleep(3)
    else:
        print("That was your moment to be cool. Whatever...")
        sleep(3)
    print()
    dice_number = randint(1,6)
    if difficulty_lower == 1:
        if dice_number == 1 or dice_number == 2 or dice_number == 3 or dice_number == 4:
            dice_result = "success"
        else:
            dice_result = "miss"
    elif difficulty_lower == 0:
        if dice_number == 1 or dice_number == 2 or dice_number == 3:
            dice_result = "success"
        else:
            dice_result = "miss"
    if dice_result == "success":
        print("YOU LAND THE NASTIEST RANDOM PROBABILITY PUNCH THE KNOWN UNIVERSE HAS EVER SEEN!!!")
        sleep(1)
        print("You defeat them like no one has ever defeated anything ever before ever.")
        sleep(3)
        phone()
    if dice_result == "miss":
        game_stage = "5"
        print("You take the biggest LOSS the known universe has ever seen. The python_dogs make you feel small inside. How embarrassing...")
        print()
        sleep(3)
        print("You lose a life.")
        sleep(3)
        game_lives -= 1
        life_check()

def squeaky_toy():
    global game_stage
    game_stage = "4"
    print()
    print("You unleash the full force of the Squeaky Toy of Justice!")
    sleep(3)
    print("It is destroyed. I need to check what I have left...")
    sleep(3)
    inventory.remove(5)
    inventory_check()

def calm_dogs():
    global game_lives
    global python_dog_answer
    global game_stage
    game_stage = "4"
    if inventory.count(5) == 1:
        print("You remember that you have a Squeaky Toy of Justice!")
        squeaky_toy()
    else: 
        print("Your coding skills are not awesome enough to appease the horde... lose a life!")
        sleep(3)
        game_lives -= 1
        life_check()

def run_dogs():   
    global game_lives
    global game_stage
    game_stage = "4"
    print("You run away.")
    sleep(1)
    print("The python_dogs give chase.")
    sleep(1)
    print("You see a wall and climb over it with haste leaving the hissing dogs on the other side!")
    phone()

def phone():
    global phone_and_sim
    phone_and_sim = 0
    global liam_angry
    liam_angry = 0
    print()
    print("Liam reappears.")
    sleep(2)
    print("You find a phone.")
    print()
    sleep(2)
    if inventory.count(4) == 1:
        print("You remember, you have a SIM Card.")
        print()
        sleep(3)
        use_sim = input("Would you like to use it? [Y/N] ").upper()
        if use_sim == "Y" or use_sim == "YES":
            phone_and_sim = 1
            button_game()
        else:
            print("You forget about the SIM Card.")
    print("What do you do with the phone?")
    print()
    print("[1] Throw the phone at Liam.\n[2] Leave the phone where you found it.")
    print()
    userchoice = input("Please enter your choice: [1/2] ")
    catch = 0
    while catch == 0:
        if userchoice == "1":
            print()
            catch = 1
            throw_phone()
        elif userchoice == "2":
            print()
            catch = 1
            button_game()
        else:
            print()
            print("Try again, I didn't recognise that.")

def throw_phone():
    global liam_angry
    print("He is very angry and turns into the super_python")
    liam_angry = 1
    sleep(2)
    button_game()
    
def button_game():
    global phone_and_sim
    global liam_angry
    print()
    if phone_and_sim == 1:
        print("You phone a friend, hopefully they can help with Liam's next task...")
        print()
    elif liam_angry == 1:
        print("Liam, if you can even call him that anymore, is absolutely furious. This task may be a bit harder now...")
        print()
    sleep(2)
    typewriter("\"Prepare for the button game!\"")
    print()
    print()
    sleep(3)
    typewriter("\"Repeat what I say...\"")
    print()
    print()
    sleep(3)
    button_round()

def button_round():
    global phone_and_sim
    global liam_angry
    global game_stage
    game_stage = "6"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if phone_and_sim == 1:
        button_question = alphabet[randint(0,25)]
    elif liam_angry == 1:
        button_question = alphabet[randint(0,25)] + alphabet[randint(0,25)] + alphabet[randint(0,25)] + alphabet[randint(0,25)] + alphabet[randint(0,25)]
    else:
        button_question = alphabet[randint(0,25)] + alphabet[randint(0,25)] + alphabet[randint(0,25)]
    print(button_question)
    print()
    button_answer = input().lower()
    if button_answer == button_question:
        print()
        print("Correct!")
        print()
        pythongod()
    elif button_answer != button_question:
        print()
        print("Incorrect! Lose a life!")
        game_lives -= 1
        life_check()
        print()

def glitch():
    typewriter("\"Oooooh noooooo, what have you done?????????!!!!!!!!!!\"")
    sleep(3)
    i = 0
    x = randint(1,6)
    while i < 300:
        if i%108 == 0 or i%110 == 0:
            print()
        elif i%3 == 0:
            print("o    000    s     00    000    sss      000  0 0  0  00 00    ss   00 ")
        elif i%5 == 0:
            print("ooo O000     O 0 0O    O0 0O      hs0o0 oooooooo0000   oooo o o  00 OO")
        elif i%7 == 0:
            print("00000000   000    00   00    0   0     00     0  0    00   00   0 0ooo")
        elif i%13 == 0:
            print("o0o0o0o0o0o o 0 o 0o 0 o 000 oo  o 0 0 oo  0 o 0 0 oo  0 o  00  oo 0 o")
        elif i%19 == 0:
            print("oooooooooooooo 00   0 0 00 0  o |  0  0 | - -   000 0 00 0 o 0 oo 00 0")
        elif i%31 == 0:
            print("HELP ME HISSS HSSSSSSS oooooooo HELP ME sssss hiss OOOooo 0 0o  osssss")
        elif i%49 == 0:
            print("hisss ssss 000 ss 0  hisssssss 0 sssss hisssss @ hissssss SSSSSSSSSSSS")
        elif i%109 == 0:
            print("                                    KILL ME                           ")
        elif i%x == 0:
            print()
        else:
            print("0   00 OOOOOOoooooooooo000000hsssss   00000   oo o0o0  00 o  00o o  0 ")
        i += 1
        x = randint(1,6)
        sleep(randint(1,3)*0.01)
    print()
    sleep(3)
    typewriter("\"Thanks, man. You stopped me going full python!!!\"")
    sleep(3)
    print()
    typewriter("\"Here, have an A-STAR!")
    print()
    print()
    sleep(3)
    print("Liam hands you top marks for your assignment!")
    print()
    sleep(3)
    typewriter("\"Hope you enjoyed it!\"")
    print()
    print()
    sleep(3)
    print("Congratulations! You have completed the game!")
    print()
    sleep(3)
    exit()       

global board_rows, board_columns, board_diagonals, board_layout, board_tiles
board_tiles = ['-', '-', '-',
            '-', '-', '-',          
            '-', '-', '-']          
board_rows = ''
board_columns = ''
board_diagonals = ''
board_layout = ''

def reset_board():
    global board_rows, board_columns, board_diagonals, board_layout, board_tiles
    board_tiles = ['-', '-', '-',
               '-', '-', '-',          
               '-', '-', '-'] 
    wantoplayagain()       

def wantoplayagain():
    playagain=input("Ready to play again? [Y/N] ")
    if playagain.upper()=="YES" or playagain.upper()=="Y":
        game()
    elif playagain.upper()=="NO" or playagain.upper()=="N":
        print("Oh.")
        sleep(0.5)
        print("Ok.")
        sleep(0.5)
        print("Fair enough.")
        sleep(3)
        print("How about now?")
        sleep(0.5)
        reset_board()
    else:
        print("Try again, I didn't recognise that.")
        print()
        wantoplayagain()

def board_update():
    global board_rows, board_columns, board_diagonals, board_layout, board_tiles      
    board_rows = [(board_tiles[0], board_tiles[1], board_tiles[2]),      
                  (board_tiles[3], board_tiles[4], board_tiles[5]),      
                  (board_tiles[6], board_tiles[7], board_tiles[8])]      
    board_columns = [(board_tiles[0], board_tiles[3], board_tiles[6]),
                     (board_tiles[1], board_tiles[4], board_tiles[7]),
                     (board_tiles[2], board_tiles[5], board_tiles[8])]
    board_diagonals = [(board_tiles[0], board_tiles[4], board_tiles[8]),
                       (board_tiles[2], board_tiles[4], board_tiles[6])]
    board_layout = ''' {} | {} | {}
 {} | {} | {}
 {} | {} | {}'''.format(board_tiles[0], board_tiles[1], board_tiles[2], board_tiles[3], board_tiles[4],
                           board_tiles[5], board_tiles[6], board_tiles[7], board_tiles[8])

def board_display():
    board_update()            
    print('-----------')      
    print(board_layout)

def check_if_tie():
    board_update()
    if '-' not in board_tiles and check_winner() is None:     
        return True                                           
    else:                                                     
        return False                                          

def check_winner():                                           
    board_update()
    for i in board_rows + board_columns + board_diagonals:
        if i.count('X') == 3:
            return 'X'
        elif i.count('O') == 3:
            return 'O'
    return None

def player_turn():
    allowed_move = 0
    board_update()
    move_made = input('Select a tile (1 - 9): ')
    check_is_digit(move_made)
    while allowed_move == 0:
        if digit == True:
            selected_tile = int(move_made) - 1
            allowed_move = 1
        else:
            print()
            print('Try again.')
            print()
            move_made = input('Select a tile (1 - 9): ')
            check_is_digit(move_made)
    while board_tiles[selected_tile] != '-':                             
        selected_tile = int(input('Insert another tile (1 - 9): ')) - 1  
    board_tiles[selected_tile] = 'X'                                     

def ai_tile():                                                          
    intercept_tile = 0
    win_tile = 0
    for row in board_rows:
        if row.count('O') == 2 and row.count('X') == 0:           
            for i in row:                                         
                if i == '-':                                      
                    return win_tile                               
                win_tile += 1                                    
        win_tile += 3                                             
    win_tile = 0                                                  
    for column in board_columns:                                  
        if column.count('O') == 2 and column.count('X') == 0:
            for i in column:                                      
                if i == '-':                                      
                    return win_tile                               
                win_tile += 3                                    
        win_tile += 1                                             
    win_tile = 0
    x = 4                                                         
    for diagonal in board_diagonals:                              
        if diagonal.count('O') == 2 and diagonal.count('X') == 0: 
            for i in diagonal:                                    
                if i == '-':                                      
                    return win_tile                               
                win_tile += x                                     
        x -= 2                                                    
        win_tile += x                                             
    for row in board_rows:
        if row.count('X') == 2 and row.count('O') == 0:
            for i in row:
                if i == '-':
                    return intercept_tile
                intercept_tile += 1
        intercept_tile += 3
    intercept_tile = 0
    for column in board_columns:
        if column.count('X') == 2 and column.count('O') == 0:
            for i in column:
                if i == '-':
                    return intercept_tile
                intercept_tile += 3
        intercept_tile += 1
    intercept_tile = 0
    x = 4
    for diagonal in board_diagonals:
        if diagonal.count('X') == 2 and diagonal.count('O') == 0:
            for i in diagonal:
                if i == '-':
                    return intercept_tile
                intercept_tile += x
        x -= 2
        intercept_tile += x
    random_tile = random.randint(0, 8)
    while board_tiles[random_tile] != '-':         
        random_tile = random.randint(0, 8)
    return random_tile

def ai_turn():                                     
    board_update()                                   
    print('-----------')                           
    ai_choice = ai_tile()                         
    board_tiles[ai_choice] = 'O'
    print('AI chooses tile {}'.format(ai_choice + 1))

def game():
    global game_lives
    global game_stage
    game_stage = "8"
    while check_winner() is None and check_if_tie() is False:   
        board_display()                                          
        player_turn()                                            
        if check_winner() is None and check_if_tie() is False:   
            ai_turn()
        else:
            break
    if check_winner() == 'X':
        board_display()
        print('-----------')
        print('YOU WIN!')
        print('-----------')
        glitch()
    elif check_winner()=='O':
        board_display()
        print('-----------')
        print('The python god wins!')
        print('-----------')
        print()
        sleep(3)
        print("You lose a life!")
        game_lives -= 1
        life_check()
    else:
        board_display()
        print('-----------')
        print('Your coding skills are literally a match for me. It\'s a draw!')
        print('-----------')
        reset_board()

def pythongod():
    global game_lives
    global game_stage
    game_stage = "7"
    sleep(3)
    print("Liam is obviously unhappy with your use of skills and your coding powers!")
    print()
    sleep(3)
    typewriter ("\"Now you will bear witness to my true form!!!\"")
    print()
    print()
    sleep(3)
    print("Liam has turned into the PYTHON_GOD!!!!!!")
    print()
    sleep(3)
    print("Don't worry, you still have some options:")
    print()
    sleep(3)
    if inventory.count(2) == 1:
        print("[1] Run away.")
        print("[2] Stand and FIGHT!")
        print("[3] Use the 'Watering Can Full of Coffee'!")
        print()
        coffee_choices()
    else:
        print("[1] Run away.")
        print("[2] Stand and FIGHT!")
        print()
        god_choices()
    
def coffee_choices():
    global game_lives
    global game_stage
    choice = input("Which do you choose? [1/2/3] ")
    if choice == "1":
        print("You try the noble thing and run away.")
        print()
        sleep(2)
        print("The python_god is too fast! He attacks and you lose a life!")
        game_lives -= 1
        life_check()
    elif choice == "2":
        print("You prepare to fight the python_god...")
        print()
        sleep(2)
        game()
    elif choice == "3":
        print("Aah, yes. I don't think you realise how powerful that watering can truly is...")
        print()
        sleep(2)
        glitch()
    else:
        print("OK time-waster. Hope you're ready for a scrap.")
        print()
        sleep(2)
        game()
    
def god_choices():
    global game_lives
    global game_stage
    choice = input("Which do you choose? [1/2] ")
    if choice == "1":
        print("You try the noble thing and run away.")
        print()
        sleep(2)
        print("The python_god is too fast! He attacks and you lose a life!")
        game_lives -= 1
        life_check()
    elif choice == "2":
        print("You prepare to fight the python_god...")
        print()
        sleep(2)
        game()
    else:
        print("OK time-waster. Hope you're ready for a scrap.")
        print()
        sleep(2)
        game()

start_game()