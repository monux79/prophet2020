def get_rec_fac(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else: 
        return n * get_rec_fac(n-1)

def get_itera_fac(n):
    if n < 0:
        return -1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *=i
        return fact
    
print(get_rec_fac(5))
print(get_itera_fac(6))
