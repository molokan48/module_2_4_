numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16,17,18,19,20]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] !=1:
        for j in range( 2 , numbers[i] ):
           if numbers[i] % j == 0:
            not_primes.append(numbers[i])
            break
        else: primes.append(numbers[i])
print('primes' , primes)
print('not_primes' , not_primes)