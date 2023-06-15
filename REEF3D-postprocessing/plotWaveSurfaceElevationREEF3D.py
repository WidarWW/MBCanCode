# IBMcanCode https://github.com/WidarWW/MBCanCode
# Since 2023
# Developed by REEF3D Team (www.reef3d.com)
# Marine Civil Engineering Group (https://www.ntnu.edu/ibm/marine-civil-engineering)
# Department of Civil and Environmental Engineering 
# Norwegian University of Science and Technology 
# Trondheim, Norway 
###################################################################################################
# the purpose of this code is to plot wave surface elevation time series from REEF3D simulations
###################################################################################################

import numpy as np
import matplotlib.pyplot as plt

# %% plot wave surface elevation time series at defined wave gauges using using P 51 in ctrl.txt for REEF3D

n_gauge = 3
n_header = n_gauge + 7

model = 'FNPF' # choose between 'CFD', 'FNPF', 'SFLOW' and 'NHFLOW', check updates at https://github.com/REEF3D or https://reef3d.com/

fsf_t = np.loadtxt('./data/REEF3D_'+model+'_WSF/REEF3D-'+model+'-WSF-HG.dat', skiprows=n_header)

# if you have defined a theoretical wave gauge using P 50 in ctrl.txt for REEF3D
fsf_t_t = np.loadtxt('./data/REEF3D_'+model+'_WSF/REEF3D-'+model+'-WSF-HG-THEORY.dat', skiprows=n_header)

# %% plot the simulated wave surface elevation time series against the theoretical values at a given wave gauge and save them as png and eps figures

i_gauge = 1

fig=plt.figure(1,(9, 3))
plt.plot(fsf_t[:,0], fsf_t[:,i_gauge], 'r-', fsf_t_t[:,0], fsf_t_t[:,i_gauge], 'k--', linewidth=1.5)
plt.xlabel('t (s)')
plt.ylabel('$\eta$ (m)')
plt.legend(["REEF3D", "theory"])
plt.grid(True, linestyle='--', linewidth=0.5)
plt.savefig('./data/wave_surface_elevation_'+model+'.png', format='png', dpi=1000, bbox_inches='tight')
plt.savefig('./data/wave_surface_elevation_'+model+'.eps', format='eps', bbox_inches='tight')
plt.show()
