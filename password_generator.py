import secrets
import string
import argparse


def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):

    charset = ""

    if use_upper:
        charset += string.ascii_uppercase
    if use_lower:
        charset += string.ascii_lowercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += "!@$&"

    if not charset:
        raise ValueError("At least one character type must be selected.")


    required_chars = []
    if use_upper:
        required_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        required_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        required_chars.append(secrets.choice(string.digits))
    if use_symbols:
        required_chars.append(secrets.choice("!@$&"))


    remaining = [secrets.choice(charset) for _ in range(length - len(required_chars))]


    password_chars = required_chars + remaining
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():
    parser = argparse.ArgumentParser(description="Secure Password Generator")
    parser.add_argument("-l", "--length",    type=int, default=16,           help="Password length (default: 16)")
    parser.add_argument("-n", "--count",     type=int, default=1,            help="Number of passwords to generate (default: 1)")
    parser.add_argument("--no-upper",        action="store_true",            help="Exclude uppercase letters")
    parser.add_argument("--no-lower",        action="store_true",            help="Exclude lowercase letters")
    parser.add_argument("--no-digits",       action="store_true",            help="Exclude digits")
    parser.add_argument("--no-symbols",      action="store_true",            help="Exclude symbols")
    args = parser.parse_args()

    while True:
        try:
            length_input = input("Enter password length: ").strip()
            if not length_input:
                print("Error: Please enter a number.")
                continue
            args.length = int(length_input)
            break
        except ValueError:
            print("Error: Please enter a valid number.")

    if args.length < 4:
        print("Error: Password length must be at least 4.")
        return

    if args.length > 30:
        print("Error: Max password length is 30 characters.")
        return

    print(f"\n Generated Password{'s' if args.count > 1 else ''}:\n")
    for i in range(args.count):
        pwd = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_lower=not args.no_lower,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
        )
        if args.count > 1:
            print(f"  {i + 1}. {pwd}")
        else:
            print(f"  {pwd}")
    print()


if __name__ == "__main__":
    main()
