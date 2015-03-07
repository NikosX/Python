def year_balance(b, r, p):
    for i in range(1, 13):
        ub = b - p
        b = ub + r * ub
    return b
    
def search_minpay(L, U):
    if U - L < 0.00005:
        return L
    M = (L + U) / 2.0
    if year_balance(b, r, M) <= 0.0:
        return search_minpay(L, M)
    else:
        return search_minpay(M, U)


b = float(balance)
r = float(annualInterestRate) / 12.0
minp = b / 12.0
maxp = year_balance(b, r, 0.0) / 12.0
p = search_minpay(minp, maxp)
print "Lowest Payment: %.2f" % p