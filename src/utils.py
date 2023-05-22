import csv

# Util for saving data in csv
def save_to_csv(data):
    with open("coindesk_news.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Название новости", "Ссылка на новость", "Дата новости"])
        writer.writerows(data)

