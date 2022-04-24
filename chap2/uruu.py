def is_Uruu(n):
    if n % 4 == 0:
        return True
    elif (n % 100 == 0) and (n % 400 != 0):
        return False
    else:
        return False

for i in range(1950, 2051):
    if is_Uruu(i):
        print(i, end=' ')
