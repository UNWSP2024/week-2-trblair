#5 item shopping list calculator
#Created on 9/9/24 by Tristan Blair
def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
    print("What is the first item you would like to buy?")
    item1 = input()
    print("How much does this item cost?")
    item1price=int(input())
    print("What is the second item you would like to buy?")
    item2 = input()
    print("How much does this item cost?")
    item2price=int(input())
    print("What is the third item you would like to buy?")
    item3 = input()
    print("How much does this item cost?")
    item3price=int(input())
    print("What is the fourth item you would like to buy?")
    item4 = input()
    print("How much does this item cost?")
    item4price=int(input())
    print("What is the fifth item you would like to buy?")
    item5 = input()
    print("How much does this item cost?")
    item5price=int(input())
    #calculates the total cost of all items user has asked for
    totalcost=item1price+item2price+item3price+item4price+item5price
    #calculates the tax on the order, assuming a rate of 7%
    tax=totalcost*0.07
    finalcost=totalcost+tax
    print("Your subtotal is ",totalcost)
    print("Your sales tax is", tax)
    print("Your total is ",finalcost)

calculate_total_purchase()
