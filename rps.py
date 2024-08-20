import random

pPoints = 0
cPoints = 0
compChoice = ""
i = 0
adv = ""
disadv = ""
rounds = input("How many rounds do you want to play? ")

while(i < int(rounds)):
    print("Rock, Paper, Scissors")
    playerAns = input("Please enter your choice: ")
    num = random.randint(1,3)
    if(num == 1):
        compChoice = "Rock"
        adv = "Scissors"
        disadv = "Paper"
    elif (num == 2):
        compChoice = "Paper"
        adv = "Rock"
        disadv = "Scissors"
    else:
        compChoice = "Scissors"
        adv = "Paper"
        disadv = "Rock"

    if(playerAns == disadv):
        print("Computer chose " + compChoice + " and user chose " + playerAns)
        print("User wins!")
        pPoints = pPoints + 1
    elif(playerAns == adv):
        print("Computer chose " + compChoice + " and user chose " + playerAns)
        print("Computer Wins!")
        cPoints = cPoints + 1
    else:
        print("Computer chose " + compChoice + " and user chose " + playerAns)
        print("Draw!")
    
    i = i + 1
    
print(str(pPoints) + " : " + str(cPoints))
if(pPoints > cPoints):
    print("User Wins with " + str(pPoints) + " points!")
elif(cPoints > pPoints):
    print("Computer wins with " + str(cPoints) + " points!")
else:
    print("It's a draw with both having " + str(pPoints) + " points!")
        

