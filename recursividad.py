def ite(n):
    x=1
    while x<= n:
        print(f"Hola {x}")
        x += 1

def rec(x,n):
    if x == n:
        print(f"Hola {x}")
    else:
        print(f"Hola {x}")
        rec(x+1, n)

def ite2(n):
    x=n
    while x>= 1:
        print(f"Hola {x}")
        x -= 1

def rec2(x):
    if x == 1:
        print(f"Hola {x}")
    else:
        print(f"Hola {x}")
        rec2(x-1)
    
    
#####
rec2(10)