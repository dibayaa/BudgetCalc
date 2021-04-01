import pandas as pd 
import matplotlib.pyplot as plt

# read in file
df = pd.read_csv('cashflow.csv', index_col ='Date', 
parse_dates = True)
df.head()

#name = input("what is your name: ")

#monthly salary
#expenses, create a dictionary for expense categories

#dictionary can be necessary expenses and fun stuff and
#  you can do calculations with the 'fun stuff'
#
# dictionary = {'housing': , 'food': ,'clothing': , 'transportation': , 
# 'fun stuff': , 'childcare/petcare': , 'cellphone': ,'health insurance': ,
# 'debt': ,'savings': , 'emergency fund': 
# }

#use pandas to create dataframe


#use matplotlib for visualization

# with open('expenses.txt', 'r') as expenses:

#     size_to_read = 10

#     expenses_contents = expenses.read(size_to_read)
#     print(expenses_contents,end='')

#     expenses.seek(0)
    
#     expenses_contents = expenses.read(size_to_read)
#     print(expenses_contents)
    


    # while len(expenses_contents) > 0:
    #     print(expenses_contents,end='*')
    #     expenses_contents = expenses.read(size_to_read)


#     fieldnames = ['housing','food','clothing','transportation','fun_stuff','childcare/petcare',
# 'cellphone','health_insurance','debt','savings','emergency_fund']
#     expensewriter = csv.DictWriter(csvfile.fieldnames = fieldnames)
    
    # expensewriter.writeheader()
    
    # expensewriter.writerow({
    #     # 'housing': '',
    #     # 'food': ''
    # })
  

#store the above in a dataframe
#export as a csv so user can save their monthly budget


#def monthly_pay:
    #pass


#def time_til_retire:
#    pass
#time value of money over time..valuation on 
# investments over time, adjust for salary and expense increase
