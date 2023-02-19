import random
import os
from data import insta
from art import ver,hl
print("Welcome to the Higher Lower Game\n\n")
print(hl)


def random_celeb():
    insta_ra = random.choice(insta)
    print(insta_ra[0],',',insta_ra[2],',',insta_ra[3])
    return insta_ra

def game():
    score=0
    game_over=False
    while(game_over==False):
        print(f"Your current Score is : {score}\n")
        cele1 = random_celeb()
        print(ver)
        cele2 = random_celeb()
        if cele2 == cele1:
            cele1 = random_celeb()
        print("\n")
        # print(cele1[1])
        # print(cele2[1])
        choice = input("Who has the most followers on instagram? 'A' OR 'B' : ")
        if(choice == 'A' and cele1[1]>cele2[1]):
            print("You Win")
            score+=1
            os.system("cls")
            print(hl)
        elif(choice == 'B' and cele2[1]>cele1[1]):
            print("You Win")
            score+=1
            os.system("cls")
            print(hl)
        else:
            print(f"Followers of {cele1[0]} are {cele1[1]} Millions and \nFollowers of {cele2[0]} are {cele2[1]} Millions\n")
            print("************* You loose *************")
            print(f" ***** Your Final Score was : {score} *****")
            game_over=True
        
game()

