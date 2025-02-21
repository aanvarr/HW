import time
import random

def decorator_1(func):
    def wrapper(*my_args1, **variable1):
        first_time = time.time()  
        returning = func(*my_args1, **variable1)  
        final_time = time.time()  
        execute_qiladigan_time = final_time - first_time  
        print(f"{func.__name__} call executed in {execute_qiladigan_time:.7f} sec") 
        return returning  
    return wrapper

@decorator_1
def funcA():
    print("Let's gooo!")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)

@decorator_1
def funx(n=2, m=5):
    print("How much money?")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

if __name__ == "__main__":
    funcA()
    funx()
    funcA()
    funx()
    funcA()
