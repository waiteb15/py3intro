

movie_star  = "Tom Trotter"

print(movie_star)
print(movie_star.upper())
print(movie_star.lower())

#why does this return 12 when length is 10
print(movie_star.count(""))
print(len(movie_star))
print(movie_star[10])
print(movie_star.count('o'))
print(movie_star.count('Tom'))

print(type(movie_star))


print(movie_star.startswith('Tom'))
print(movie_star.endswith('Trotter'))

print(movie_star.replace('Tom','Scott'))

print(movie_star)



#strip commands get rid of whitepsace

x="xyxyxyxy"


word_string = 'spring/warf/blom/yubu'

words = word_string.split('/')

print(words[0])
print(len(words))