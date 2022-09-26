# Craig Kimball 9/26/22
# COMP390 Assignment 1

import meteor_data_class

if __name__ == '__main__':
    #  Reads in a data set of meteors found of Earth and prints a table of the ones that are over 2,900,000 grams and another table of the ones that fell after 2013

    #  This will be a list of every meteor
    all_meteors = []
    #  This will be the list of meteors that are over 2,000,000g and fell 2013 or later
    target_meteor_list = []

    with open("meteor_data.txt", "r") as f:
        while f.readline() != "":
            line = f.readline()
            line1 = line.replace("\n", "")
            line2 = line1.split('\t')


            print(line2)
