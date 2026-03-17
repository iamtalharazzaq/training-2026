def print_table(n):
    print(f"\nMultiplication Table for {n}")
    print("-" * 27)
    for i in range(1, 13):
        # Right-align both numbers and result
        print(f"{n:2} x {i:2} = {n * i:3}")


def get_valid_number():
    while True:
        try:
            n = int(input("Enter a number between 1 and 12: "))
            if 1 <= n <= 12:
                return n
            else:
                print("Invalid Number, try again...!")
        except ValueError:
            print("Invalid input...!")


num = get_valid_number()
print_table(num)

# Bonus
print("\n--- Multiplication Tables for 1 to 12 ---")
for n in range(1, 13):
    print_table(n)
