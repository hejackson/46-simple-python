#!/usr/local/bin/python3


def max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a


def max_of_three(a, b, c):
    """
    Either a, b or c is max, or they're all equal
    """
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return a


def length_of_thing(thing):
    x = 0
    for item in thing:
        x += 1

    return x


def is_a_vowel(character):
    if character.lower() in 'aeiouy':
        return True
    else:
        return False


def translate(string):
    new_string = ''
    for c in string:
        if is_a_vowel(c):
            new_string += c
        elif c.isalpha():
            new_string += c + 'o' + c
        else:
            new_string += c

    return new_string


def sum(list):
    x = 0
    for item in list:
        x += item

    return x


def multiply(list):
    x = 1
    for item in list:
        x *= item

    return x


def reverse(string):
    return string[::-1]


def is_palindrome(string):
    if string == reverse(string):
        return True
    else:
        return False


def is_member(x, a):
    for item in a:
        if x == item:
            return True

    return False


def overlapping(a, b):
    for item in a:
        for other in b:
            if other == item:
                return True

    return False


def generate_n_chars(n, c):
    string = ''
    for x in range(n):
        string += c

    return string


def historgram(list):
    for x in list:
        print(generate_n_chars(x, '*'))


def max_in_list(list):
    if len(list) > 0:
        max = list[0]
    else:
        return None

    if len(list) > 1:
        for item in list[1:]:
            if item > max:
                max = item

    return max


def map_words_to_len(words):
    result = {}
    for item in words:
        try:
            result[len(item)].append(item)

        except KeyError:
            result[len(item)] = [item]

    return result


def find_longest_word(list):
    if len(list) > 0:
        max = len(list[0])

    else:
        return None

    if len(list) > 1:
        for word in list:
            if len(word) > max:
                max = len(word)

    return max


def filter_long_words(words, n):
    result = []
    for item in words:
        if len(item) > n:
            result.append(item)

    return result


def palindrome2(phrase):
    alpha_string = ''
    for c in phrase:
        if c.lower().isalpha():
            alpha_string += c.lower()

    return is_palindrome(alpha_string)


def pangram(phrase):
    # define list of lower case characters, taken from comment on
    # https://stackoverflow.com/questions/16060899/alphabet-range-python
    alphabet = set(map(chr, range(ord('a'), ord('z') + 1)))
    newset = set()
    for c in phrase:
        if c.isalpha():
            newset.add(c.lower())

    return alphabet == newset


def bottles_of_beer():
    for x in range(99, 0, -1):
        print('{} bottles of beer on the wall, {} bottles of beer.'
              .format(x, x))
        print('Take one down, pass it around, {} bottles of beer on the wall'
              .format(x - 1))
        print()


def translate2(phrase):
    """
    doesn't yet handle phrases like 'christmas!'
    """
    result_list = []
    eng_to_swed = {
        'merry': 'god',
        'christmas': 'jul',
        'and': 'och',
        'happy': 'gott',
        'new': 'nytt',
        'year': 'år'
    }

    for word in phrase.split():
        if word.lower() in eng_to_swed:
            result_list.append(eng_to_swed[word.lower()])

        else:
            result_list.append(word.lower())

    return ' '.join(result_list)


if __name__ == '__main__':
    pass