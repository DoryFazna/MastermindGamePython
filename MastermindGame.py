import random
import Functions.Codes
file = open("GameRecords.txt","a")
word=""
while True:
  
  start="X"
  
  print("Do you want to ",word,"start the game??\n .......Yes / No .........\n")
  start=input()
  if start == "No" :
    break    
  elif start == "Yes" :
    Functions.Codes.welcomenote()

    while True :
     #GENERATES 4 DIGIT NUMBER & INTRO
      pattern=Functions.Codes.intro()
      file.write("----------------------MASTERMIND----------------------------\n")
      file.write("%-25s %-25s %s"%("No","Guess","results"))
      file.write("\n")
      c=1
      m=0
      
      while m < 8 :
        
        c=m+1
        exact=0
        close=0
        check=[0,0,0,0]
        check2=[0,0,0,0]
        
        print(c,end="")
        file.write(str(c))
        file.write("\t\t\t")
        
        
      #INPUT NUMBERS FROM THE PLAYER  
        g1,g2,g3,g4=input("\t\t\t").split()
        file.write(g1)
        file.write(g2)
        file.write(g3)
        file.write(g4)
        file.write("\t\t\t")
        guess=[g1,g2,g3,g4]
            
        g1,g2,g3,g4=int(g1),int(g2),int(g3),int(g4)
        
      #IF THE PLAYER INPUT 0000  
        if g1 == g2 == g3 == g4 == 0:
           Functions.Codes.endgame()
           file.write("\nyou have ended the game.. do you want to try again?\n")
           break
          
      #IF THE NUMBERS > 6  
        if (g1>6) or (g2>6) or (g3>6) or (g4>6) :
          print("Error, please enter values between 1-6")
          file.write("\nError, please enter values between 1-6\n")
          m=c-1
          continue
        
      #CALCULATES THE EXACT     
        for i in range (0,4):
          if guess[i] == pattern[i] :
             exact=exact+1
             check[i]=1
             
      #CALCULATES THE MISPLACED NUMBERS     
        for i in range(0,4):
          for k in range (0,4) :
            if (check[i] == 0 and check [k]==0) and (check2[k]==0):
              if pattern[i]==guess[k]:
                check2[k]=1
                close+=1
                break
              
      #PRINTS 0's and 1's
        
        a=Functions.Codes.printresult(exact,1)
        b=Functions.Codes.printresult(close,0)
        Z=a+b
        file.write(str(Z))
        file.write("\n")
        
        print("_"*80)
        file.write("_"*80)
        file.write("\n")
        m+=1
        
     #FIGURING OUT IF IT IS A WIN
        
        if guess[0] == pattern [0] and guess[1] == pattern [1] and guess[2] == pattern [2] and guess[3] == pattern [3]:
          Functions.Codes.victory()
          file.write("\n CONGRATULATIONSSS!!! YOU WONN !!!! do u want to try again?\n")
          break       
     
     #FIGURING OUT IF THE GAME IS OVER
        if c>=8 :
          Functions.Codes.gameover(pattern)
          file.write("\nGAME OVER .. :( \n The Hidden Code is ")
          file.write(str(pattern))
          file.write("\n WANNA TRY AGAIN??\n")
          
     # USER INPUT YES or NO     
      x="A"
      x=str(input())
      file.write(x)
      file.write("\n")
      if x=="No" :
        word="Re"
        break
      elif x=="Yes":
        m=9
        continue
      else :
        break

  else :
    break
file.close()
