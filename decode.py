#!/bin/python3

from string import ascii_lowercase
import sys

def decode_message(message):
    # Define the substitution rules
    orig = "rstuvwxyzponmlkedcbaqjihgf"

    # Create the mapping dictionary for both lowercase and uppercase
    substitution_dict = {orig[i]: ascii_lowercase[i] for i in range(len(orig))}
    substitution_dict.update({orig[i].upper(): ascii_lowercase[i].upper() for i in range(len(orig))})

    # Decode the message
    decoded_message = ''.join(substitution_dict.get(char, char) for char in message)

    return decoded_message

def main(input_file):
    try:
        # Read the content of the input file
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Decode the content
        decoded_content = decode_message(content)

        # Generate the output file name
        output_file = f"{input_file}.decoded"

        # Write the decoded content to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decoded_content)

        print(f"Decoded content has been saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decode.py <input_file>")
    else:
        main(sys.argv[1])
