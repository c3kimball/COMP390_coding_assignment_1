class MeteorDataEntry:

    def __init__( self, name, id, nametype, recclass, mass_g, fall, year, reclat, reclong, GeoLocation, States, Counties):
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

    # Checks to see if a meteor is over 2,900,000g
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



