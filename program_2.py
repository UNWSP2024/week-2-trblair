#Friend average age-ifier
#Made by Tristan Blair, 9/9/24
def average_age():
    # Get User Input
    print("How old are your friends?")
    friend1=int(input())
    friend2=int(input())
    friend3=int(input())
    friend4=int(input())
    friend5=int(input())
    # Sum ages
    totalage=friend1+friend2+friend3+friend4+friend5
    # Average the ages
    finalage=totalage//5
    # Print the results
    print(finalage)
# Line which calls the above function.
average_age()
