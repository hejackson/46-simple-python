#!/usr/local/bin/python3

import re
import functools
import os
import time
import random
import requests
import itertools
import sys
import bs4


def max_new(a, b):
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


def char_freq(string):
    freq = {}
    for c in string:
        try:
            freq[c] += 1

        except KeyError:
            freq[c] = 1

    return freq


def rot13(phrase):
    cipher = {
        'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't',
        'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a',
        'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h',
        'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O',
        'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V',
        'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C',
        'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J',
        'X': 'K', 'Y': 'L', 'Z': 'M'
    }

    decode = ''

    for c in phrase:
        if c.isalpha():
            decode += cipher[c]
        else:
            decode += c

    return decode


def correct(phrase):
    a = re.sub('\.', ' ', phrase)
    b = re.sub(' +', ' ', a)
    return b


def endswitch(word):
    if word[-1].lower() == 'y':
        return word[:-1] + 'ies'

    elif word[-1].lower() in ['o', 's', 'x', 'z']:
        return word + 'es'

    elif word[-2:].lower() in ['ch', 'sh']:
        return word + 'es'

    else:
        return word + 's'


def make_ing_form(word):
    if word.lower()[-2:] == 'ie':
        return word[:-2] + 'ying'

    elif word.lower()[-1] == 'e':
        if word.lower() != 'be' and word.lower()[-2:] != 'ee':
            return word[:-1] + 'ing'
        else:
            return word + 'ing'

    elif word.lower()[-3] not in 'aeiouy':
        if word.lower()[-2] in 'aeiouy':
            if word.lower()[-1] not in 'aeiouy':
                return word + word[-1] + 'ing'

    else:
        return word + 'ing'


def max_in_list2(list):
    # stolen from http://www.python-course.eu/python3_lambda.php
    result = functools.reduce(lambda a, b: a if (a > b) else b, list)
    return result


def mapit1(words):
    list = {}
    for word in words:
        try:
            list[len(word)].append(word)
        except KeyError:
            list[len(word)] = [word]

    return list


def mapit2(words):
    return list(map(len, words))


def mapit3(words):
    return [len(x) for x in words]


def find_longest_word2(words):
    return max([len(x) for x in words])


def filter_long_words2(words, n):
    return [x for x in words if len(x) > n]


def palindrome3(file):
    with open(file, 'r') as infile:
        for text in infile:
            text = text.strip()
            if palindrome2(text):
                print(text)

    print()


def semordnilap(file):
    # create set to keep first word of all semos found
    # create and populate set for all words in file
    # walk through each word and add first word of all semos to semos list
    semos = set()
    words = set()
    with open(file, 'r') as infile:
        for text in infile:
            text = text.strip()
            words.add(text)

    for word in words:
        # is this word already in semos set?
        if word not in semos and word[::-1] not in semos:

            # is this word and it's reverse in the list of words?
            if word[::-1] in words:
                semos.add(word)

    for word in semos:
        print('{} {}'.format(word, word[::-1]))


def char_freq_table(file):
    letters = {}
    with open(file, 'r') as infile:
        for line in infile:
            line = line.strip()
            for c in line:
                if c.isalpha():
                    try:
                        letters[c] += 1
                    except KeyError:
                        letters[c] = 1

    return letters


def speak_ICAO(phrase):
    d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
         'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india',
         'j': 'juliett', 'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november',
         'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra',
         't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey',
         'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'}

    a = .2
    b = .5

    for c in phrase:
        if c.isalpha():
            c = c.lower()
            os.system('say ' + d[c])
            time.sleep(a)
        else:
            time.sleep(b)


def hapax(file):
    words = {}
    with open(file, 'r') as infile:
        for line in infile:
            line = line.strip()
            for word in line.split():
                word = re.sub('[\W_]', '', word)
                try:
                    words[word.lower()] += 1
                except KeyError:
                    words[word.lower()] = 1

    for word in sorted(words):
        if words[word] == 1:
            print(word)


def number_lines(file, file2):
    line_number = 1
    with open(file, 'r') as infile:
        with open(file2, 'w') as outfile:
            for line in infile:
                outfile.write('{}: {}'.format(line_number, line))
                line_number += 1


def average_word_length(file):
    number_of_words = 0
    length_of_all_words = 0
    with open(file, 'r') as infile:
        for line in infile:
            line = line.strip()
            for word in line.split():
                word = re.sub('[\W_]', '', word)
                number_of_words += 1
                length_of_all_words += len(word)

    return length_of_all_words / number_of_words


def guess_number():
    name = input('Hello! What is your name? ')
    print('Well, {}, I am thinking of a number between 1 and 20.'.format(name))
    number = random.randint(1, 20)
    guess = 999
    number_of_guesses = 0

    while guess != number and number_of_guesses < 10:
        print('Take a guess.')
        guess = int(input())
        number_of_guesses += 1
        if guess > number:
            print('Your guess is too high.')
        elif guess < number:
            print('Your guess is too low.')
        else:
            print('Good job, {}!  You guessed my number in {} guesses!'.
                  format(name, number_of_guesses))
            break


def anagram(words):
    word = words[random.randint(0, len(words) - 1)]
    scramble = ''.join(random.sample(word, len(word)))

    print('Word anagram: {}'.format(scramble))

    guess = ''
    number_of_guesses = 0
    while guess != word and number_of_guesses < 10:
        print('Guess the word!')
        guess = input()
        number_of_guesses += 1

        if guess == word:
            print('Correct!')
            break


def lingo(word):
    guess = ''
    while guess != word:
        guess = input('Please enter your {} character guess: '
                      .format(len(word)))
        result = ''
        for x in range(len(guess)):
            if guess[x].lower() == word[x].lower():
                result += '[' + guess[x] + ']'
            elif guess[x].lower() in word.lower():
                result += '(' + guess[x] + ')'
            else:
                result += guess[x]

        print('Clue: {}'.format(result))


def sentence_splitter(text):
    # taken from:
    # https://github.com/R4meau/46-simple-python-exercises/blob/master/exercises/ex42.py

    # Add newline to sentences ending in period, but not if Mr., Mrs., Dr.
    # new = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', text)
    pattern = re.compile(r"""
                         (?<!Mr)        # ignore Mr.
                         (?<!Mrs)       # ignore Mrs.
                         (?<!Dr)        # ignore Dr.
                         \.             # match a period, follwed by
                         \s+            # one or more spaces, followed by
                         ([A-Z])        # A CAPITAL letter, saving letter
                         """, re.VERBOSE)

    new = re.sub(pattern, r'.\n\1', text)

    # replace ! or ? with same, followed by newline
    # -- this next line didn't work, it didn't put the ! or ? back
    # new = re.sub(r'([!\?])\s+', '\1\n', new)
    new = re.sub(r'!\s+', '!\n', new)
    new = re.sub(r'\?\s+', '?\n', new)

    return new


def anagram2():
    url = 'http://www.puzzlers.org/pub/wordlists/unixdict.txt'
    response = requests.get(url)
    spinner = itertools.cycle(['-', '/', '|', '\\'])

    results = set()
    for word in response.text.split():
        if len(word) < 7:
            print('{}...'.format(word))
            for x in itertools.permutations(word, len(word)):
                sys.stdout.write(next(spinner))
                sys.stdout.flush()
                y = ''.join(x)
                # add newlines to either end of sample 'word' to match
                # word boundaries present in the response.text output from
                # the URL.  For example: '\nzombie\n'
                z = '\n' + y + '\n'
                if y != word and z in response.text:
                    results.add(word + ' : ' + y)

                sys.stdout.write('\b')

    print('\n\nDone...\n\n')
    return results


def nested():
    text = ''
    length = 2 * random.randint(1, 5)
    for x in range(length):
        r = random.randint(0, 1)
        if r:
            text += '['
        else:
            text += ']'

    open = 0
    for c in text:
        if open >= 0:
            if c == '[':
                open += 1
            else:
                open -= 1
                if open < 0:
                    break

    if open != 0:
        print('{} NOT OK'.format(text))
    else:
        print('{} OK'.format(text))


def spinit(x):
    spinner = itertools.cycle(['-', '/', '|', '\\'])

    for i in range(x):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        sys.stdout.write('\b')


def pokemon():
    url = "https://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon#List"
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    table = soup.findChildren('table')
    rows = table[0].findChildren('tr')

    names = []

    for row in rows[1:]:
        names.append(row.find('a', href=True, title=True).string)

    names = """audino bagon baltoy banette bidoof braviary bronzor carracosta
    charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute
    gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff
    kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp
    magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath
    poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye
    scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink
    starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle
    whismur wingull yamask""".split()

    # names = ['dog', 'goldfish', 'gecko', 'hipster', 'ostritch']
    # names = 'goldfish dog hippopotamus snake elephant tick gecko \
    #          kangaroo ocelot'.split()

    print(names)
    perms = itertools.permutations(names, len(names))
    total = len(names) ** len(names)
    print('There are {0:,} permutations of names.'
          .format(total))
    input('Press [enter | return] to begin...')

    longest = []


    def invalid_word(word, names):
        for name in names:
            if name[0].lower() == word[-1].lower():
                return True

        return False


    def check_last_and_next(current_word, next_word):
        if current_word[-1].lower() == next_word[0].lower():
            return True
        else:
            return False


    def longest_set(permutation):
        current_list = []
        current_word = permutation[0]
        current_list.append(current_word)

        if current_word in bad_words:
            return current_list

        for word in permutation[1:]:
            if current_word in bad_words:
                return current_list

            if check_last_and_next(current_word, word):
                current_list.append(word)
                current_word = word

            else:
                return current_list

        return current_list

    bad_words = []
    for name in names:
        if invalid_word(name, names) is False:
            bad_words.append(name)

    for p in perms:
        if p[0] in bad_words:
            pass
        else:
            print(longest)
            current_set = longest_set(p)
            if len(current_set) > len(longest):
                longest = current_set

    print('LONGEST: {} {}'.format(len(longest),longest))


if __name__ == '__main__':
    pass
