def fib (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(fib(n-1)+fib(n-2))

n = int (input('請輸入所要計算第幾個費式數列：'))
for i in range (n+1):
    print('fib(%d)=%d' %(i,fib(i)))