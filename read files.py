film_file = open('film.txt','r')
# r read,w write,a append,r+ read and write
print(film_file.readable())
print(film_file.read())
print(film_file.readline())
#readline last line
print(film_file.readlines())
#a list of lines
films = film_file.readlines()
for film in films:
    print(film)
film_file.close()