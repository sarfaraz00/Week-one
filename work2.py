a=[(10, 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
print([t[:-1] + (100,) for t in a])

letter = "tHis iS mE"
print(letter.swapcase())

string = 'ABCDCDC'
substring = 'CDC'
count = string.count(substring)
print(count)