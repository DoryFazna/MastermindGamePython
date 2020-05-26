
#functions
import random

def welcomenote ():
  print(" Welcome to MASTERMIND..\n Hidden code's length = 4 \n NOTE :- Add space in between your guess's numbers. \n\t Example ------- 1 2 3 4")

#GENERATES 4 RANDOM NUMBERS BETWEEN 1-6
def intro ():
  file = open("GameRecords.txt","a")
  pattern = [random.choice('123456') for i in range (4)]
  print("\t----------------------MASTERMIND----------------------------")
  print("\t\t\t\t\t\tColor Mapping:\n\t\t\t\t\t\t1-White  2-Blue  3-Red\n\t\t\t\t\t\t4-Yellow  5-Green  6-Purple ")
  print('Number to Guess -   X X X X ')
  print("%-25s %-25s %s"%("No","Guess","results"))
  return pattern

#PRINTS 0's and 1's
def printresult (x,y):
    file = open("GameRecords.txt","a")
    text=[]
    print("\t\t\t\t\t\t\t",end="")
    
    for i in range (0,x):
      print(y," ",end="")
      text.append(y)
    print()  
    return text

#USER INPUT 0000
def endgame ():
  print("you have ended the game.. do you want to try again?\n.........Yes/No.........")
  
#IF THE PLAYER LOSE    
def gameover(p):
      print("GAME OVER .. :( \n The Hidden Code is ",p,"\n WANNA TRY AGAIN??\n........Type Yes/No........." )

#IF IT IS A WIN
def victory ():
  print(" CONGRATULATIONSSS!!! YOU WONN !!!! do u want to try again?\n.........Type Yes/No..........")
