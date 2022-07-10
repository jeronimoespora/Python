n1=int(input("Introduce el primer numero: "))
n2=int(input("Introduce el segundo numero: "))





def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

for i in range(n1,n2):
    if is_prime(i) == True:
        print(str(i))
    else:
        pass