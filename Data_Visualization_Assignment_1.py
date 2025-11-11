#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(3):
    print("Rishu Thakur")


# In[2]:


a = 10
b = 20
c = 30
sum = a + b + c
print("The sum is:", sum)


# In[3]:


str1 = "Hello"
str2 = "Python"
str3 = "World"
result = str1 + " " + str2 + " " + str3
print("Concatenated string:", result)


# In[4]:


for i in range(1, 11):
    print("7 x", i, "=", 7 * i)

print()

for i in range(1, 11):
    print("9 x", i, "=", 9 * i)


# In[19]:


n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# In[6]:


n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum from 1 to", n, "is:", total)


# In[20]:


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Maximum is:", max(a, b, c))


# In[21]:


n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    if i % 7 == 0 and i % 9 == 0:
        total += i
print("Sum of numbers divisible by 7 and 9:", total)


# In[22]:


n = int(input("Enter a number: "))
total = 0
for i in range(2, n + 1):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        total += i
print("Sum of prime numbers from 1 to", n, "is:", total)


# In[23]:


def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total

n = int(input("Enter a number: "))
print("Sum of odd numbers from 1 to", n, "is:", sum_of_odds(n))


# In[17]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(n):
    total = 0
    for i in range(2, n + 1):
        if is_prime(i):
            total += i
    return total

n = int(input("Enter a number: "))
print("Sum of prime numbers from 1 to", n, "is:", sum_of_primes(n))


# In[16]:


a = 20
b = 30
c = a + b
print(a, "+" ,b, "=" ,c)


# In[15]:


a = "Rishu"
b = "is from"
c = "Hamirpur"

concatenated_string = a + " " + b + " " + c

print(concatenated_string)


# In[14]:


for i in range(1, 11):
    print(7, "*" ,i, "=" ,i * 7)


# In[12]:


n = int(input("Enter the number"))
for i in range(1,11):
    print(n, "*" ,i, "=" ,i * n)


# In[27]:


n = int(input("Enter a number: "))
sum_n = n * (n + 1) // 2
print(sum_n)


# In[7]:


def multiply(a,b):
    c = a * b
    return c 
print(multiply(10,5))

