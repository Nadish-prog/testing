import random

def generate_random_number(start, end):
    return random.randint(start, end)

if __name__ == "__main__":
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    random_number = generate_random_number(start, end)
    print(f"Random number between {start} and {end}: {random_number}")