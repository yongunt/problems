Is the Number a Prime? (with a twist)
Write a function that takes a number and returns True if it's a prime; False otherwise. The number can be 2^64-1 (2 to the power of 63, not XOR). With the standard technique it would be O(2^64-1), which is much too large for the 10 second time limit imposed by Edabit.

Sieve of Eratosthenes

Examples
prime(7) ➞ True

prime(56963) ➞ True

prime(5151512515524) ➞ False

Notes
A "prime" number is a number that can only be divided by itself and 1 (upon division the result is a whole number).


source --> https://edabit.com/challenge/EcBpRwgYsbmEWXKB9