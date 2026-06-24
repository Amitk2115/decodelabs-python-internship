import secrets
import string
import math


def get_password_length():
    while True:
        try:
            length = int(input("Enter desired password length (min 8): "))
            if length < 8:
                print("Too short. Minimum is 8 characters.")
            elif length > 64:
                print("Maximum allowed is 64 characters.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")


def get_character_options():
    print("\nCharacter options:")
    print("1. Letters + Numbers (alphanumeric)")
    print("2. Letters + Numbers + Special Characters (recommended)")

    while True:
        choice = input("Choose (1 or 2): ").strip()
        if choice in ("1", "2"):
            return choice
        print("Enter 1 or 2.")


def build_character_pool(choice):
    pool = string.ascii_letters + string.digits
    if choice == "2":
        pool += string.punctuation
    return pool


def generate_password(length, pool):
    # Enterprise approach: list + join = O(N), not O(N^2)
    return ''.join(secrets.choice(pool) for _ in range(length))


def calculate_entropy(length, pool_size):
    return length * math.log2(pool_size)


def display_result(password, pool):
    entropy = calculate_entropy(len(password), len(pool))

    print("\n" + "=" * 40)
    print(f"  Generated Password: {password}")
    print(f"  Length            : {len(password)}")
    print(f"  Character Pool    : {len(pool)} characters")
    print(f"  Entropy           : {entropy:.1f} bits")

    if entropy >= 128:
        strength = "VERY STRONG"
    elif entropy >= 80:
        strength = "STRONG"
    elif entropy >= 60:
        strength = "MODERATE"
    else:
        strength = "WEAK"

    print(f"  Strength          : {strength}")
    print("=" * 40)


def main():
    print("=== DecodeLabs Password Generator ===")
    print("  Powered by cryptographic randomness\n")

    while True:
        length = get_password_length()
        choice = get_character_options()
        pool = build_character_pool(choice)
        password = generate_password(length, pool)
        display_result(password, pool)

        again = input("\nGenerate another? (y/n): ").strip().lower()
        if again != 'y':
            print("Stay secure.")
            break


if __name__ == "__main__":
    main()