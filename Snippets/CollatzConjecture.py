# This program applies the Collatz conjecture
# A sequence defines as such that any positive integer
# If it's even, half it. If it's odd, multiply by 3 and add 1
# Eventually the sequence will always reach 1
def conjecture(number):
    print(number)
    if number == 1:
        return
    elif number%2 == 0:
        return conjecture(number//2)
    else:
        return conjecture(number*3+1)

def main():
    try:
        user_input = input("Enter a positive integer: ")
        if user_input.isdigit() and int(user_input) > 0:
            user_input = int(user_input)
        else:
            raise ValueError
    except ValueError:
        print("Must be a positive integer")
    number = conjecture(user_input)

main()
