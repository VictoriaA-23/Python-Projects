#This program executes a trivia game for two players based on questions and information from other modules. 

#imports modules with game questions and formatting
import triviaQuestions
import questionClass

#attaches variable to question list from other module
questionslist = triviaQuestions.makelist()

#sets points to 0 
player1_points = 0
player2_points = 0

#establishes which player gets which question
question_num = 1


for obj in questionslist:
    choice = 1
    #question formatting for player 1
    if question_num %2 != 0:
        print("Question for the first player:")
        print(obj.question)
        print(str(choice) + '.' + obj.answer1)
        choice += 1
        print(str(choice) + '.' + obj.answer2)
        choice += 1
        print(str(choice) + '.' + obj.answer3)
        choice += 1
        print(str(choice) + '.' + obj.answer4)
        
    #question formatting for player 2
    else:
        print("Question for the second player:")
        print(obj.question)
        print(str(choice) + '.' + obj.answer1)
        choice += 1
        print(str(choice) + '.' + obj.answer2)
        choice += 1
        print(str(choice) + '.' + obj.answer3)
        choice += 1
        print(str(choice) + '.' + obj.answer4)
        

    while True:
        #allows user to enter answer to question
        incorrect = 0
        answer = int(input("Enter your solution (a number between 1 and 4): "))
        if answer < 1 or answer > 4:
            print("Invalid choice!")
        #establishes if user answer is correct answer
        else:
            if answer == 1 and obj.answer1 == obj.correctAnswer:
                print("That is the correct answer.\n")
            elif answer == 2 and obj.answer2 == obj.correctAnswer:
                print("That is the correct answer.\n")
            elif answer == 3 and obj.answer3 == obj.correctAnswer:
                print("That is the correct answer.\n")
            elif answer == 4 and obj.answer4 == obj.correctAnswer:
                print("That is the correct answer.\n")
            else:
                correctIndex = 0
                if obj.answer1 == obj.correctAnswer:
                    correctIndex = 1
                elif obj.answer2 == obj.correctAnswer:
                    correctIndex = 2
                elif obj.answer3 == obj.correctAnswer:
                    correctIndex = 3
                elif obj.answer4 == obj.correctAnswer:
                    correctIndex = 4

                print("That is incorrect. The correct answer is", correctIndex)
                print()
                incorrect = 1
            #assigns points when player gives correct answer
            if question_num %2 != 0 and incorrect == 0:
                player1_points += 1
            elif question_num %2 != 0 and incorrect ==0:
                player2_points += 1

            #moves to the next question and person
            question_num += 1
            break;
        
#announces each player's amount of points
print("The first player earned", player1_points, "points.")
print("The second player earned", player2_points, "points.")

#declares who the winner (if any) is
if player1_points > player2_points:
    print("The first player wins the game.")
elif player1_points < player2_points:
    print("The second player wins the game.")
else:
    print("Match tied!")
