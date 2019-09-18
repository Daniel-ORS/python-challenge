budgetData="budget_data.csv"
import csv
with open(budgetData, "r") as budgetData:
    csvreader=csv.reader(budgetData,delimiter=",")
    #print(csvreader)
    csv_header=next(csvreader)
    
    numMonths=[]
    total=[]
    d=[]

    for row in csvreader:
        numMonths.append(row[0])
        total.append(int(row[1]))
        
    for i in range(len(total)-1):
        d.append(total[i+1]-total[i])

greatestIncrease=max(d)
greatestDecrease=min(d)
increaseIndex=d.index(greatestIncrease)+1
decreaseIndex=d.index(greatestDecrease)+1

   
result=f''' 
    \n
    Financial Analysis
    ---------------------------------
    Total Months: {len(total)}
    Total: ${sum(total)}
    Average Change: ${round(sum(d)/len(d),2)}
    Greatest Increase in Profits:{numMonths[increaseIndex]}, ${greatestIncrease}
    Greatest Decrease in Profits:{numMonths[decreaseIndex]}, ${greatestDecrease}
    \n
'''
print(result)

textFile=open("PyBankResults.txt","w")
textFile.write(result)





















   

