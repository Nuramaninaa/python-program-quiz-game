
print('Food Quiz Game')
answer=input('You want to play the Quiz ? (yes/no) :')
print("\n")
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is the rarest M&M color?')
    if answer.lower()=='brown':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: What is the common name for dried plum? ')
    if answer.lower()=='prunes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What was the first soft drink in space?')
    if answer.lower()=='coca cola':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thank you for playing this quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print("\n")
print('Total Marks:',mark)
print('DONE!')