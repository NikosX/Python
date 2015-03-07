def year_balance(b, r, p):
    for i in range(1, 13):
        ub = b - p
        b = ub + r * ub
    return b


b = float(balance)
r = float(annualInterestRate) / 12.0
maxp = int(year_balance(b, r, 0.0) / 12)
for p in range(0, maxp + 10, 10):
    if year_balance(b, r, p) <= 0:
        print "Lowest Payment: %d" % p
        break