def romanToInt(s):
    values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    prev =0
    total = 0
    
    for c in reversed(s):
        print(c)
        cur = values[c]
        if cur < prev:
            total -= cur
        else:
            total += cur
        prev = cur
    return total
        

print(romanToInt("MCMXCIV"))