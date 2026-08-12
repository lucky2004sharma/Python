print("this is my 5th programm")

print("----------WELCOME TO QUIZ GAME----------")

name = input("Please enter your name : ")

print(f"Welcome to {name} Game")

while True:
    
    score = 0
    
    
    print("Q1. What is the capital of INDIA")
    print("a. Delhi")
    print("b. Mumbai")
    print("c. Kolkata")
    print("d. Gujarat")
    
    answer = input("plz. Choose answer : ")
    if answer in ["a", "b", "c","d"]:
        if answer == "a":
            score = score + 1 
            print("Correct answer : ")
            
        else:
            print("Wrong answer : ")   
        
        
    else:
        print("choose only btwn a,b,c,d :")
        
    
    print("Q2. In what year did World War II end?  ")
    print("a. 1944")
    print("b. 1947")
    print("c. 1946")
    print("d. 1945")
    
    answer = input("plz. Choose answer : ")
    if answer in ["a", "b", "c","d"]:
        if answer == "d":
            score = score + 1 
            print("Correct answer : ")
            
        else:
            print("Wrong answer : ")
               
        
    else:
        print("choose only btwn a,b,c,d :")
    
    
    print("Q3. Which planet is closest to the sun? ")
    print("a. Venus")
    print("b. Mercury")
    print("c. Mars")
    print("d. Jupiter")
    
    answer = input("plz. Choose answer : ")
    if answer in ["a", "b", "c","d"]:
        if answer == "b":
            score = score + 1 
            print("Correct answer : ")
            
        else:
            print("Wrong answer : ")
               
        
    else:
        print("choose only btwn a,b,c,d :")
        
        
        
    print("Q4. Who has won the most total Academy Awards? ")
    print("a. Walt Disney")
    print("b. Pixar")
    print("c. Sony")
    print("d. Dream Works")
    
    answer = input("plz. Choose answer : ")
    if answer in ["a", "b", "c","d"]:
        if answer == "a":
            score = score + 1 
            print("Correct answer : ")
            
        else:
            print("Wrong answer : ")
               
        
    else:
        print("choose only btwn a,b,c,d :")
        
        
        
        
        
    print("Q5. What is a group of crows called?  ")
    print("a. Angel")
    print("b. Murder")
    print("c. Narnia")
    print("d. Herd")
    
    answer = input("plz. Choose answer : ")
    if answer in ["a", "b", "c","d"]:
        if answer == "b":
            score = score + 1 
            print("Correct answer : ")
            
        else:
            print("Wrong answer : ")
            
            
        break
        
    else:
        print("choose only btwn a,b,c,d :")
        

print("Total question is 5 and total score is ", score)
print(f"So, Total answer is {score}/5")
