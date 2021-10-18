n = int(input());
fib_arr=[0,1];
def fib(n):
    if n>len(fib_arr):
        temp = fib(n-1) + fib(n-2);
        fib_arr.append(temp);
        return temp;
    else:
        return fib_arr[n-1];

if n<=0:
    print('invalid input')
elif n==1:
    print([0])
else:
    fib(n)
    print(fib_arr)
