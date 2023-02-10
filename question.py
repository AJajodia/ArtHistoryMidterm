import pandas as pd
import random
from PIL import Image
import psutil


class Question:
    def __init__(self, category=random.choice(["name", "artist", "medium", "location", "country", "period"])):
        self.correct = 0
        self.total = 0
        self.category = ""
        self.name = "piece[0]"
        self.artist = "piece[1]"
        self.medium = "piece[2]"
        self.location = "piece[3]"
        self.country = "piece[4]"
        self.period = "piece[5]"
        self.random = False
        self.play(category)

    def play(self, category):
        categories = {"name": 0, "artist": 1, "medium": 2, "location": 3, "country": 4, "period": 5}
        self.category = categories[category]
        filename = 'europeReview.csv'
        file = pd.read_csv(filename, keep_default_na=False)
        piece = file.iloc[random.randint(0, file.shape[0] - 1), :]
        while piece[self.category] == "":
            piece = file.iloc[random.randint(0, file.shape[0] - 1), :]
        self.name = piece[0]
        self.artist = piece[1]
        self.medium = piece[2]
        self.location = piece[3]
        self.country = piece[4]
        self.period = piece[5]

        im = Image.open(r"/Users/anu/PycharmProjects/ArtHistoryMidterm/photos/" + self.name)
        im.show()
        im.close()
        if input("What is the " + category + " of this work? ") == piece[self.category]:
            self.correct += 1
            self.total += 1
            print("You got it")
        else:
            self.total += 1
            print("Nope")
        print("Here are other details")
        self.show()
        print()
        print("Score: " + str(self.correct/self.total * 100) + "%")
        print()

        if input("Do you want to keep playing? (y/n) ") == "y":
            for i in range(40):
                print("")
            for proc in psutil.process_iter():
                if proc.name() == "Preview":
                    proc.terminate()
            self.play(category)
        else:
            im.close()
            for proc in psutil.process_iter():
                if proc.name() == "Preview":
                    proc.terminate()

    def show(self):
        print("Name:", self.name)
        print("Artist:", self.artist)
        print("Medium:", self.medium)
        print("Location:", self.location)
        print("Country:", self.country)
        print("Period:", self.period)
