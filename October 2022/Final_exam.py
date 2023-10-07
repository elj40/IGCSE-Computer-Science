#Car park booking system
def getDay():
    return 8
#Data structures - Task 1
booking_range = 14 #const
parking_spaces = 20 #const
def resetData():
    for i in range(0,booking_range):
        two_week_period.append([])
        for j in range(0,parking_spaces):
            two_week_period[i].append(0)


two_week_period = []
resetData()
while True:
    open_i = -1
    day = getDay()
    if day > 14:
        two_week_period = []
        resetData()
        day = (day % 14) + 1
    while True:
        #Data input - Task 1
        print("Please select a day that you would like to book ("+str(day)+"-14)")
        print("Today is day: " + str(day))
        req_day = int(input())
        while req_day < day or req_day > 14:
            req_day = int(input("Try again: "))

        disabled = ""
        while disabled != "y" and disabled != "n":
            disabled = input("Do you need an accessible parking space? (y/n) ")

        start = 0
        stop = parking_spaces
        step = 1
        if disabled == "n":
            start = parking_spaces-1
            stop = 5
            step = -1
            
        #Check for open space - task 2
        for i in range(start,stop,step):
            if two_week_period[req_day-1][i] == 0:
                open_i = i + 1
                break
        if open_i == -1:
            print("There are no parking spaces available that day")
            continue
        else:
            break

    print("There is an available parking space at spot "+ str(open_i))
    visitor_name = ""
    visitor_license = ""
    while len(visitor_name) == 0:
        visitor_name = input("Enter your name: ")
    while len(visitor_license) == 0:
        visitor_license = input("Enter your license number: ")
    two_week_period[req_day-1][open_i-1] = visitor_name + ", " + visitor_license
    print("Your booking was made successfully")
    print("="*50)
    print()
    go = input("Would you like to make another booking?")
    if go == "n":
        break
    
print("Here are some stats on the car park:")
 
