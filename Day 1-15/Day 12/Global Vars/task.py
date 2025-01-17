def is_prime(num):
    limit = int(num/2)
    while limit > 1:
        if num%limit ==  0:
            return False
        limit-=1
    return True
print(is_prime(7))