import math
import time

def welcome():
    print("======================")
    print("=====PRIME TESTER=====")
    print("======================")
def menu():
    print("What do you want to do?")
    print("1.Check if a number is prime")
    print("2.Display every prime number up to...")
    print("3.Benchmark!!!")
    
    while True:
        try:
            choice = int(input())
            if (choice not in range(1,3 + 1)):
                raise ValueError("")
        except:
            print("Please enter a correct option!")
        break
    procedure(choice)
def menuBenchmark():
    print("======BENCHMARK======")
    print("Choose your benchmark")
    print("1.10000 Primes")
    print("2.100000 Primes")
    print("3.1000000 Primes")
    print("4.10000000 Primes")
    print("5.Custom settings")

    while True:
        try:
            choice = int(input())
            if (choice not in range(1,5 + 1)):
                raise ValueError("")
        except:
            print("Please enter a correct option!")
        break
    
    if choice == 1:
        return 10000
    elif choice == 2:
        return 100000
    elif choice == 3:
        return 1000000
    elif choice == 4:
        return 10000000
    elif choice == 5:
        number = int(input("Enter a custom setting..."))
        return number
def procedure(choice):
    if choice == 1:
        checkPrime()
    elif choice == 2:
        print("Check primes up to...")
        checkUpTo()
    elif choice == 3:
        benchmark()
def checkPrime():
    nb = int(input("Enter a number to check..."))
    if isPrime(nb):
        print(nb, "is prime!!")
    else:
        print(nb, "isn't prime. :-(")
def checkUpTo(a = 0):
    if a == 0:
        nb = int(input())
    else:
        nb = a
    for i in range(2, nb + 1):
        if isPrime(i) == True:
            print(i)
def benchmark():    
    nb = menuBenchmark()

    time1 = time.time()
    checkUpTo(nb)
    time2 = time.time()

    print("Test took", time2 - time1, "second(s) to calculate prime numbers up to", nb)
def space(line = 1):
    for i in range(0, line):
        print("")
def enterNumber():
    print("Enter a number to test...")
    nb = int(input())
    return nb
def isPrime(nb):
    if isDivisibleByTwoOrFive(nb) == False:
        if isDivisibleByThree(nb) == False:
            if isDivisibleByMoreThanSeven(nb) == False:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def isDivisibleByTwoOrFive(nb):
    nb = str(nb)
    if (nb[len(nb) - 1] == '0' or nb[len(nb) - 1] == '2' or nb[len(nb) - 1] == '4' or nb[len(nb) - 1] == '5' or nb[len(nb) - 1] == '6' or nb[len(nb) - 1] == '8'):
        return True
    else:
        return False
def isDivisibleByThree(nb):
    nb = str(nb)
    sum = 0
    for i in range(0, len(nb)):
        sum += (int)(nb[i])
    if (sum % 3 == 0):
        return True
    else:
        return False
def isDivisibleByMoreThanSeven(nb):
    i = 7
    init = 0
    while i <= math.ceil(math.sqrt(nb)) + 1:
        if nb % i == 0:
            return True
        if init == 0 or init == 2:
            i += 4
            init = 0
        else: 
            i += 2
            init += 1
    return False

welcome()
menu()