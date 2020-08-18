# import random
from random import SystemRandom

# method-1
# Standard pseudo-random generators are not suitable for security/cryptographic purposes.

# num_len = 8
# x = [random.randint(0,9) for i in range(num_len)]
# new_x = "".join(map(str,x))
# print("No1:", new_x)


# method-2 to resolve method-1
# type: ignore
cryptogen = SystemRandom()
x = [cryptogen.randrange(9) for i in range(8)]
num = "".join(map(str, x))
print("No:", num)
