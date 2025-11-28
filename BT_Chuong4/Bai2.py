from random import randrange

def endGame():
    continueGame = input("Choi Tiep? (Y/N): ")
    if(continueGame == "N" or continueGame == "N"): return True
    return False

randomNumber = randrange(1, 100)
count = 0
while(True):
    print("="*30)
    guessNumber = int(input("Hay doan so tu 1 - 100: "))
    if(guessNumber == randomNumber):
        print("Ban da doan dung!")
        print("="*30)
        if(endGame()):
            count = 0
            break
    elif(count >= 7):
        print("Het luot doan! Ban da thua!")
        print("="*30)
        if(endGame()):
            count = 0
            break
    print("Ban da doan: ", count, " lan")
    count+=1
    
