#Expense Tracker Project
print("Welcome to Expense Tracker\n")
print("======MENU======")
print("1.Add Expense\n2.View All Expenses\n3.View Total Spending\n4.Exit")
print("==================")
expenses=[]#list of expenses in form of dictionary
total_spent=0
count=0#Expenses added
while True:
    choice=input("Enter your choice (1-4):")
    #Add Expense
    if choice=="1":
        date=input("Enter the date(dd/mm/yyyy):")
        category=input("Enter the category:")
        description=input("Enter the description:")
        amount=float(input(f"Enter the amount spent for {category}"))
        dict_expense={"Date":date,
                      "Category":category,
                      "Description":description,
                      "Amount":amount
                     }
        expenses.append(dict_expense)#Adding expense in the list
        total_spent+=amount#Total spending
        count+=1
        print("Expense added successfully.\n")
    #View Expense
    elif choice=="2":
        if len(expenses)==0:
            print("NO Expenses added.\nFirst add the expenses to view")
        else:
            
            print(f"======YOUR EXPENSES=====\nYou have spent a money {count} times")
            number=1
            for item in expenses:
                print(f"Expense number {number} :{item['Date']},{item['Category']},{item['Description']},{item['Amount']}\n")
                number+=1
    #view Total Spending
    elif choice=="3":
        print(f"You have spent a total money of Rs.{total_spent}\n")
    #Exit
    elif choice=="4":
        print("Thank You for exploring Expense Tracker")
        break
        
    else:
        print("Invalid Choice! Try again(1-4)")
        
        
