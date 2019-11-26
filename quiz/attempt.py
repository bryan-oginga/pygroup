
def icorectTrials():
     print("You failed the guess game !! ")

def PrintMessage():
    attempt = 0

    while attempt < 3:
        userInput = int(input("Enter a number : "))
        attempt += 1

        if userInput == 9:
            print("Congraculations you win the game")
            break

    else:
        icorectTrials()

    
# function call
PrintMessage()
    







        
       
        
       



