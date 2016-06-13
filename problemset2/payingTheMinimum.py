totalpaid = 0 
for i in range(1,13):
    print ("Month: " + str(i))
    minmonthlypayment = round((balance * monthlyPaymentRate),2)
    totalpaid += minmonthlypayment
    print ("Minimum monthly payment: " + str(minmonthlypayment))
    remainingbalance = balance - minmonthlypayment
    balance = round((remainingbalance + remainingbalance*annualInterestRate/12.0),2)
    print ("Remaining balance: " + str(balance))
    
print ("Total paid: ") + str(totalpaid)
print ("Remaining balance: " + str(balance))
