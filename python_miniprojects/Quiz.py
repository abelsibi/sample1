print("Welcome to the Quiz !")
user_interested=input("Are you interested to play this quiz game ! : ")
if user_interested.lower() != "yes":
    quit()
else:
    print("let start the game ):")
score=0

Answer=input("What is the fullform of CPU ? ")
if Answer.lower()=="central processing unit" :
    print("correct ,you got one point ): ")
    score+=1
else:
    print("wrong answer , no new points :( ")

Answer=input("What is the fullform of RAM ? ")
if Answer.lower()=="random acess memory" :
    print("correct ,you got one point ): ")
    score+=1
else:
    print("wrong answer , no new points :( ")
    

Answer=input("What is the fullform of BIOS ? ")
if Answer.lower()=="basic input output system" :
    print("correct ,you got one point ): ")
    score+=1
else:
    print("worng answer , no new points :( ")

total_score=print("you have got " + str(score) + "points  \n congrats")
total_percentage =print("you had got " + str((score/3)*100) + " percentage")
conclusion=print("Thanks for playing ,come again !!! ")