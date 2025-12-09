import random
import string

def passwordgenerator(length: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

password = passwordgenerator()
print(f'Generate password: {password}')
# k = 42
# random.seed(k)
# pw = random.randint(4, 9)
# print(pw)