
# should return a dictionary
def letter_freq(txt):
    frequency_dict = {}

    for i, char in enumerate(txt):
        if char in frequency_dict:
            frequency_dict[char] += 1

        else:
            keypair = {char: 1}
            frequency_dict.update(keypair)

    # need to sort the list
    sorted_dict = sorted(frequency_dict.items())
    print("Sorted items: ", sorted_dict)

    return frequency_dict


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
