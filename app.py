def add_numbers(a, b):
    return a + b
    
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero!")
    return a / b

def main():
    print("sum App")
    x = add_numbers(3, 5)
    print("Result:", x)

if __name__ == "__main__":
    main()
