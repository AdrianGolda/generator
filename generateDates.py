import datetime
import csv


def getMonth(argument):
    switcher = {
        1: "Styczen",
        2: "Luty",
        3: "Marzen",
        4: "Kwiecien",
        5: "Maj",
        6: "Czerwiec",
        7: "Lipiec",
        8: "Sierpien",
        9: "Wrzesien",
        10: "Pazdziernik",
        11: "Listopad",
        12: "Grudzien",
    }
    return switcher[argument]


def getTimeOfYear(argument):
    switcher = {
        1: "zima",
        2: "zima",
        3: "zima",
        4: "wiosna",
        5: "wiosna",
        6: "wiosna",
        7: "lato",
        8: "lato",
        9: "lato",
        10: "jesien",
        11: "jesien",
        12: "jesien",
    }
    return switcher[argument]


if __name__ == "__main__":
    numdays = 100
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]
    date_objects = []
    for date in date_list:
        date_object = {}
        date_object["data"] = date.strftime("%Y-%m-%d")
        date_object["rok"] = date.year
        date_object["miesiac"] = getMonth(date.month)
        date_object["dzien"] = date.day
        date_object["czyDzienWolny"] = (
            "Dzien wolny" if date.weekday() >= 5 else "Dzien pracujacy"
        )
        date_object["PoraRoku"] = getTimeOfYear(date.month)
        date_object["weekend"] = "Weekend" if date.weekday() >= 5 else "Srodek tygodnia"
        date_object["RokAkademicki"] = (
            "Poza Rokiem akademickim" if date.month in [7, 8, 9] else "Rok akademicki"
        )
        date_object["RokSzkolny"] = (
            "Poza Rokiem szkolnym" if date.month in [7, 8] else "Rok szkolny"
        )
        date_object["Wakacje"] = "Wakacje" if date.month in [7, 8] else "Poza wakacjami"
        date_objects.append(date_object)
    with open("daty.csv", "w", newline="") as file:
        csv_writer = csv.writer(file, delimiter=",", quotechar=",")
        csv_writer.writerow(([str(e) for e in date_object.keys()]))
        for date in date_objects:
            csv_writer.writerow(date.values())

