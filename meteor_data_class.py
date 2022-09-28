class MeteorDataEntry:

     # adding self to the parameters breaks it, leaving it like this for now
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
        if meteor.mass_g != '' and meteor.year != '':
            if float(meteor.mass_g) > 2900000:
                return True
        else:
            return False



