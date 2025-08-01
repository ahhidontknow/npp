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
    def __init__(self, material, size = np.array([]), material_enrichment = True):
        self.material = material.name
        # check if custom range is provided, if so use it
        if isinstance(material_enrichment, np.ndarray): 
            enrichment_range = material_enrichment
            self.enrichment = np.random.uniform(low = enrichment_range[0], high = enrichment_range[1])
        else: # else use range provided by material
            enrichment_range = material.range_rod_enrichment
            self.enrichment = np.random.uniform(low = enrichment_range[0], high = enrichment_range[1])

    def __repr__(self):
        desc = 'The material used in this rod is {name}. \n'.format(name = self.material)
        desc = desc + 'The enrichment in this rod is {enrichment}'.format(enrichment = self.enrichment)
        return (desc)