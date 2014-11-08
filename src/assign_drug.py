#filename = 'inflammation_1.dat'
#print filename[-5]

def assign_drug(filename):
    if int(filename[-5]) % 2 == 1:
        return 'tylenol'
    else:
        return 'placebo'

import sys
filename = sys.argv[1]  # for using in script
print assign_drug(filename)
#print filename
    
assert assign_drug('inflammation_1.dat') == 'tylenol'
assert assign_drug('inflammation_3.dat') == 'tylenol'
assert assign_drug('inflammation_4.dat') == 'placebo'
