'''This is my CS160 fianl project using Python, It will ask for a list of students
and their scores from a user. It will then add them to the appropriate list for
later recall. Finally the user will ask for a student and their score.
Created on 8/22/19
Created by Thomas Chase'''

#Student list loop

#function for the student list
def createStudent():
    studentList = []
    return studentList

#function to fill list
def fillStudent(studentList):
    name = input('Please enter a students name or "q" to quit: ')
    studentList.append(name)
    while name != 'q':
        name = input('Please enter a students name or "q" to quit: ')
        studentList.append(name)
        
        if name == 'q':
            break
        
    
        else:
            name = input('Please enter a students name or "q" to quit: ')
            studentList.append(name)
            continue

    return studentList
#function for the scores list
def createScore():
    scoreList = []
    return scoreList

#function to fill the score list
def fillScore(scoreList):
    score = int(input('Please enter the first students score first or "0" to quit: '))
    scoreList.append(score)
    while score != '0':
        score = int(input('Please enter the next students score, or "0" to quit: '))
        scoreList.append(score)
        
        if score == 0:
            break
        
    
        else:
            score = int(input('Please enter the next students score, or "0" to quit: '))
            scoreList.append(score)
            continue

    return scoreList




#printing list
def printList(studentList, scoreList):
    nam = input('Please enter the stundent name to see their score, or "q" to leave program.')
    while nam != 'q':
        for x in range(len(studentList)):
            if studentList[x] != nam:
                print('Sorry I could not find that student')
                break
            else:
                if studentList[x] == nam:
                    print(studentList[x], 'got a', scoreList[x])
                break
                
        nam = input('Please enter the stundent name to see their score, or "q" to leave program.')

#main function
def main():
    studentList = createStudent()
    fillStudent(studentList)
    scoreList = createScore()
    fillScore(scoreList)
    printList(studentList, scoreList)

#call the main function
main()
        
