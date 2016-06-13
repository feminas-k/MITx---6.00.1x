fixedmonthlypayment = 0
b = balance
a = annualInterestRate
while True:
    #loop over each month of a year
    for i in range(1,13):
        remainingbalance = balance - fixedmonthlypayment
        balance = round((remainingbalance + remainingbalance*annualInterestRate / 12.0), 2)
    #if the balance is less than or equal to zero,print out value of fixedmonthlypayment,break the loop
    if balance <= 0:
        print("Lowest payment: "+ str(fixedmonthlypayment))
        break
    else:
        #if the balance is not less than or equal to zero, increment fixedmonthlypayment by 10,continue loop
        fixedmonthlypayment +=10
        balance =b
        annualInterestRate = a
