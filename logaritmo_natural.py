def fatorial(n):
    if n < 0: return "Fatorial não existe para negativos" 
    fat = 1
    for i in range(2, n + 1): 
        fat *= i 
    return fat

def Euler():
    e = 0 
    for n in range(1000):
        e += 1/fatorial(n) 
    return e 

