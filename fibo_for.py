# Creating fibonacci series with for loop and function

def fibo_func(fibo_range):
    p1 = 0
    p2 = 1
    for i in fibo_range:
        if i<=1:
            print(f"Fibo Value : {i}")
        else:
            cur_value = p1+p2
            print(f"Fibo Value : {cur_value}")
            p1 = p2
            p2 = cur_value


fibo_func(range(0,10))

# ls = range(0,10)
#fibo_func(ls)
