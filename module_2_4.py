numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    is_primes = True
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            is_primes = False
            not_primes.append(numbers[i])
            break
    if is_primes == True:
        primes.append(numbers[i])
print('Primes:', primes)
print('Not Primes:', not_primes)
