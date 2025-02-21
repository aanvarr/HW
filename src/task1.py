def kwargsAcceptFun(**event4):
        if not event4:
            print("NO data entered")
        else:
            print("Received arguments:")
            for a2, b2 in event4.items():
                print(f"{a2}: {b2}") 

#e.g.
kwargsAcceptFun(name1="Messi", age1=37, location1="Rosario")
kwargsAcceptFun()
