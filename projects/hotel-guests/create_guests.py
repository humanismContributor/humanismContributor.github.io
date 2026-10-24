import json
import random


def main():
    write_data()


def write_data():
    name_list = []
    for data in range(1, 240):
        first_name = first_name_gen()
        last_name = last_name_gen()
        id_num = pad(data, 3)
        canton = canton_gen()
        visits = visit_gen()
        avg_room_rev = room_rev_gen(visits)
        avg_anc_rev = anc_rev_gen(visits)
        data = {
            "First Name": first_name,
            "Last Name": last_name,
            "Guest ID": id_num,
            "Canton": canton,
            "Visits per Year": visits,
            "Average Room Revenue": avg_room_rev[0],
            "Average Number of Nights": avg_room_rev[1],
            "Average Ancillary Revenue": avg_anc_rev
        }
        name_list.append(data.copy())
    with open("guests_data.json", "w") as f:
        json.dump(name_list, f, indent=4)


def anc_rev_gen(visits):
    total = 0
    for num in range(visits):
        anc_rev = random.randint(40, 200)
        total += anc_rev
    avg = int(total / visits)
    return avg


def room_rev_gen(visits):
    total = 0
    total_nights = 0
    rate_1 = random.randint(1, 3)
    nights_1 = random.randint(1, 3)
    if rate_1 == 1:
        rate_1 = 240
    elif rate_1 == 2:
        rate_1 = 270
    elif rate_1 == 3:
        rate_1 = 330
    total += (rate_1 * nights_1)
    total_nights += nights_1
    if visits > 1:
        for num in range(visits - 1):
            remaining_rates = random.randint(1, 10)
            if remaining_rates == 1 or remaining_rates == 2:
                remaining_rates = 270
            elif remaining_rates == 3:
                remaining_rates = 330
            else:
                remaining_rates = rate_1
            nights = random.randint(1, 9)
            if nights == 1:
                nights = 1
            elif nights == 2:
                nights = 2
            elif nights == 3:
                nights = 3
            else:
                nights = nights_1
            total += (remaining_rates * nights)
            total_nights += nights
    avg = int(total / visits), int(total_nights / visits)
    return avg


def visit_gen():
    visit = random.randint(1, 3)
    return visit


def canton_gen():
    canton = random.randint(1, 34)
    if canton == 1 or canton == 27:
        canton = 'Zurich'
    elif canton == 2 or canton == 28 or canton == 30:
        canton = 'Bern'
    elif canton == 3 or canton == 29 or canton == 31:
        canton = 'Luzern'
    elif canton == 4:
        canton = 'Uri'
    elif canton == 5:
        canton = 'Schwyz'
    elif canton == 6 or canton == 32:
        canton = 'Obwalden'
    elif canton == 7:
        canton = 'Nidwalden'
    elif canton == 8:
        canton = 'Glarus'
    elif canton == 9:
        canton = 'Zug'
    elif canton == 10:
        canton = 'Fribourg'
    elif canton == 11 or canton == 33:
        canton = 'Solothurn'
    elif canton == 12:
        canton = 'Basel-Stadt'
    elif canton == 13:
        canton = 'Basel-Landschaft'
    elif canton == 14:
        canton = 'Schaffhausen'
    elif canton == 15:
        canton = 'Appenzell Ausserrhoden'
    elif canton == 16:
        canton = 'Appenzell Innerhoden'
    elif canton == 17:
        canton = 'St. Gallen'
    elif canton == 18:
        canton = 'Graubunden'
    elif canton == 19 or canton == 34:
        canton = 'Aargau'
    elif canton == 20:
        canton = 'Thurgau'
    elif canton == 21:
        canton = 'Ticino'
    elif canton == 22:
        canton = 'Vaud'
    elif canton == 23:
        canton = 'Valais'
    elif canton == 24:
        canton = 'Neuchatel'
    elif canton == 25:
        canton = 'Geneve'
    elif canton == 26:
        canton = 'Jura'
    return canton


def pad(data, limit):
    data_string = str(data)
    while len(data_string) < limit:
        data_string = '0' + data_string
    return int(data_string)


def last_name_gen():
    last_name = random.randint(1, 30)
    if last_name == 1:
        last_name = 'Mueller'
    elif last_name == 2:
        last_name = 'Gerber'
    elif last_name == 3:
        last_name = 'Jeger'
    elif last_name == 4:
        last_name = 'Aubry'
    elif last_name == 5:
        last_name = 'Winzeler'
    elif last_name == 6:
        last_name = 'Alder'
    elif last_name == 7:
        last_name = 'Inauen'
    elif last_name == 8:
        last_name = 'Iten'
    elif last_name == 9:
        last_name = 'Jeanneret'
    elif last_name == 10:
        last_name = 'Aebischer'
    elif last_name == 11:
        last_name = 'Chatgny'
    elif last_name == 12:
        last_name = 'Rochat'
    elif last_name == 13:
        last_name = 'Favre'
    elif last_name == 14:
        last_name = 'Gaillard'
    elif last_name == 15:
        last_name = 'Aymon'
    elif last_name == 16:
        last_name = 'Mathieu'
    elif last_name == 17:
        last_name = 'Seematter'
    elif last_name == 18:
        last_name = 'Burch'
    elif last_name == 19:
        last_name = 'Keller'
    elif last_name == 20:
        last_name = 'Odermatt'
    elif last_name == 21:
        last_name = 'Werlen'
    elif last_name == 22:
        last_name = 'Amacker'
    elif last_name == 23:
        last_name = 'Kaelin'
    elif last_name == 24:
        last_name = 'Buergler'
    elif last_name == 25:
        last_name = 'Arnold'
    elif last_name == 26:
        last_name = 'Caminada'
    elif last_name == 27:
        last_name = 'Schmid'
    elif last_name == 28:
        last_name = 'Bernasconi'
    elif last_name == 29:
        last_name = 'Hefti'
    elif last_name == 30:
        last_name = 'Meier'
    return last_name


def first_name_gen():
    first_name = random.randint(1, 30)
    if first_name == 1:
        first_name = 'Daniel'
    elif first_name == 2:
        first_name = 'Maria'
    elif first_name == 3:
        first_name = 'Thomas'
    elif first_name == 4:
        first_name = 'Sandra'
    elif first_name == 5:
        first_name = 'Andreas'
    elif first_name == 6:
        first_name = 'Claudia'
    elif first_name == 7:
        first_name = 'Markus'
    elif first_name == 8:
        first_name = 'Monika'
    elif first_name == 9:
        first_name = 'Martin'
    elif first_name == 10:
        first_name = 'Karin'
    elif first_name == 11:
        first_name = 'Michael'
    elif first_name == 12:
        first_name = 'Andrea'
    elif first_name == 13:
        first_name = 'Christian'
    elif first_name == 14:
        first_name = 'Nicole'
    elif first_name == 15:
        first_name = 'Stefan'
    elif first_name == 16:
        first_name = 'Daniela'
    elif first_name == 17:
        first_name = 'Marco'
    elif first_name == 18:
        first_name = 'Manuela'
    elif first_name == 19:
        first_name = 'Patrick'
    elif first_name == 20:
        first_name = 'Barbara'
    elif first_name == 21:
        first_name = 'David'
    elif first_name == 22:
        first_name = 'Sarah'
    elif first_name == 23:
        first_name = 'Simon'
    elif first_name == 24:
        first_name = 'Sabrina'
    elif first_name == 25:
        first_name = 'Kevin'
    elif first_name == 26:
        first_name = 'Laura'
    elif first_name == 27:
        first_name = 'Pascal'
    elif first_name == 28:
        first_name = 'Melanie'
    elif first_name == 29:
        first_name = 'Fabian'
    elif first_name == 30:
        first_name = 'Jessica'
    return first_name


if __name__ == "__main__":
	main()
