import sys


def main():
    amount = int(sys.argv[2])
    fiscal_units = int(sys.argv[3])
    if sys.argv[1] == 'FR':
        print "Total tax due: %.2f" % tax(amount, bands_fr, fiscal_units)

bands_fr = [(0, 6011),          \
            (5.5, 11991-6012),  \
            (14, 26631-11992),  \
            (30, 71397-26632),  \
            (41, 151200-71398), \
            (45,0-151201)]

def tax(income, bands, fiscal_units):
    
    bands = [(x[0], x[1]*fiscal_units) for x in bands];
    
    taxed = []
    tax = 0
    
    for band in bands:
        
        base = 0
        if band[1] > 0 and income >= band[1]:
            base = band[1]
        else:
            base = income
        rate = band[0]
        
        tax_increment = 0.01 * rate * base
        
        income -= base
        tax += tax_increment
        
        print "%.2f due after taxing %.2f at rate %.2f" % (tax_increment, base, rate)
        
        if income <= 0:           
            return tax
        
        
#        if band[1] > 0 and income >= band[1]:
#           tax += 0.01 * band[0] * band[1]
#          income -= band[1]
#     else:
#        tax += income * band[0] * 0.01
#       return tax
    


if __name__ == '__main__':
    main()
    
    
    
