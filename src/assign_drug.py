#filename = 'inflammation_1.dat'
#print filename[-5]

def assign_drug(filename):
    if filename[-5] == '1':
        return 'tylenol'
    elif filename[-5] == '4':
        return 'placebo'
    
assert assign_drug('inflammation_1.dat') == 'tylenol'
assert assign_drug('inflammation_3.dat') == 'tylenol'
assert assign_drug('inflammation_4.dat') == 'placebo'
