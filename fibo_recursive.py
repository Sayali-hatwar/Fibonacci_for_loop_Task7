# creating fibonacci series with recursive function

def fibo_recur(n):
    if n <= 1:
        return n
    return fibo_recur(n-1) + fibo_recur(n-2)


for i in range(10):
    print(f"Fibo Value : {fibo_recur(i)}")

