# 1.hello_name

# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


# hello_name('Bob') → 'Hello Bob!'
# hello_name('Alice') → 'Hello Alice!'
# hello_name('X') → 'Hello X!'

def hello_name(name):
    return 'Hello ' + name + '!'


# 2.make_abba


# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye"
# returns "HiByeByeHi".


# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'

def make_abba(a, b):
    return a + b + b + a


# 3.make_tags
#
# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag
# makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags
# around the word, e.g. "<i>Yay</i>".
#
#
# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'

def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'


# 4.make_out_word


# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of
# the out string, e.g. "<<word>>".
#
#
# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]', 'word') → '[[word]]'


def make_out_word(out, word):
    return out[0:2] + word + out[2:]


# 5.extra_end


# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length
# will be at least 2.
#
#
# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'


def extra_end(str):
    return str[-2:] * 3


# 6.first_two


# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is
# shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string
# "".
#
#
# first_two('Hello') → 'He'
# first_two('abcdefg') → 'ab'
# first_two('ab') → 'ab'


def first_two(str):
    if len(str) >= 2:
        return str[:2]
    else:
        return str


# 7.first_half

# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
#
#
# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'

def first_half(str):
    if len(str) % 2 == 0:
        frist_half = len(str) / 2
        return str[:frist_half]


# 8.without_end


# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will
# be at least 2.
#
#
# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'

def without_end(str):
    return str[1:-1]


# 9.combo_string


# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and
# the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
#
#
# combo_string('Hello', 'hi') → 'hiHellohi'
# combo_string('hi', 'Hello') → 'hiHellohi'
# combo_string('aaa', 'b') → 'baaab'


def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a


# 10.non_start


# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least
# length 1.
#
#
# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'


def non_start(a, b):
    return a[1:] + b[1:]


# 11.left2

# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length
# will be at least 2.
#
#
# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'


def left2(str):
    first_two = str[:2]
    return str[2:] + first_two


# 12.double_char


# Given a string, return a string where for every char in the original, there are two chars.
#
#
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
    result = ''
    for i in str:
        result += i * 2
    return result


# 13.count_hi

# Return the number of times that the string "hi" appears anywhere in the given string.
#
#
# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
    return str.count('hi')


# def count_hi(str):
#   sum = 0
#   ## Loop to length-1 and access index i and i+1
#   ## in the loop.
#   for i in range(len(str)-1):
#     if str[i:i+2] == 'hi':
#       sum = sum + 1
#   return sum


# 14.cat_dog


# Return True if the string "cat" and "dog" appear the same number of times in the given string.
#
#
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
    cat = str.count('cat')
    dog = str.count('dog')

    if cat == dog:
        return True
    return False


# Using for loop
# def cat_dog(str):
#     sum_cat = 0
#     sum_dog = 0

#     for i in range(len(str) -1):
#         if str[i:i+3] == 'cat':
#             sum_cat += 1
#     for i in range(len(str) -1):
#         if str[i:i+3] == 'dog':
#             sum_dog += 1
#     if sum_cat == sum_dog:
#         return True
#     return False


# 15.count_code


# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any
# letter for the 'd', so "cope" and "cooe" count.
#
#
# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if str[i] == 'c' and str[i + 1] == 'o' and str[i + 3] == 'e':
            count += 1
    return count


# 16.end_other


# Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note:
# s.lower() returns the lowercase version of a string.
#
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
    str_a = a.lower()
    str_b = b.lower()
    return str_a.endswith(str_b) or str_b.endswith(str_a)


# 17.xyz_there

# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period
# (.). So "xxyz" counts but "x.xyz" does not.
#
#
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
    # if '.xyz' in str:
    #   return False
    # elif '.xyz' and 'xzy':
    #   return True

    # elif 'xyz' in str:
    #   return True
    # return False
    return str.count('.xyz') != str.count('xyz')
