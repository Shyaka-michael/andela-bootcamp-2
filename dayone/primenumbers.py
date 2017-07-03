def primenumber(number):
    list_of_prime_numbers = []
    if type(number) == str:
        return "value incorect"
    if number > 0:
        for num in range(1, (number + 1)):
            if all(num % i != 0 for i in range(2, num)):
                list_of_prime_numbers.append(num)

        return list_of_prime_numbers
