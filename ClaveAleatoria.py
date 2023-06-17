#! /usr/bin/python
#Hello, here is a script to generate random passwords

import random

letters = "abcdefghlijkmnopqrstvwyzABCDEFGHIJKLMNOPQRSTVWYZ"
numbers = "1234567890"
symbols = "!·$%&/()=?¿\|@#~¬{[]}¿¡+-*/"

chars = letters + numbers + symbols
length = 14
generator_pass = random.sample(chars, length)

#.join to delete spaces
password = "".join(generator_pass)

print(password)


#my native language is Spanish but I use English because it is a universal language and to practice it :D
