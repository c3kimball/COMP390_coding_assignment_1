# Craig Kimball 9/26/22
# COMP390 Assignment 1

import meteor_data_class

if __name__ == '__main__':
    #  Reads in a data set of meteors found of Earth and prints a table of the ones that are over 2,900,000 grams and another table of the ones that fell after 2013

    #  This will be a list of every meteor
    all_meteors = []
    #  This will be the list of meteors that are over 2,000,000g and fell 2013 or later
    target_meteor_list = []

    # Reads in meteor_data.txt line by line and cleans it in order to make a new MeteorDataEntry object
    with open("meteor_data.txt", "r") as f:
        while f.readline() != "":
            line = f.readline()
            line1 = line.replace("\n", "")
            line2 = line1.split('\t')

            #  Having severe problems with this line
            #  This is where the code breaks when adding self as a parameter in MeteorDaraEntry
            #  When self was a parameter it wasn't able to find the last parameter for some reason
            all_meteors.append(
                meteor_data_class.MeteorDataEntry(line2[0], line2[1], line2[2], line2[3], line2[4], line2[5],
                                                  line2[6], line2[7], line2[8], line2[9], line2[10], line2[11]))

    #  It's as bad as I thought, I am only reading in the bottom half o th meteor list
    #  It complains that the file size is too large, so that probably is the issue, but I have no idea how to fix it
    for i in range(len(all_meteors)):
        print(i)
