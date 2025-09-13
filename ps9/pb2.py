import random
def game():
    print("You are playing the game..")
    score = random.randint(1,62)

    with open("hiscore.txt","r") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)                    #converting string into integer
        else:
            hiscore = 0
        
    print(f"Your score: {score}")
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))                         #converting integer into string
        
    return score


game()