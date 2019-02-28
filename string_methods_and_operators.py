#!/usr/bin/env python

movie_star = "Tommy Trotter"

print(movie_star)
print(movie_star.upper())
print(movie_star.count('t'))
print(movie_star.count('Tom'))
print(len(movie_star))
print(type(movie_star))
print(movie_star.count('T') + movie_star.count('t'))
print(movie_star.lower().count('t'))

print(movie_star.startswith('Tom'))
print(movie_star.startswith('Brad'))


print(movie_star.replace('Tom', 'Brad'))
print(movie_star.replace('Tom', ''))

s = "      All my exes live in Texas       "
print("|" + s.lstrip() + '|')
print("|" + s.rstrip() + '|')
print("|" + s.strip() + '|')
print()


s = "xyxxyyxxxyyyxyxyxyxAll my exes live in Texasxyxyxyxyyyyyy"
print("|" + s.lstrip('xy') + '|')
print("|" + s.rstrip('xy') + '|')
print("|" + s.strip('xy') + '|')
print()

word_string = 'spink warf    blom   yuvu'
words = word_string.split()

print(words)

word_string = 'spink/warf/blom/yuvu'
words = word_string.split('/')
print(words)
print(words[0], words[0][0])

