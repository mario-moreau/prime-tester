# prime-tester
A Python program for doing things with prime numbers.

Launching the program grants you with a selection menu.
Here, three options open to you :
- Check if a number is prime
- Display every prime number up to a given number
- Benchmark your system with prime numbers

## Prime checking
Checking if a number is prime is done efficiently by three functions:
- isDivisibleByThree() checks the last digit of the number. If that digit is 0, 2, 4, 5, 6 or 8, then the number can't be prime because it can be at least divided by 2 or 5.
- isDivisibleByThree() checks the digital root of the number (sum of all digits). If the digital root of a number is divisible by three, then the number is divisible by three. For example, digital root of 123 is 1+2+3=6, 6 is divisible by 3, so 123 is divisible by three. It's a modular arithmetic trick, I remember seeing a demonstration for it in math courses, I have to find it again.
- isDivisibleByMoreThanSeven() searches for dividers equal or higher than 7. This function checks every non-previously tested number up to the square root of the number we are checking.

## Benchmark
You are able to benchmark your system with primes numbers.
The program searches for primes up to a given limit and records time taken by the operation.

## Improvements to be made:
- Algorithm has most likely room for improvements. It's already pretty optimized but I'm sure we can find primes faster ;)
- Benchmark has to be adjusted to fit a real-world usecase. Calculating too few primes doesn't provide an accurate measure with modern computers, and calculating too many can take more time than the universe's age...
- I would like to implement an option for choosing between single-threading and multi-threading. This program appears to take all threads by default. I have to learn how to handle threads, because it's now out of my reach.
