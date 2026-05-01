# <>
# Python program - Egyptian fraction in Egyptian Form using Greedy Algorithm

import math
# import fractions
# import functools

def egyptian_frac(numerator, denominator):
    # Creating our list of denominators for our Egyptian Fractions
    egypt_lst = []
    while numerator != 0:
        
        x = math.ceil(denominator/numerator)
        egypt_lst.append(x)
        
        numerator = x * numerator - denominator
        denominator *= x
        
    str = ""
    
    for ones in egypt_lst:
        str += "1/{0} + ".format(ones)
        
    final_string = str[:-3]
    
    return final_string

print(egyptian_frac(7, 12))