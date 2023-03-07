print("WELCOME TO PYTHON QUIZ!!!")
playing=input("DO YOU WANT TO PLAY?")
if playing.lower()!="yes":
    quit()
print("OKAY !! LETS PLAY !!!")
score=0
answer=input("who developed python?")
if answer.lower()=="guido van rossum":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!")
answer=input("what is the extension of python files?")
if answer.lower()==".py":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!")
answer=input("what are like container that are used to store data?")
if answer.lower()=="variables":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!")
answer=input("Which character is used to give single-line comments in Python?")
if answer.lower()=="#":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!!")
answer=input("Which keyword is used for function in Python language?")
if answer.lower()=="def":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!")
answer=input(" What are the two main types of functions in Python?")
if answer.lower()=="built-in function and user defined function":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!")
answer=input("which function is used to returns the identity of the object in python?")
if answer.lower()=="id()":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!")
answer=input("which Python operator responsible for declaring variables?")
if answer.lower()=="assignment operator":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!")
answer=input("which operator is used to concatenate two strings?")
if answer.lower()=="+":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!")
answer=input("which function is used to find the length of a string in python?")
if answer.lower()=="len() ":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!")
print("YOU GOT "+str(score)+" QUESTION CORRECT")
print("YOU HAVE GOT"+str((score/10)*100)+"%")