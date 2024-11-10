def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for k in range(2, int(result)):
            if int(result) % k == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
        return result
    return wrapper

@is_prime
def sum_three(*args):
    result = sum(args)
    return result

result = sum_three(2, 3, 6)
print(result)
result = sum_three(8,9,15)
print(result)
result = sum_three(9,25,39)
print(result)