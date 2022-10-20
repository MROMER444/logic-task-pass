def check_prime_num(number):
    if number > 1:
        for i in range(2 , int(number)):
            if number % i == 0:
                print(number, "not prime")
                break
        else:
            print(number, "this is prime")
check_prime_num(173)