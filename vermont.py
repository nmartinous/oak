# Animals in Vermont simulation
# -----------------------------

'''
IMPORTS
'''

import random

'''
VARIABLES
'''

# Dictionaries to store objects and information
animal_id = 1
animal_catalogue = {}
kingdom_catalogue = {}
phylum_catalogue = {}
class_catalogue = {}
order_catalogue = {}
family_catalogue = {}
genus_catalogue = {}
species_catalogue = {}

'''
CLASSES
'''

# Animal Kingdom
class Animal:
    
    def __init__(self, commonName='N/A', k='Animalia', p='N/A', c='N/A', o='N/A', f='N/A', g='N/A', s='N/A', diet='N/A'):

        global animal_id
        global animal_catalogue
        global species_catalogue

        self._commonName = commonName
        self._kingdom = k
        self._phylum = p
        self._class = c
        self._order = o
        self._family = f
        self._genus = g
        self._species = s
        self._diet = diet
        self._id = animal_id
        self._conservation_status = 'Not Inputted'

        gender_value = random.randint(0,1)
        if gender_value == 0:
            gender = 'Male'
        else:
            gender = 'Female'
        self._gender = gender

        animal_catalogue.update({animal_id: self})
        animal_id += 1

        if (self._kingdom not in kingdom_catalogue):
            kingdom_catalogue.update({self._kingdom: 1})
        else:
            kingdom_catalogue[self._kingdom] += 1

        if (self._phylum not in phylum_catalogue):
            phylum_catalogue.update({self._phylum: 1})
        else:
            phylum_catalogue[self._phylum] += 1

        if (self._class not in class_catalogue):
            class_catalogue.update({self._class: 1})
        else:
            class_catalogue[self._class] += 1

        if (self._order not in order_catalogue):
            order_catalogue.update({self._order: 1})
        else:
            order_catalogue[self._order] += 1

        if (self._family not in family_catalogue):
            family_catalogue.update({self._family: 1})
        else:
            family_catalogue[self._family] += 1

        if (self._genus not in genus_catalogue):
            genus_catalogue.update({self._genus: 1})
        else:
            genus_catalogue[self._genus] += 1

        if (self._commonName not in species_catalogue):
            species_catalogue.update({self._commonName: 1})
        else:
            species_catalogue[self._commonName] += 1

    def get_common_name(self):
        return self._commonName
    
    def get_kingdom(self):
        return self._kingdom
    
    def get_phylum(self):
        return self._phylum
    
    def get_class(self):
        return self._class
    
    def get_order(self):
        return self._order
    
    def get_family(self):
        return self._family
    
    def get_genus(self):
        return self._genus
    
    def get_species(self):
        return self._species
    
    def get_diet(self):
        return self._diet

    def set_common_name(self, commonName):
        self._commonName = commonName

    def set_common_name(self, k):
        self._kingdom = k

    def set_common_name(self, p):
        self._phylum = p

    def set_common_name(self, c):
        self._class = c

    def set_common_name(self, o):
        self._order = o

    def set_common_name(self, f):
        self._family = f

    def set_common_name(self, g):
        self._genus = g

    def set_common_name(self, s):
        self._species = s

    def set_common_name(self, diet):
        self._diet = diet

    def del_common_name(self):
        del self._commonName
    
    def del_kingdom(self):
        del self._kingdom
    
    def del_phylum(self):
        del self._phylum
    
    def del_class(self):
        del self._class
    
    def del_order(self):
        del self._order
    
    def del_family(self):
        del self._family
    
    def del_genus(self):
        del self._genus
    
    def del_species(self):
        del self._species
    
    def del_diet(self):
        del self._diet

    def __repr__(self):
        return "\nSpecies Info\n------------\nCommon Name: {}\nKingdom: {}\nPhylum: {}\nClass: {}\nOrder: {}\nFamily: {}\nGenus: {}\nSpecies: {}\nDiet: {}\nConversation Status: {}\n\nIndividual Info\n---------------\nID: {}\nGender: {}\n".format(self._commonName, self._kingdom, self._phylum, self._class, self._order, self._family, self._genus, self._genus[0]+ ". " + self._species, self._diet, self._conservation_status, self._id, self._gender)

# Chordate Phylum
class Chordata(Animal):
    
    def __init__(self, commonName='N/A', k='Animalia', p='Chordata', c='N/A', o='N/A', f='N/A', g='N/A', s='N/A', diet='N/A'):
        super().__init__(commonName, k, p, c, o, f, g, s, diet)

# Mammal Class
class Mammal(Chordata):

    def __init__(self, commonName='N/A', k='Animalia', p='Chordata', c='Mammalia', o='N/A', f='N/A', g='N/A', s='N/A', diet='N/A'):
        super().__init__(commonName, k, p, c, o, f, g, s, diet)

# Carnivoran Order (Meat-eating Mammals)
class Carnivora(Mammal):

    def __init__(self, commonName='N/A', k='Animalia', p='Chordata', c='Mammalia', o='Carnivora', f='N/A', g='N/A', s='N/A', diet='N/A'):
        super().__init__(commonName, k, p, c, o, f, g, s, diet)

# Canidae Family (Dogs & Dog-like Carnivores)
class Canidae(Carnivora):

    def __init__(self, commonName='N/A', k='Animalia', p='Chordata', c='Mammalia', o='Carnivora', f='Canidae', g='N/A', s='N/A', diet='N/A'):
        super().__init__(commonName, k, p, c, o, f, g, s, diet)

# Urocyon Genus (Gray Fox and Island Fox)
class Urocyon(Canidae):

    def __init__(self, commonName='N/A', k='Animalia', p='Chordata', c='Mammalia', o='Carnivora', f='Canidae', g='Urocyon', s='N/A', diet='N/A'):
        super().__init__(commonName, k, p, c, o, f, g, s, diet)

# U.cinereoargenteus Species (Gray Fox)
class Gray_Fox(Urocyon):

    def __init__(self, commonName='Gray Fox', k='Animalia', p='Chordata', c='Mammalia', o='Carnivora', f='Canidae', g='Urocyon', s='cinereoargenteus', diet='Omnivore'):
        super().__init__(commonName, k, p, c, o, f, g, s, diet)
        self._conservation_status = 'Least Concern'

# Lagomorph Order (Rabbits, Hares, & Pikas)
class Lagomorpha(Mammal):

    def __init__(self, commonName='N/A', k='Animalia', p='Chordata', c='Mammalia', o='Lagomorpha', f='N/A', g='N/A', s='N/A', diet='N/A'):
        super().__init__(commonName, k, p, c, o, f, g, s, diet)

# Leporidae Family (Rabbits & Hares)
class Leporidae(Lagomorpha):

    def __init__(self, commonName='N/A', k='Animalia', p='Chordata', c='Mammalia', o='Lagomorpha', f='Leporidae', g='N/A', s='N/A', diet='N/A'):
        super().__init__(commonName, k, p, c, o, f, g, s, diet)

# Syvilagus Genus (Rabbits)
class Sylvilagus(Leporidae):

    def __init__(self, commonName='N/A', k='Animalia', p='Chordata', c='Mammalia', o='Lagomorpha', f='Leporidae', g='Syvilagus', s='N/A', diet='N/A'):
        super().__init__(commonName, k, p, c, o, f, g, s, diet)

# S.floridanus Species (Eastern Cottontail)
class Eastern_Cottontail(Sylvilagus):
    
    def __init__(self, commonName='Eastern Cottontail', k='Animalia', p='Chordata', c='Mammalia', o='Lagomorpha', f='Leporidae', g='Syvilagus', s='floridanus', diet='Herbivore'):
        super().__init__(commonName, k, p, c, o, f, g, s, diet)
        self._conservation_status = 'Least Concern'

'''
FUNCTIONS
'''

# Prints all living members of a level using a string as input for level and search_input
# i.e. level_print('kingdom', 'Animalia')
# Implement counter for members of level
def level_print(level, search_input):
    first = True
    count = 0
    match level:
            case 'Kingdom':
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_kingdom() == search_input):
                        count += 1
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_kingdom() == search_input):
                        if first:
                            print('There are {} living members in the {} {}\n'.format(count, search_input, level))
                            print("###########################################")
                            print(animal_catalogue[indvidual])
                            first = False
                        else:
                            print("###########################################")
                            print(animal_catalogue[indvidual])
            case 'Phylum':
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_phylum() == search_input):
                        count += 1
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_phylum() == search_input):
                        if first:
                            print('There are {} living members in the {} {}\n'.format(count, search_input, level))
                            print("###########################################")
                            print(animal_catalogue[indvidual])
                            first = False
                        else:
                            print("###########################################")
                            print(animal_catalogue[indvidual])
            case 'Class':
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_class() == search_input):
                        count += 1
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_class() == search_input):
                        if first:
                            print('There are {} living members in the {} {}\n'.format(count, search_input, level))
                            print("###########################################")
                            print(animal_catalogue[indvidual])
                            first = False
                        else:
                            print("###########################################")
                            print(animal_catalogue[indvidual])
            case 'Order':
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_order() == search_input):
                        count += 1
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_order() == search_input):
                        if first:
                            print('There are {} living members in the {} {}\n'.format(count, search_input, level))
                            print("###########################################")
                            print(animal_catalogue[indvidual])
                            first = False
                        else:
                            print("###########################################")
                            print(animal_catalogue[indvidual])
            case 'Family':
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_family() == search_input):
                        count += 1
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_family() == search_input):
                        if first:
                            print('There are {} living members in the {} {}\n'.format(count, search_input, level))
                            print("###########################################")
                            print(animal_catalogue[indvidual])
                            first = False
                        else:
                            print("###########################################")
                            print(animal_catalogue[indvidual])
            case 'Genus':
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_genus() == search_input):
                        count += 1
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_genus() == search_input):
                        if first:
                            print('There are {} living members in the {} {}\n'.format(count, search_input, level))
                            print("###########################################")
                            print(animal_catalogue[indvidual])
                            first = False
                        else:
                            print("###########################################")
                            print(animal_catalogue[indvidual])
            case 'Common Name':
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_common_name() == search_input):
                        count += 1
                for indvidual in animal_catalogue:
                    if (animal_catalogue[indvidual].get_common_name() == search_input):
                        if first:
                            print('There are {} living {} individuals\n'.format(count, search_input))
                            print("###########################################")
                            print(animal_catalogue[indvidual])
                            first = False
                        else:
                            print("###########################################")
                            print(animal_catalogue[indvidual])
    return count

'''
TEST CALLS
'''

# Test calls
print("")
eastern_cottontail = Eastern_Cottontail()
gray_fox = Gray_Fox()
eastern_cottontail = Eastern_Cottontail()
gray_fox = Gray_Fox()
eastern_cottontail = Eastern_Cottontail()
gray_fox = Gray_Fox()
S

# Add way to add new animals easily
# Add exception handling (use assertion errors to check that values are in cataloguesS)
# Add unit testing
# Add Canada Bluegrass as the first plantS