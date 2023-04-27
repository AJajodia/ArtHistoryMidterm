# this file is part of a larger project that helped me study for my art history midterm
# the other files for this project are located at github.com/AJajodia/ArtHistoryMidterm

# import pandas, random, PIL, and psutil
import pandas as pd
import random
from PIL import Image
import psutil

# create class Question, which has attributes for each piece of data needed for answers as well as the category chosen
class Question:
    def __init__(self, category=random.choice(["name", "artist", "medium", "location", "country", "period"])):
        # initializes Question and assigns to each variable, as well as initializes a game with 0 questions answered
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
        # start
        self.play(category)

    def play(self, category):
        # create a lookup table for each category
        categories = {"name": 0, "artist": 1, "medium": 2, "location": 3, "country": 4, "period": 5}
        self.category = categories[category]
        # gives the file for specific review (in this case, only European works
        filename = 'europeReview.csv'
        # read the csv as a DataFrame
        file = pd.read_csv(filename, keep_default_na=False)
        # find a random row (work)
        piece = file.iloc[random.randint(0, file.shape[0] - 1), :]
        # if the category is empty (ex. piece has no attribution), find a new work
        while piece[self.category] == "":
            piece = file.iloc[random.randint(0, file.shape[0] - 1), :]
        # assign variables to the correct piece
        self.name = piece[0]
        self.artist = piece[1]
        self.medium = piece[2]
        self.location = piece[3]
        self.country = piece[4]
        self.period = piece[5]

        # open the image in a new tab
        im = Image.open(r"/Users/anu/PycharmProjects/ArtHistoryMidterm/photos/" + self.name)
        im.show()
        # close PIL process but keep the window open
        im.close()
        
        # ask question
        if input("What is the " + category + " of this work? ") == piece[self.category]:
            # update counters
            self.correct += 1
            self.total += 1
            print("You got it")
        else:
            # update counters
            self.total += 1
            print("Nope")
            
        print("Here are other details")
        # show details with method
        self.show()
        print()
        # show score
        print("Score: " + str(self.correct/self.total * 100) + "%")
        print()

        # if player inputs y, keep playing
        if input("Do you want to keep playing? (y/n) ") == "y":
            for i in range(40):
                print("")
            # terminate Preview, thus closing the image window
            for proc in psutil.process_iter():
                if proc.name() == "Preview":
                    proc.terminate()
            # play again
            self.play(category)
        else:
            # close image
            im.close()
            # terminate Preview
            for proc in psutil.process_iter():
                if proc.name() == "Preview":
                    proc.terminate()
    # show method (called when printing Question)
    def show(self):
        # prints basic info for eahc work
        print("Name:", self.name)
        print("Artist:", self.artist)
        print("Medium:", self.medium)
        print("Location:", self.location)
        print("Country:", self.country)
        print("Period:", self.period)
