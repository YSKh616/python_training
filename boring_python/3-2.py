import random

def get_answer(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 3
    elif num == 4:
        return 4

num = random.randint(1, 4)
r = get_answer(num)
print(r)
