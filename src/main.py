from task1 import kwargsAcceptFun

kwargsAcceptFun(name1="Messi", age1=37, location1="Rosario")
kwargsAcceptFun()

from task2 import typeBasedTransformer
information = {
    'a': 13,
    'b': 4.5,
    'c': "Sekin",
    'd': False,
    'e': [6, 4, 3],
    'f': {"hw": 5, "ts": 6},
    'g': None,
    'h': (2, 8, 10)
}

output1 = typeBasedTransformer(information)
print(output1)
from task3 import funcA,funx
if __name__ == "__main__":
    funcA()
    funx()
    funcA()
    funx()
    funcA()
