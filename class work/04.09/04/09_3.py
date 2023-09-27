import json
import csv

with open("films.json", mode="r") as f:
    obj = json.load(f)

# print(obj)
films = obj.get("response")
print(films)

# в формат CSV

# with open("films.csv", mode="w") as csv_file:
#     fieldnames = list(films[0].keys())
#     writter = csv.DictWriter(csv_file, fieldnames=fieldnames,
#                              lineterminator="\n")
#     writter.writeheader()
#     for film in films:
#         writter.writerow(film)

# в формат CSV 2 способ

 # with open("films2.csv", mode="w") as csv_file:
 #    fieldnames = list(films[0].keys())
 #    writer = csv.writer(csv_file, lineterminator="\n")
 #    writer.writerow(fieldnames)
 #    for film in films:
 #        films_values = film.values()
 #        print(films_values)
 #        writer.writerow(films_values)


 def add_films_to_csv(title, year, genre):
     with open("film2.csv", mode="a"), as f:
        csvwriter = csv.writer(f, lineterminator="\n")
        csvwriter.writerow([title, year, genere])

add_films_to_csv("terminator 4", 2007, "action")