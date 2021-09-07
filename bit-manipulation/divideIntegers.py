'''
https://www.geeksforgeeks.org/divide-two-integers-without-using-multiplication-division-mod-operator/
'''
def divide(A, B):
    sign = (-1 if((A < 0) ^
                (B < 0)) else 1)
    
    # remove sign of operands
    dividend = abs(A)
    divisor = abs(B)
    INT_MAX = pow(2,31)-1
    # Initialize
    # the quotient
    quotient = 0
    temp = 0
        
    # test down from the highest
    # bit and accumulate the
    # tentative value for valid bit
    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i
            quotient |= 1 << i
    #if the sign value computed earlier is -1 then negate the value of quotient
    if sign ==-1 :
        quotient=-quotient
    if quotient > INT_MAX: 
        return INT_MAX
    return quotient

print(divide(49, 6))