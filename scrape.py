from bs4 import BeautifulSoup
import requests
import sys
import codecs

link = sys.argv[1]

source = requests.get(link).text
soup = BeautifulSoup(source, "lxml")
title = soup.title.text

filename = title.replace(" ","_").replace("|","").lower()
filename_with_extension = filename + ".txt"

with codecs.open(filename_with_extension, "w", encoding="utf8") as fh:
    fh.write(title + "\n\n")
    for ingredients in soup.find_all("div", class_="ingredients__text"):
        fh.write(ingredients.text + "\n")

    fh.write("\n")
    counter = 1 
    for steps in soup.find_all("li", class_="step"):
        step = "%i . %s" % (counter, steps.text)
        fh.write(step + "\n\n")
        
        counter += 1

    fh.close()