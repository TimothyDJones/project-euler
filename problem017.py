"""
Problem 17
https://projecteuler.net/problem=17

Number Letter Counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000(one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

ONES = ( "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine" )
TEENS = ( "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" )
TENS = ( "twenty", "thirty", "forty", "fifty", "sixty",
        "seventy", "eighty", "ninety", "hundred" )
SUFFIXES = ( "", "thousand", "million", "billion" )

def main():
    MAX_NUM = 1000
    words = list()

    print(convert_num_to_words(342))
    print(convert_num_to_words(115))
    print(convert_num_to_words(1000))
    print(convert_num_to_words(500))
    print(convert_num_to_words(45))
    print(convert_num_to_words(122))
    print(convert_num_to_words(110))
    print(convert_num_to_words(6))
    print(convert_num_to_words(14))
    

    for n in range(1, MAX_NUM + 1):
        num_word, num_word_len = convert_num_to_words(n)
        words.append([n, num_word, num_word_len])

    print(sum([w[2] for w in words]))

def convert_num_to_words(n: int):
    # Make into 4-digit string
    words = list()

    num = list(map(int, list(str(n).zfill(4))))
    thousands_digit = num[0]
    hundreds_digit = num[1]
    tens_digit = num[2]
    ones_digit = num[3]

    if thousands_digit > 0:
        words.append(ONES[thousands_digit])
        words.append("thousand")

    if hundreds_digit > 0:
        words.append(ONES[hundreds_digit])
        words.append("hundred")

    if tens_digit > 0:
        if hundreds_digit > 0:
            words.append("and")

        if tens_digit > 1:
            words.append(TENS[tens_digit - 2])
        elif tens_digit == 1:
            words.append(TEENS[ones_digit])
            
    if ones_digit > 0:
        if tens_digit == 0 and hundreds_digit > 0:
            words.append("and")
        
        if not tens_digit == 1:
            words.append(ONES[ones_digit])

    num_word = " ".join(words)
    num_word_len = len([l for l in list(num_word) if not l in [" "]])

    return (num_word, num_word_len)

if __name__ == "__main__":
    main()
