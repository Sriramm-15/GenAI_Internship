# Prime Number Generator

# Function to check if a number is prime or not
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

start = input("Enter the start of the range:")
end = input("Enter the end of the range:")

try:
    #typecasting 
    start = int(start)
    end = int(end)

    if start<= 0 or end<= 0:
        print("Both numbers must be positive")
    elif start > end:
        print("Start of range must be less than or equal to end")
    else:
        print("Prime numbers in the range:")
        count = 0
        for number in range(start, end + 1):
            if is_prime(number):
                print(number, end=" ")
                count=count+1
                if count == 10:  # Print 10 numbers per 1 line
                    print()
                    count = 0
        if count != 0:  # print next numebrs in new line
            print()

except ValueError:
    print("Enter positive integers")
