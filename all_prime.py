def check_prime_num(number):
    if number > 1:
        for i in range(2 , int(number)):
            if number % i == 0:
                print(number, "not prime number")
                break
        else:
            print(number, "prime number")
check_prime_num(173)