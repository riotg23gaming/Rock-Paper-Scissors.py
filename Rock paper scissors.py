import  random
import time
import  winsound
history=[]
com_reaction=[]
print('====================Rock(🪨),Paper(🗞️),Scissors(✂️)=====================')
time.sleep(1.5)
print('Welcome to the game of Rock,Paper,Scissors!👋')
time.sleep(1.5)
print('You will be playing against me(COM)🥰!')
time.sleep(1.5)
while True:
    count = 0
    score_Player = 0
    score_COM = 0
    num = int(input('How many wins are needed to decide the winner? : '))
    while True:
        print(f'Player: {score_Player}')
        print(f'COM: {score_COM}')
        count+=1
        print(f"Turn: {count}")
        move_user = input('Select move(Rock,Scissors or Paper) or type Quit to quit: ').capitalize().strip()
        if move_user=='Quit':
            break
        else:
            if move_user != 'Rock' and move_user != 'Paper' and move_user != 'Scissors':
                print("Invalid input! Please select a move!")
                count -= 1
                continue
            com_move = random.randint(1, 3)
            if com_move == 1:
                com_move = 'Rock'
            elif com_move == 2:
                com_move = "Paper"
            else:
                com_move = 'Scissors'
            for i in range(4):
                print("\rThe computer is Thinking" + "." * i, end="", flush=True)
                time.sleep(0.5)

            print()
            time.sleep(3)
            print(f'The computer chose {com_move}')
            time.sleep(1)
            if (move_user == 'Rock' and com_move == 'Scissors' or
                    move_user == 'Paper' and com_move == 'Rock' or
                    move_user == 'Scissors' and com_move == 'Paper'):
                score_Player += 1
                winsound.Beep(1000, 200)
                print("You Win!")
                com_reaction = ["What?! How did you do that?! 😱",
                                "Okay... you got me.",
                                "Lucky move! 😒",
                                "I'll remember that!",
                                "Well played! 👏",
                                "You got me this time!",
                                "Fine, fine... you win. 😤",
                                "I underestimated you! 🤖"]


            elif (move_user == "Rock" and com_move == "Rock" or
                  move_user == 'Paper' and com_move == "Paper" or
                  move_user == 'Scissors' and com_move == 'Scissors'):

                print("Draw!")
                com_reaction = ["A draw?! Great minds think alike.",
                                "We picked the same move! 😐",
                                "Copycat! 😂",
                                "We're evenly matched!",
                                "Nobody wins this round!",
                                "What are the chances?!",
                                "Tie! Let's do that again.",
                                "You read my mind! 🧠"]
            else:
                score_COM += 1
                print("You Lose!")
                winsound.Beep(300, 400)
                com_reaction = ["Ha! I got you! 😈",
                                "Too easy! 😎",
                                "Better luck next round!",
                                "The computer strikes again! 🤖",
                                "I knew you were going to do that!",
                                "Ouch! That one was mine!",
                                "Victory is mine! 🏆",
                                "Looks like I'm ahead! 😏"]

            reaction = random.choice(com_reaction)
            for letter in reaction:
                print(letter, end='', flush=True)
                time.sleep(0.03)
            print()

            time.sleep(1.5)

            if score_COM == num - 1 and score_Player == num - 1 and num > 1:
                print("Last round to decide the winner!")
            elif score_COM == num and score_Player < num or score_Player == num and score_COM < num:
                print('Game over', end='')
                print()
                if score_Player > score_COM:
                    name = input('Enter your name: ')
                    print(f'The winner is {name} 🏆')
                    break
                else:
                    print('You lost the Game')
                    time.sleep(1)
                    print('The winner is Me 🏆')
                    break

    history.append({'Player':score_Player,
                        'COM': score_COM})

    print('Would you like to see the history score(Y/N)?:')
    answer = input().capitalize()
    if answer == 'Y':
        print(history)

    print('Would you like to play again!')
    answer = input('Enter your answer(Y/N): ').upper()
    if answer != 'Y':
        print('It was nice Playing with you!🥰')
        time.sleep(1)
        print('I hope to see you again! 👋')
        break

