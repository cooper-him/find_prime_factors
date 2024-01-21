def find_prime_factors(big_num) :
    prime = 2
    list = [2]
    factor = 0
    int(big_num)
    while big_num % 2 == 0 :
        big_num = big_num / 2
        factor+=1
    fac_list = [factor]
    print(big_num)
    while big_num != 1 :
        factor = 0
        prime += 1
        is_prime = True
        for num in list :
            if prime % num == 0 :
                is_prime = False
                break
            if num > prime**0.5 + 1 :
                break
        if is_prime == True :
            list = list + [prime]
            while big_num % prime == 0 :
                big_num = big_num / prime
                factor+=1
            fac_list += [factor]
            if factor != 0 :
                print(big_num)
    return fac_list, list


import time

while True :

    big_num=int(input("the big num :"))
    start=time.time()
    fac_list, prime_list = find_prime_factors(big_num)
    end1=time.time()
    print("the prime factors of the big num is : ")
    withx=True
    for i in range(0, len(prime_list)) :

        if withx :
            if not fac_list[i] == 0 and not fac_list[i] == 1 :
                print(f" {prime_list[i]}^{fac_list[i]} ", end='')
                withx=False
            elif not fac_list[i] == 0 :
                print(f" {prime_list[i]} ", end='')
                withx=False
            continue

        if not withx :
            if not fac_list[i] == 0 and not fac_list[i] == 1 :
                print(f"* {prime_list[i]}^{fac_list[i]} ", end='')
            elif not fac_list[i] == 0 :
                print(f"* {prime_list[i]} ", end='')
    end2=time.time()
    print()
    print(f"计算用时: {(end1-start):.3f}s, 排列输出用时: {(end2-end1):.3f}s")
    print()