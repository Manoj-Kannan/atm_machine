print("Welcome to Bank of Parota ATM")
restart = 'Y'
chances = 3							#the total number of tries a user can perform in case of incorrect password
balance = 100

while chances >= 0:
    pin = int(input("Enter your ATM pin: "))
    if pin == (1234):
        print("You have entered your pin correctly")
        while restart not in ('n','no','NO','N'):
            print("Press 1 to check your balance \n")
            print("Press 2 to withdraw cash\n")
            print("Press 3 to pay cash\n")
            print("press 4 to return card\n")
            option = int(input("Enter your choice: "))
            if option == 1:
                print("your available balance is : ",balance )
                restart = input("Would you wish to continue: ") 
                if restart  in ('n','no','NO','N'):		#gets input from the user and if the input is not in the tuple specified before, the programs executes from the beginning(4 options)
                    print("Thank you")
                    break
            elif option == 2:
                withdraw = int(input("10/20/30/40/50/60/70/80/90/100 \nEnter the amount you wish to withdraw: "))
                if withdraw in [10,20,30,40,50,60,70,80,90,100]:
                    balance = balance - withdraw
                    print("your available balance is ",balance)
                    restart = input("Would you wish to continue: ") 
                    if restart  in ('n','no','NO','N'):
                        print("Thank you")
                        break
                else:
                    print("Invalid amount please retry!!")
                    restart = 'y' #returns back to the 4 options

            elif option == 3:
                pay = int(input("enter the amount you wish to pay : "))
                balance = balance + pay
                print("your available balance is ",balance)
                restart = input("Would you wish to continue: ") 
                if restart  in ('n','no','NO','N'):
                    print("Thank you")
                    break

            elif option == 4:
                print("thank you")				#greets and quit the program
                quit()

    elif pin != ('1234'):
        print("incorrect pin!!")
        chances-=1 						#Returns to enter your atm pin

        if chances == 0:
            print("no more tries")
            break
