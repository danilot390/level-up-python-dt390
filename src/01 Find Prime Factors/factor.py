def get_prime_factors(number):
    factors = []
    div = 2
    while div <= number:
        if number % div == 0:
            factors.append(div)
            number /= div
        else:
            div += 1
    return factors


# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]
