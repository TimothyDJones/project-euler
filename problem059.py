"""
Problem 59
https://projecteuler.net/problem=59

XOR Decryption
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using 0059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

"""
from itertools import product, cycle, islice
from string import ascii_lowercase
from pprint import pprint


def main():
    sum_ascii_vals_plaintext = 0

    with open("/usr/share/dict/words") as f:
        dict_words = [word.strip() for word in f.readlines()]
    # pprint(dict_words[:20])

    with open("0059_cipher.txt", "r") as f:
        ciphertext = [int(c) for c in f.readline().split(",")]
    # pprint(ciphertext)

    candidate_passwords = ["".join(c) for c in product(ascii_lowercase, repeat=3)]
    # pprint(candidate_passwords[:20])
    # print(len(candidate_passwords))

    for password in candidate_passwords:
        plaintext = "".join(decipher(ciphertext=ciphertext, password=password))
        # If more than 10% of characters are "spaces", then we have
        # reasonable expectation that plaintext may contain valid text.
        if (float(plaintext.count(" ")) / float(len(plaintext))) > 0.1:
            print(plaintext)
            word_count, valid_word_count = 0, 0
            for word in plaintext.split(" "):
                word_count += 1
                if word in dict_words:
                    valid_word_count += 1

            # If more than 50% of words are valid words from dictionary,
            # then we have reasonable evidence that this is the valid
            # plaintext.
            if (float(valid_word_count) / float(word_count)) > 0.5:
                sum_ascii_vals_plaintext = sum([ord(c) for c in list(plaintext)])
                break

    print(sum_ascii_vals_plaintext)


def decipher(ciphertext: list, password: str):
    key = islice(cycle(password), len(ciphertext))

    return [chr(c ^ ord(k)) for c, k in zip(ciphertext, key)]

if __name__ == "__main__":
    main()
