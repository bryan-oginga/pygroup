

speed = int(input("Enter the speed limit : "))
points = 0

def SpeedCheck(speed):

    if speed < 70:
        print("OK")
        
    else:

        print(f'Your points are {points + 2}')
        if points > 12:
            print("License suspended")
           


SpeedCheck(speed)