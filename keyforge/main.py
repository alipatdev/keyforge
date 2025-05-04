#!/usr/bin/env python3

import argparse
import secrets
import string

__version__ = "0.1.0"

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    alphabet = ''
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_lower:
        alphabet += string.ascii_lowercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation
    if not alphabet:
        raise ValueError("No character class selected.")
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(
        prog="keyforge",
        description="KeyForge: secure password generator from terminal"
    )
    parser.add_argument('-l', '--length', type=int, default=16,
                        help='Password length')
    parser.add_argument('-n', '--count', type=int, default=1,
                        help='Number of passwords to generate')
    parser.add_argument('--no-symbols', dest='symbols', action='store_false',
                        help='Exclude symbols')
    parser.add_argument('--no-numbers', dest='numbers', action='store_false',
                        help='Exclude numbers')
    parser.add_argument('--no-upper', dest='upper', action='store_false',
                        help='Exclude uppercase characters')
    parser.add_argument('--no-lower', dest='lower', action='store_false',
                        help='Exclude lowercase characters')
    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()

    for _ in range(args.count):
        print(generate_password(
            args.length, args.upper, args.lower, args.numbers, args.symbols
        ))

if __name__ == '__main__':
    main()