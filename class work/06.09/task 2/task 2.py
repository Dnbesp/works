# За допомогою модуля реквест за посиланням  ...  отиримати дані та записати їх в ссв файл
import csv
import requests
path = 'https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/people/people-100.csv'
response = requests.get(path)
text = response.text
with open('data.csv', mode="w", newline='') as file:
    file.write(text)

# напишіть функцію чар....
def change_csv_value(file_path, row_index, column, new_value):
    with open(file_path, mode='r+') as file:
        csv_file = csv.reader(file)
        lst_data = list(csv_file)
        lst_data[row_index][column] = new_value
        file.seek(0)
        csv_writer = csv.writer(file)
        csv_writer.writerows(lst_data)

change_csv_value("data.csv", row_index=2, column=2, new_value="xxxxxx")

