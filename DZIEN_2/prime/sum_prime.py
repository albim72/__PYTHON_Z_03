def find_prime_numbers_sum(minimum, maksimum):
    total = 0
    for number in range(minimum,maksimum+1):
        count = 0
        for i in range(2,(number//2+1)):
            if number%i == 0:
                count += 1
                break
            if count==0 and number!=1:
                total = total +number