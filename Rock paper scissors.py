import  random
import time
print('====================Rock(🪨),Paper(🗞️),Scissors(✂️)=====================')
time.sleep(2)
print('Wellcome to the game of Rock,Paper,Scissors!👋')
time.sleep(2)
print('You will be playing against me(COM)🥰!')
time.sleep(1)
while True:
    count = 0
    score_Player = 0
    score_COM = 0
    num = int(input('How many wins do you want us to Play? : '))
    while True:
        print(f'Player: {score_Player}')
        print(f'COM: {score_COM}')
        count+=1
        print(f"Turn: {count}")
        move_user = input('Select move(Rock,Scissors or Paper): ').capitalize()
        if move_user!='Rock' and  move_user!='Paper' and move_user!= 'Scissors':
            print("Invalid input! Please select a move!")
            count-=1
            continue
        com_move=random.randint(1,3)
        if com_move==1:
            com_move='Rock'
        elif com_move==2:
            com_move="Paper"
        else:
            com_move='Scissors'
        for i in range(4):
            print("\rThe computer is Thinking" + "." * i, end="", flush=True)
            time.sleep(0.5)

        print()
        time.sleep(5)
        print(f'The computer chose {com_move}')
        time.sleep(2)
        if  (move_user=='Rock' and com_move=='Scissors' or
            move_user=='Paper' and com_move=='Rock' or
            move_user=='Scissors' and com_move=='Paper' ):
            score_Player+=1
            print("You Win!")

        elif(move_user=="Rock" and com_move=="Rock"or
             move_user=='Paper' and com_move=="Paper"or
             move_user=='Scissors' and com_move=='Scissors'):

            print("Draw!")
        else:
            score_COM+=1
            print("You Lose!")

        if  score_COM==num-1 and score_Player==num-1 and num>1:
            print("Last round to decide the winner!")
        elif score_COM==num and score_Player<num or score_Player==num and score_COM<num:
            print('Game over')
            if score_Player> score_COM:
                name=input('Enter your name: ')
                print(f'The winner is {name} 🏆')
                break
            else:
                print('You lost the Game')
                time.sleep(2)
                print('The winner is the computer 🏆')
                break
    print('Would you like to play again!')
    answer=input('Enter your answer(Y/N): ').upper()
    if answer!='Y':
        print('It was nice Playing with you!🥰')
        time.sleep(2)
        print('I hope to see you again! 👋')
        break



