# Our quiz!
## moved score to outside of def quiz so that it becomes a global score and
##we can split our quiz up into different questions but it will still add up
##our score as we go along but it means we can test questions one at a time
## which is good if we have lots of questions

score = 0

def quiz():

 

##when we put an input in need to put a prompt with it like ("Enter name:  ")
        
    name = input("Enter name: ")

    print("Hello " + name)

    question1()

def question1():
    global score

    print("Which Disney character is named after a planet?")
    print("a. Mickey Mouse")
    print("b. Donald Duck")
    print("c. Pluto")
    print("d. Bambi")
    answer = input("Choose an option:  ")

    if answer.lower() == "c":
        score = score + 100
        print("Well done")

    else:
        print("Sorry - the answer was c. Pluto")

    question2()

def question2():
    global score
    
    print("Which of the following is not a Disney Character?")
    print("a. Eeyore")
    print("b. Ariel")
    print("c. Minni Mouse")
    print("d. Harry Potter")
    answer = input("Choose an option:  ")

    if answer.lower() == "d":
        score = score + 100
        print("Well done")

    else:
        print("Sorry - the answer was d. Harry Potter")

    
    
    question3()

def question3():
    global score

    print("What is the little girl called in Inside out?")
    print("a. Riley")
    print("b. Joy")
    print("c. Holly")
    print("d. Ellie")
    answer = input("Choose an option:  ")
          
    if answer.lower() == "a":
        score = score + 100
        print("Well done")

    else:
        print("Sorry - the answer was a. Joy")
        
          
    print("You've scored", score)


# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
