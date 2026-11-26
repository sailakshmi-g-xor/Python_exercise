def is_prime(n):
    if(n<2):
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            return False     
    return True
def primes_up_to(limit):
    l = []
    for n in range(limit+1):
        if is_prime(n):
            l.append(n)
        else:
            continue
    return l
n = input()
l = [int(num) for num in n.split(" ")]
for num in l:
    if is_prime(num):
        print(f"{num} is prime")
    else :
        print(f"{num} is not prime")
primes = primes_up_to(50)
print(f"{"The prime numbers upto 50 are"}:{primes}")
print("Count:",len(primes)) 

