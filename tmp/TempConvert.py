# TempConvert.py
val = input("please input temperature")
if val[-1] in ['C','c']:
    f = 1.8 * float(val[0:-1]) + 32
    print('Converted temperature is %.2fF '%f)
elif val[-1] in ['F','f']:
    c = (float(val[0:-1]) - 32)/1.8
    print('Converted temperature is : %.3fC '%c)
else:
    print('incorrect input ')