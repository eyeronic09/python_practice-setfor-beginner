
import random

while True:
    play = ["p","r","s"]
    computer = play[random.randint(0,2)]
    
    playChoice = input("enter the  'r' for rock , 'p' for paper , 's' for scissor OR 'q' ")
    if(playChoice == "q"):
        print("thx for playing")
        break
    
    if(playChoice not in play):
        print("not an valid choice enter between 'r' for rock , 'p' for paper , 's' for scissor")
        continue
    
    print(f"you choose the {playChoice} and computer choose {computer}")
    if(playChoice == computer):
        print(f"computer choose{play} and player choose {playChoice} so its a tie")
        break
    elif(playChoice == 'r' and play == 's'):
        print("rock beat scissor. you win")
    elif(playChoice == "s" and play == "p"):
        print("scissor beats paper. you win")
    elif(playChoice == "p" and play == "r"):
        print("paper beats rock. you win")
    else:
        print(f"{computer} beats {playChoice}. Computer wins!")
