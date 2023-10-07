#March 2022 specimen paper

scores = []
names = []
par = -1

def sumScore(i):
    score_sum = 0
    for x in scores[i]:
        score_sum += x
    return score_sum

def findWinnerIndex():
    sumOfScores = []
    for i in range(scores):
        sumOfScores.append(sumScore(i))

    small = 0
    for i in range(1,len(sumOfScores)):
        if sumOfScores[i] < small:
            small = i

    return i

def Setup_task1():
    correct = False
    while not correct:
        print("Hello and welcome to another round of golf!")
        player_count = int(input("How many players are playing today? (1-4): "))
        while player_count < 1 or player_count > 4:
            print("There can only be between 1 and 4 players, please enter again")
            player_count = input("How many players are playing today? (1-4): ")
        for i in range(0,player_count):
            names.append(input("Please enter a name for player "+str(i+1)+": "))
            scores.append([])
        print("How many holes are you playing?")
        print("\tA. 18 holes")
        print("\tB. 9 holes")
        
        holes = input().lower()
        while holes != "a" and holes != "b":
            print("Please select A or B")
            holes = input().lower()

        holes = (holes == "a") * 18 + (holes == "b") * 9
        print("You are going to play "+str(holes)+" holes today")

        par = input("What is the par for the entire course? ")
        while len(par) == 0:
            par = input("What is the par for the entire course? ")
        par = int(par)
        
        print()
        print("Here is what you have entered so far, ")
        print("There are "+str(player_count)+" players")
        print("Their names are: ")
        for i in range(0, player_count):
            print(f'\t{i+1}. {names[i]}')
        print("You will play "+str(holes)+" holes with a par of "+str(par))
        print()
        
        correct = (input("Is everything correct (y/n)? ").lower()=="y")
    for s in scores:
        for i in range(holes):
            s.append(0)

def Scorekeep_task2(r):
    print()
    print("="*50)
    print("It is now hole "+str(r))
    print("Please enter your scores: ")
    i = 0
    for n in names:
        a = input(f"Enter {n}'s score for hole {r}: ")
        b = input("And again for confirmation: ")
        while a != b:
            print()
            print("Let's try that again")
            a = input(f"Enter {n}'s score for hole {r}: ")
            b = input("And again for confirmation: ")
        scores[i][r-1] = int(a)
        i += 1
        print()
        if input(f"Would {n} like to see their total score (y/n)? ").lower == "y":
            print(n+"'s total score is " + str(sumScore(i))
        
def Showcase_task3():
    print()
    print("Finally! The end is here.")
    print("Playing with a par "+str(par)" these are the final scores: ")
    for i in range(len(names)):
        print(f"\t{i+1}. {names[i]}: {sumScore(i)-par}")
    print()
    print("The winner is...")
    print("\n"+"~"*50)
    print(names[findWinnerIndex()].upper())
    print("~"*50+"\n")

    print("Here is some extra info that you can learn: ")
    print("\t1. Each players scores")
    print("\t2. Each players scores")
    print("\t1. Each players scores")
    print("\t1. Each players scores")
    
              
Setup_task1()
for i in range(len(scores[0])):
    Scorekeep_task2(i+1)
Showcase_task3()
