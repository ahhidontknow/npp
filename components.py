###############################################################################
# imports if needed
###############################################################################

import numpy as np

###############################################################################
# core components of a npp
###############################################################################

class neutron:
    def __init__(pos):
        self.pos = pos
        

class fissile_material:
    def __init__(self, name, range_rod_enrichment):
        self.name = name
        self.range_rod_enrichment = range_rod_enrichment
        
    def __repr__(self):
        desc = 'This fissile material is called {name}. \n'.format(name = self.name)
        desc = desc + 'It has a typical enrichment from {range_rod_enrichment[0]} to {range_rod_enrichment[1]}'.format(range_rod_enrichment = self. range_rod_enrichment)
        return desc

    # def induce_fission():
        

class non_fissile_material:
    def __init__(self, name):
        self.name = name


class moderator:
    def __init__(self, name):
        self.name = name

    def __repr__(self, name):
        desc = 'This moderator is {name}'.format(name = self.name)
        return desc

   # def reduce_neutron_speed:


class fuel_rod:
    def __init__(self, material, enrichtment = True):
        self.material = material.name
        self.enrichment = enrichtment

    def __repr__(self):
        desc = "The material is {name}, the enrichment {enrichment}".format(name = self.material, enrichment = self.enrichment)
        return (desc)