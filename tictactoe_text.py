## VERSION 3.1.2 - TEXT ONLY, One & Two Player Mode, Clearing for console WINDOWS CMD and Powershell

import random
import time
import sys
import subprocess

board = [" " for p in range(0,10)]
cells = [1,2,3,4,5,6,7,8,9]
player = 0
a=0
t=3
occ = []
msg = ["Hope You're Enjoying Our Tic Tac Toe Game! O(∩_∩)O",
"Great job, you're getting the hang of it! (´▽`ʃ♡ƪ)",
"Don't give up, you can still turn this around! ♪(^∇^*)",
"It's not over yet. Keep playing your best! o(*￣▽￣*)ブ",
"Every move counts. Stay focused! (^///^)",
"Well played! This is an exciting game. ƪ(˘⌣˘)ʃ",
"You're doing great, just a few more moves to victory! ヾ(＠⌒ー⌒＠)ノ",
"Remember, it's all about strategy. You've got this! (。・∀・)ノ",
"Keep the pressure on. You're making excellent moves. ╰(*°▽°*)╯",
"Win or lose, it's all about having fun. Enjoy the game! (●ˇ∀ˇ●)"]
print("WELCOME to our TIC-TAC-TOE game! (｡･∀･)ﾉﾞ")
print("We Hope you enjoy!")
print("（￣︶￣）↗　")
print("""
Enter Mode of Playing [1 or 2]:
1 - One Player
2 - Two Player
""")

while True:
    try:
        mode = int(input("Mode: "))
        print(" ")
        if mode == 1 or mode == 2:
            break
        else:
            print("Not A Valid Mode...")
    except ValueError:
        print("Not A Valid Mode...")
        
if mode == 1:
    print("You Chose to Play with an AI, Good Luck!")
    print("You are playing as 'O'...")
elif mode == 2:
    print("You Chose Two Player Mode! Input positions one by one to play...")
    print("Good Luck to Both the players!")
print(" ")
while True:
    
    if player == 1:
        this = "X"
        that = "O"
    elif player == 0:
        this = "O"
        that = "X"
        
    if (
            (board[1] == board[2] == board[3] != " ")
            or (board[4] == board[5] == board[6] != " ")
            or (board[7] == board[8] == board[9] != " ")
            or (board[1] == board[4] == board[7] != " ")
            or (board[2] == board[5] == board[8] != " ")
            or (board[3] == board[6] == board[9] != " ")
            or (board[1] == board[5] == board[9] != " ")
            or (board[3] == board[5] == board[7] != " ")
    ):
        break
        
    if a == 9:
        print("It's a Tie!")
        print("The board has been Cleared... Play Again!")
        board[1]=board[2]=board[3]=board[4]=board[5]=board[6]=board[7]=board[8]=board[9]=" "
        a=0
        print(f"Player '{this}' Moves First!")
        occ = []

    print("~~~~~~~~~~~~~")
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |")
    print("-------------")
    print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
    print("-------------")
    print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |")
    print("~~~~~~~~~~~~~")
        
    if mode == 1:
        if player == 0:
            while True:
                try:
                    print(f"Player {this}'s Turn!")
                    pos = int(input("Enter a position [1-9]: "))
                    if 0 < pos < 10 and pos not in occ:
                        break
                    else:
                        print("Not a Valid position on the board...")
                except ValueError:
                    print("Not a Valid position on the board...")
            board[pos] = "O"
            player = 1 - player
            print(f"Player '{this}' entered a valid position:", pos)
        elif player == 1:
            empty_cells = [i for i in cells if i not in occ]
            pos = random.choice(empty_cells)
            board[pos] = "X"
            player = 1 - player
            print(f"The Bot playing with '{this}' entered a valid position:", pos)
            time.sleep(2)

    if mode == 2:
        while True:
                try:
                    print(f"Player {this}'s Turn!")
                    pos = int(input("Enter a position [1-9]: "))
                    if 0 < pos < 10 and pos not in occ:
                        break
                    else:
                        print("Not a Valid position on the board...")
                except ValueError:
                    print("Not a Valid position on the board...")
        if player == 0:
            board[pos] = "O"
            player = 1 - player
        elif player == 1:
            board[pos] = "X"
            player = 1 - player
        print(f"Player '{this}' entered a valid position:", pos)
    time.sleep(1)
    a+=1
    occ.append(pos)
    subprocess.run('cls' if sys.platform == 'win32' else 'clear', shell=True)


    print(" ")
    print("┻━┻ ︵ ＼( °□° )／ ︵ ┻━┻ ︵ ＼( °□° )／ ︵ ┻━┻ ︵ ＼( °□° )／ ︵ ┻━┻ ︵ ＼( °□° )／ ︵ ┻━┻")
    print(" ")
    print(random.choice(msg))
    print(" ")
    
print("~~~~~~~~~~~~~")
print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |")
print("-------------")
print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
print("-------------")
print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |")
print("~~~~~~~~~~~~~")

print(" ")
print(f"Player '{that}' WON!")
print("Congratulations!")
print(" ")
while t > 0:
    print("Terminating Program in",t, end='\r')
    time.sleep(1)
    t -= 1
            
print("Thank You For Playing. (^///^)")
print("Have A Nice Day! (。・∀・)ノ")
time.sleep(1)

