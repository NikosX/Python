balance = 10000
monthlyPaymentRate = 100
annualInterestRate = 0.10
b = float(balance)
r = float(annualInterestRate) / 12.0
p = float(monthlyPaymentRate)
sumpaid = 0

for i in range(1,13):

    q = p * b

    ub = b - q

    b = ub + r * ub

    sumpaid += q

    print "Month: %d" % i
    print "Minimum monthly payment: %.2f" % q
    print "Remaining balance: %.2f" % b

print "Total paid: %.2f" % sumpaid
print "Remaining balance: %.2f" % b