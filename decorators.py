def hello_decorator(func):
    def inner1(*args, **kwargs):
        
        print("before Execution")
        
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")
        
        # returning the value to the original frame
        return returned_value
        
    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a * b

a, b = 1, 2

# getting the value through return of the function
# sum_two_numbers = hello_decorator (sum_two_numbers)
print("multiplication : " + sum_two_numbers(1, 2))
