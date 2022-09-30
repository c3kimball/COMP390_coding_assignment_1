# Craig Kimball 9/30/22
# COMP390 Assignment 1

import meteor_data_class

#  Reads in a data set of meteors found on Earth and prints out 2 tables:
#       One for the meteors over 2,900,000g
#       Another for meteors that fell in 2013 or later
if __name__ == '__main__':

    #  List of meteors that are over 2,000,000g
    target_mass = []

    #  List of meteors that fell in 2013 or later
    target_year = []

    # A list of every meteor
    all_meteors = meteor_data_class.generate_meteors()

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
