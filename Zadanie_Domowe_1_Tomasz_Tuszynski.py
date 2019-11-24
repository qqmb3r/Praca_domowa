def primes(number):
    #if isinstance(number, int) == False:
    #    print("This is not an integer, please set another number!")
    #   return 0
    if number > 1:
        for i in range(2,number):
                if (number % i) == 0:
                    return 0
                    break
        else:
            return 1
def firstNprimes(N):
    if N < 2:
        print("N/A")
    if N == 2:
        print("2")
    if N>2:
        i=1
        MyResult = 0
        while MyResult<N:
            i+=1
            a = primes(i)
            if a == 1:
                print(i)
                MyResult+=1
                a = 0
firstNprimes(55)

