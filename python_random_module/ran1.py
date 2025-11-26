import random

"""
1.random.seed()
-->The seed() method is used to initialize the random number generator.
                            (or)
   Initializes random number generator → makes results repeatable.
-->The random number generator needs a number to start with (a seed value), 
   to be able to generate a random number.
"""
random.seed(2)
print(random.random()) #Note :"Why is seed() used in test automation?"

#Demonstrate that if you use the same seed value twice, you will get the same random number twice:
random.seed(10)
print(random.random())
random.seed(10)
print(random.random())

"""
2)random.random()
--Returns a random float between 0.0 and 1.0.
"""

print(random.random())

"""
3)random.randint(a, b)
--Returns a random integer between a, b(inclusive)

"""
print(random.randint(10, 20))


"""
4)random.randrange(start, stop, step)
--Returns a random value from a range (stop is excluded).
"""
print(random.randrange(0, 10, 2))   # 0,2,4,6,8

"""
5)random.uniform(a, b)
--Returns a random float between a and b.
"""
print(random.uniform(1, 5))
"""
6)random.choice(sequence)
--Returns one random item from a list/string/tuple.
"""
print(random.choice(['red', 'blue', 'green']))

"""
7) random.choices(sequence, k=n)
--Returns multiple random items, allowing duplicates.
"""
print(random.choices([1,2,3], k=4))

"""
8)random.sample(sequence, k=n)
--Return unique random items (no duplicates).
"""
print(random.sample([1,2,3,4], k=2))

"""
9)random.shuffle(list)
--Shuffles a list in-place (modifies original list).
"""
mylist = [1,2,3,4]
random.shuffle(mylist) #Note :"Why doesn’t shuffle() work on strings or tuples?"
print(mylist)

"""
10)random.getrandbits(k)

--Returns a random integer with k random bits.
"""
print(random.getrandbits(4))   # 0 to 15 #Note:"How does getrandbits() help in generating large random integers?"

"""
11)random.triangular(low, high, mode)
Returns a float based on a triangular distribution.
"""
print(random.triangular(10, 20, 15)) #Note :"What is the role of the ‘mode’ parameter in triangular()?"

"""
12)random.betavariate(alpha, beta)
--Returns values using Beta distribution.
"""
print(random.betavariate(1, 3)) #Note :"In which real-world scenarios is betavariate() commonly used?"


