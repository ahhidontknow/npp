# it is called construction_site as its meant for building individual components used.

###############################################################################
# import of basic 
###############################################################################

# needed to get lib from other directory
import sys
import os

# basic math & animations
import numpy as np
import matplotlib as plt

# basic concepts
import components as cmp


# extend path to construction site in order to 
sys.path.insert(0, os.getcwd() + '/constructions_site')
import materials as mat


###############################################################################
# build you npp here :)
###############################################################################


fissile_material = mat.u_235

rod1 = cmp.fuel_rod(fissile_material)

print(rod1)

#neut1 = cmp.neutron()