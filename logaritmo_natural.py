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

def ln(x, termos=50):
    if x <= 0:
        return "Logaritmo indefinido"

    y = x - 1  # porque usamos ln(1 + y)

    resultado = 0

    for n in range(1, termos + 1):
        termo = ((-1)**(n+1)) * (y**n) / n
        resultado += termo

    return resultado


print(ln(2))