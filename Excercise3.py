'''
Created on Apr 12, 2022

@author: michaelmordec
'''
def main():
    pennies=int(input("enter number of pennies: "))
    nickels=int(input("enter number of nickels: "))
    dimes=int(input("enter number of dimes: "))
    quarters=int(input("enter number of quarters: "))
    
    total = pennies*1 + nickels*5 + dimes*10 + quarters*25
    
    if(total==100):
        print("You Win!")
    elif(total < 100):
        print("Too Low!")
    elif(total > 100):
        print("Too High!")

main()