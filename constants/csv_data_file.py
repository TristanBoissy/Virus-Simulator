import csv

fieldnames = ["time", "not_infected", "infected", "immune"]

def setup_csv_data_file(not_infected, infected, immune):

    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    update_csv_file(0, not_infected, infected, immune)

def update_csv_file(time, not_infected, infected, immune):
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        info = {
            "time": time,
            "not_infected": not_infected,
            "infected": infected,
            "immune": immune
        }
        csv_writer.writerow(info)
