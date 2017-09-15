#Program for calculate the fibonacci number of user choice

n = int(input("Please enter a number to calculate fibonacci:")) #Here user will input his choice
# def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a = 0 # Here we can write a, b = 0, 1
    b = 1
    while b < n: # Here while loop will check condition that n is greater
        print b,
        a, b = b, a + b


# Now call the function we just defined:
fib(n)

