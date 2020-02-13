import csv
from random import randint

"""
GenrePicker needs a list of genres in its root directory called genres.csv.
It contains a function named random genre which returns a random genre from this list.
"""


class GenrePicker:
    def __init__(self):
        self.genres = []
        with open("./audio/genres.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                self.genres.append(row[0])
        self.number_of_genres = len(self.genres)

    def random_genre(self):
        return self.genres[randint(0, self.number_of_genres)]


genre_object = GenrePicker()
print(genre_object.random_genre())
