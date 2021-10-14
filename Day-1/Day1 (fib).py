n = int(input());
fib_arr=[0,1];
def fib(n):
    if n>len(fib_arr):
        temp = fib(n-1) + fib(n-2);
        fib_arr.append(temp);
        return temp;
    else:
        return fib_arr[n-1];
fib(n);
print(fib_arr);