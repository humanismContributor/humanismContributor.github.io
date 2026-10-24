import json
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    canton_info = []
    with open("guests_data.json") as f:
        guest_book = json.load(f)
        # Creates a dictionary of cantons
        canton_count = {}
        high_value = {}
        profitable = {}
        underperforming = {}
        hv_percent = {}
        for guest in guest_book:
            canton = guest["Canton"]
            value = guest["Visits per Year"] * (guest["Average Room Revenue"] + guest["Average Ancillary Revenue"])
            per_canton(canton_count, canton)
            if value >= 1000:
                per_canton(high_value, canton)
            if value < 1000 and value > 600:
                per_canton(profitable, canton)
            if value < 600:
                per_canton(underperforming, canton)
    find_percent(canton_count, high_value, hv_percent)
    for canton in canton_count:
        print(
            "In", canton + ":\n" +
            "Number of Guests:", canton_count.get(canton, 0),
            "\nHigh Value Guests:", high_value.get(canton, 0),
            "\nHigh Value Percentage:", hv_percent.get(canton, 0),
            "\nProfitable Guests:", profitable.get(canton, 0),
            "\nUnderperforming Guests:", underperforming.get(canton, 0), "\n\n"
        )
    with open("Canton Info.txt", "w") as f:
        for canton in canton_count:
            f.write("In " + canton + ": " + "\n")
            f.write("Number of Guests: " + str(canton_count.get(canton, 0)) + "\n")
            f.write("High Value Guests: " + str(high_value.get(canton, 0)) + "\n")
            f.write("High Value Percentage: " + str(hv_percent.get(canton, 0)) + "\n")
            f.write("Profitable Guests: " + str(profitable.get(canton, 0)) + "\n")
            f.write("Underperforming Guests: " + str(underperforming.get(canton, 0)) + "\n\n")
    make_bar_plot(canton_count, "Number of Guests")
    make_bar_plot(high_value, "High Value Guests")
    make_bar_plot(hv_percent, "High Value Guest Percentage")
    make_bar_plot(profitable, "Profitable Guests")
    make_bar_plot(underperforming, "Underperforming Guests")

    print('-----------------------------------------------------------------\n')
    # Guest look-up
    guest_directory = input("Would you like to see all guests? (Y/N?): ").capitalize()
    print()
    while True:
        if guest_directory == 'Y':
            print("To see each guest per Canton, select: A\n" +
                "To see each High Value guest, select: B\n" +
                "To see each Profitable guest, select: C\n" +
                "To see each Underperforming guest, select: D\n" +
                "To see each guest according to number of visits, select: E\n" +
                "To see each guest according to the average number of nights, select: F\n"
            )
            choice = input("Please enter one of the choices mentioned or press 'Enter' to exit: ").capitalize()
            if choice == "":
                print("\n...\nGoodbye\n")
                exit()
            print()
            # Write a search option via Cantons
            # Search by last names
            by_canton = input("Please choose a canton or press 'Enter' to exit: ")
            if by_canton == "":
                print("\n...\nGoodbye\n")
                exit()
            by_canton = by_canton[0].capitalize() + by_canton[1:]
            print()
            if choice == "E":
                req_visits = int(input("How many visits? "))
                print()
            elif choice == "F":
                req_nights = int(input("How many nights? "))
                print()
            for guest in guest_book:
                canton_choice = guest["Canton"]
                value = guest["Visits per Year"]*(guest["Average Room Revenue"] + guest["Average Ancillary Revenue"])
                num_visits = guest["Visits per Year"]
                num_nights = guest["Average Number of Nights"]
                if choice == "A":
                    if canton_choice == by_canton:
                        print("First and Last Name:", guest["First Name"], guest["Last Name"], "\n" +
                            "Guest ID:", guest["Guest ID"],"\n" +
                            "Canton:", guest["Canton"],"\n" +
                            "Vists per Year:", guest["Visits per Year"],"\n"+
                            "Average Room Revenue:", guest["Average Room Revenue"],"\n" +
                            "Average Number of Nights:", guest["Average Number of Nights"],"\n" +
                            "Average Ancillary Revenue:", guest["Average Ancillary Revenue"],"\n\n"
                        )
                if choice == "B":
                    if canton_choice == by_canton and value >= 1000:
                        print("First and Last Name:", guest["First Name"], guest["Last Name"], "\n" +
                            "Guest ID:", guest["Guest ID"],"\n" +
                            "Canton:", guest["Canton"],"\n" +
                            "Vists per Year:", guest["Visits per Year"],"\n"+
                            "Average Room Revenue:", guest["Average Room Revenue"],"\n" +
                            "Average Number of Nights:", guest["Average Number of Nights"],"\n" +
                            "Average Ancillary Revenue:", guest["Average Ancillary Revenue"],"\n\n"
                        )
                if choice == "C":
                    if canton_choice == by_canton and value < 1000 and value > 600:
                        print("First and Last Name:", guest["First Name"], guest["Last Name"], "\n" +
                            "Guest ID:", guest["Guest ID"],"\n" +
                            "Canton:", guest["Canton"],"\n" +
                            "Vists per Year:", guest["Visits per Year"],"\n"+
                            "Average Room Revenue:", guest["Average Room Revenue"],"\n" +
                            "Average Number of Nights:", guest["Average Number of Nights"],"\n" +
                            "Average Ancillary Revenue:", guest["Average Ancillary Revenue"],"\n\n"
                        )
                if choice == "D":
                    if canton_choice == by_canton and value < 600:
                        print("First and Last Name:", guest["First Name"], guest["Last Name"], "\n" +
                            "Guest ID:", guest["Guest ID"],"\n" +
                            "Canton:", guest["Canton"],"\n" +
                            "Vists per Year:", guest["Visits per Year"],"\n"+
                            "Average Room Revenue:", guest["Average Room Revenue"],"\n" +
                            "Average Number of Nights:", guest["Average Number of Nights"],"\n" +
                            "Average Ancillary Revenue:", guest["Average Ancillary Revenue"],"\n\n"
                        )
                if choice == "E":
                    if canton_choice == by_canton and num_visits == req_visits:
                        print("First and Last Name:", guest["First Name"], guest["Last Name"], "\n" +
                            "Guest ID:", guest["Guest ID"],"\n" +
                            "Canton:", guest["Canton"],"\n" +
                            "Vists per Year:", guest["Visits per Year"],"\n"+
                            "Average Room Revenue:", guest["Average Room Revenue"],"\n" +
                            "Average Number of Nights:", guest["Average Number of Nights"],"\n" +
                            "Average Ancillary Revenue:", guest["Average Ancillary Revenue"],"\n\n"
                        )
                if choice == "F":
                    if canton_choice == by_canton and num_nights == req_nights:
                        print("First and Last Name:", guest["First Name"], guest["Last Name"], "\n" +
                            "Guest ID:", guest["Guest ID"],"\n" +
                            "Canton:", guest["Canton"],"\n" +
                            "Vists per Year:", guest["Visits per Year"],"\n"+
                            "Average Room Revenue:", guest["Average Room Revenue"],"\n" +
                            "Average Number of Nights:", guest["Average Number of Nights"],"\n" +
                            "Average Ancillary Revenue:", guest["Average Ancillary Revenue"],"\n\n"
                        )
            print('-----------------------------------------------------------------\n')
        elif guest_directory == 'N':
            print("\n...\nGoodbye\n")
            exit()
        else:
            guest_directory = input("Would you like to see all guests? (Y/N?): ").capitalize()
            print()
    print()
    print("\n...\nGoodbye\n")


def find_percent(total, actual, new_dict):
    for count in total:
        new_dict[count] = round(100 * actual.get(count, 0) / total[count])


def per_canton(canton_list, canton):
    if canton not in canton_list:
        canton_list[canton] = 1
    else:
        canton_list[canton] += 1
    return canton_list


def make_bar_plot(canton_list, title):
    """
    Turns a dictionary (where values are numbers) into a bar plot.
    Labels gives the order of the bars! Uses a package called seaborn
    for making graphs.
    """
    fig, ax = plt.subplots(figsize=(30, 10))
    # turn the counts into a list
    counts = []
    # loop over the labels, in order
    for label in canton_list:
        counts.append(canton_list[label])
    # format the data in the way that seaborn wants
    data = {
        'x': list(canton_list.keys()),
        'y': counts
    }
    plot = sns.barplot(x = 'x',y = 'y', data= data)
    #plt.pie(counts, labels=canton_list.keys())
    plt.setp(plot.get_xticklabels(), rotation=30)
    plt.savefig(title + " per Canton.png")
    return plt


if __name__ == '__main__':
    main()
