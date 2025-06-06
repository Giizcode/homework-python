#1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#2
def digit_sum(k):
    return sum(int(d) for d in str(k))


#3
def powers_of_two(N):
    power = 1
    result = []
    while power * 2 <= N:
        power *= 2
        result.append(power)
    return result
