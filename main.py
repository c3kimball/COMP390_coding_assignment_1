# Craig Kimball 9/26/22
# COMP390 Assignment 1

import meteor_data_class

if __name__ == '__main__':
    #  Reads in a data set of meteors found of Earth and prints a table of the ones that are over 2,900,000 grams and another table of the ones that fell after 2013

    #  List of every meteor
    all_meteors = []

    #  List of meteors that are over 2,000,000g
    target_mass = []

    #  List of meteors that fell in 2013 or later
    target_year = []

    # Reads in meteor_data.txt line by line and cleans it in order to make a new MeteorDataEntry object
    with open("meteor_data.txt", "r") as f:
        while f.readline() != "":
            line = f.readline()
            line1 = line.replace("\n", "")
            line2 = line1.split('\t')

            all_meteors.append(
                meteor_data_class.MeteorDataEntry(line2[0], line2[1], line2[2], line2[3], line2[4], line2[5],
                                                  line2[6], line2[7], line2[8], line2[9], line2[10], line2[11]))

    #  Sorting through all_meteors to look for target meteors
    for element in all_meteors:
        if meteor_data_class.MeteorDataEntry.check_mass(element):
            target_mass.append(element)

        if meteor_data_class.MeteorDataEntry.check_year(element):
            target_year.append(element)

    # Printing target_mass meteors
    meteor_data_class.MeteorDataEntry.print_mass(target_mass)
    # Printing target_year meteors
    meteor_data_class.MeteorDataEntry.print_year(target_year)
