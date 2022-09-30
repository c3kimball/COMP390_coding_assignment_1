#  Craig Kimball 9/20/2022

#  Reads in meteor_data.txt and generates a cleaned list of all meteors
def generate_meteors():
    all_meteors = []
    with open("meteor_data.txt", "r") as f:
        read_all_meteors = f.readlines()

    for i in range(len(read_all_meteors)):
        line1 = read_all_meteors[i].replace("\n", "")
        line2 = line1.split('\t')

        try:
            new_meteor = MeteorDataEntry(line2[0], line2[1], line2[2], line2[3], line2[4], line2[5], line2[6],
                                         line2[7], line2[8], line2[9], line2[10], line2[11])
            all_meteors.append(new_meteor)


        except:
            print("Defective data entry found\n")

    return all_meteors


class MeteorDataEntry:

    def __init__(self, name, id, nametype, recclass, mass_g, fall, year, reclat, reclong, GeoLocation, States,
                 Counties):
        self.name = name
        self.id = id
        self.nametype = nametype
        self.recclass = recclass
        self.mass_g = mass_g
        self.fall = fall
        self.year = year
        self.reclat = reclat
        self.reclong = reclong
        self.GeoLocation = GeoLocation
        self.States = States
        self.Counties = Counties

    #  Generates a cleaned list of all meteors from meteor_data.txt

    def check_mass(meteor):
        #  An error occurs when trying to cast an empty string into a float, so this first line is necessary
        if meteor.mass_g != '':
            if float(meteor.mass_g) > 2900000:
                return True
        else:
            return False

    #  Checks if the meteor fell in 2013 or later
    def check_year(meteor):
        #  An exact copy of check_mass, but with year instead of mass_g
        if meteor.year != '':
            if float(meteor.year) > 2012:
                return True
        else:
            return False

    #  Neatly prints out a table of each meteor over 2,900,000g
    def print_mass(meteors):
        name_label = "NAME"
        mass_label = "MASS (g)"
        print(f"{name_label:<24}{mass_label:<20}")
        print("======================================")
        for element in meteors:
            name_label = element.name
            mass_label = element.mass_g
            print(f"{name_label:<24}{mass_label:<20}")
        print()

    #  Neatly prints out a table of each meteor that fell in 2013 or later
    def print_year(meteors):
        name_label = "NAME"
        year_label = "YEAR"
        print(f"{name_label:<24}{year_label:<20}")
        print("======================================")
        for element in meteors:
            name_label = element.name
            year_label = element.year
            print(f"{name_label:<24}{year_label:<20}")
        print()
