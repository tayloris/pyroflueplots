# To activate Python enviroment $  C:\PythonEnv\pythonEnv\Scripts\activate.bat

import pandas as pd
import os
import sys
# adding source folder to the system path
try:
    import ToolboxGF as Tbx
except:
    print('ToolboxGF not found')
    print('Please ToolboxGF in to PYTHONPATH by typing:')
    #print('export PYTHONPATH = $PYTHONPATH; C:\pathToDirectory\pyroflueplots\src')
    print("$ set PYTHONPATH=%PYTHONPATH%;C:\pathToDirectory\pyroflueplots\src")
    quit()
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib.colors as pltc
import numpy as np
all_colors = [k for k,v in pltc.cnames.items()]


script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, "..", ".."))
extensionPDF = '.pdf'
extensionPNG = '.png'

# User input directories

DATAFILE      = os.path.join(parent_dir,'data', 'raw_data_withoutDIV_0_without_outliers.csv')
OUPUTPLOT     = os.path.join(parent_dir,'plots', 'BarChartsMatrix')

# =============================================================

df = pd.read_csv(DATAFILE, header=1, nrows=23)

#print(df)
 
# Tuve que separar la liste de variables porque hay grupos que no tienen "stdev"

yaxisToPlot_8 = ['Em_fac_CO2_g_kg-1char_by_gas_comp',  'Em_fac_CO2_g_kg-1char_by_gas_comp_stdev', 'Em_fac_CH4_g_kg-1char_by_gas_comp', 'Em_fac_CH4_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_CO_g_kg-1char_by_gas_comp', 'Em_fac_CO_g_kg-1char_by_gas_comp_stdev', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_TSP_g_kg-1char_by_gas_comp', 'Em_fac_TSP_g_kg-1char_by_gas_comp_stdev', 'Em_fac_PIC_g_kg-1char_by_gas_comp', 'Em_fac_PIC_g_kg-1char_by_gas_comp_stdev']

yaxisToPlot_15 = ['Em_fac_NO_g_kg-1char_by_gas_comp', 'Em_fac_NO_g_kg-1char_by_gas_comp_stdev', 'Em_fac_NO2_g_kg-1char_by_gas_comp', 'Em_fac_NO2_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_NOx_gNO2_kg-1char_by_gas_comp', 'Em_fac_NOx_gNO2_kg-1char_by_gas_comp_stdev', 'Em_fac_N2O_g_kg-1char_by_gas_comp', 'Em_fac_N2O_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_NH3_g_kg-1char_by_gas_comp', 'Em_fac_NH3_g_kg-1char_by_gas_comp_stdev', 'Em_fac_HCN_g_kg-1char_by_gas_comp', 'Em_fac_HCN_g_kg-1char_by_gas_comp_stdev' ]

yaxisToPlot_16 = ['Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 
                  'Em_fac_HCl_g_kg-1dryfeedstock_by_gas_comp', 'Em_fac_HCl_g_kg-1dryfeedstock_by_gas_comp_stdev', 'Em_fac_SO2_g_kg-1dryfeedstock_by_gas_comp', 'Em_fac_SO2_g_kg-1dryfeedstock_by_gas_comp_stdev',
                  'Em_fac_HCl_g_kg-1char_by_gas_comp', 'Em_fac_HCl_g_kg-1char_by_gas_comp_stdev', 'Em_fac_SO2_g_kg-1char_by_gas_comp', 'Em_fac_SO2_g_kg-1char_by_gas_comp_stdev']

yaxisToPlot_10 = ['Em_fac_CO2_g_kg-1char_by_gas_comp_normalized_by_fuel_addition',  'Em_fac_CO2_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_CH4_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_CH4_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_CO_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_CO_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_TSP_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_TSP_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_PIC_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_PIC_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev']

yaxisToPlot_11 = ['Em_fac_NO_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NO_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_NO2_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NO2_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_NOx_gNO2_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NOx_gNO2_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_N2O_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_N2O_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_NH3_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NH3_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_HCN_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_HCN_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev' ]

yaxisToPlot_12 = ['Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev', 
                  'Em_fac_HCl_g_kg-1dryfeedstock_by_gas_comp', 'Em_fac_HCl_g_kg-1dryfeedstock_by_gas_comp_stdev', 'Em_fac_SO2_g_kg-1dryfeedstock_by_gas_comp', 'Em_fac_SO2_g_kg-1dryfeedstock_by_gas_comp_stdev',
                  'Em_fac_HCl_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_HCl_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_SO2_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_SO2_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev']


yaxisToPlot_13 = ['Em_fac_CO2_g_kg-1char_by_gas_comp_normalized', 'Em_fac_CO2_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_CO_g_kg-1char_by_gas_comp_normalized_', 'Em_fac_CO_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_TSP_g_kg-1char_by_gas_comp_normalized', 'Em_fac_TSP_g_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_PIC_g_kg-1char_by_gas_comp', 'Em_fac_PIC_g_kg-1char_by_gas_comp_stdev', 'Em_fac_CH4_g_kg-1char_by_gas_comp', 'Em_fac_CH4_g_kg-1char_by_gas_comp_stdev', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp_stdev']

yaxisToPlot_14 = ['Em_fac_NOx_gNO2_kg-1char_by_gas_comp', 'Em_fac_NOx_gNO2_kg-1char_by_gas_comp_stdev', 'Em_fac_N2O_g_kg-1char_by_gas_comp', 'Em_fac_N2O_g_kg-1char_by_gas_comp_stdev', 'Em_fac_NH3_g_kg-1char_by_gas_comp', 'Em_fac_NH3_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_NO_g_kg-1char_by_gas_comp', 'Em_fac_NO_g_kg-1char_by_gas_comp_stdev', 'Em_fac_NO2_g_kg-1char_by_gas_comp', 'Em_fac_NO2_g_kg-1char_by_gas_comp_stdev', 'Em_fac_HCN_g_kg-1char', 'Em_fac_HCN_g_kg-1char_by_gas_comp_stdev']

yaxisToPlot_9 = ['Em_fac_NOx_gNO2_kg-1char_by_gas_comp', 'Em_fac_NOx_gNO2_kg-1char_stdev', 'Em_fac_SO2_g_kg-1char_by_gas_comp', 'Em_fac_SO2_g_kg-1char_stdev', 'Em_fac_HCl_g_kg-1char_by_gas_comp', 'Em_fac_HCl_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp_stdev']

yaxisToPlot_2 = ['Em_fac_Naphtalene_particle_µg_kg-1char', 'Em_fac_Naphtalene_gas_µg_kg-1char', 'Em_fac_Naphtalene_tot_µg_kg-1char', 'Em_fac_Acenaphthylene_particle_µg_kg-1char',
               'Em_fac_Acenaphthylene_gas_µg_kg-1char', 'Em_fac_Acenaphthylene_tot_µg_kg-1char', 'Em_fac_Acenaphthene_particle_µg_kg-1char', 'Em_fac_Acenaphthene_gas_µg_kg-1char',
               'Em_fac_Acenaphthene_tot_µg_kg-1char', 'Em_fac_Fluorene_particle_µg_kg-1char', 'Em_fac_Fluorene_Gas_µg_kg-1char', 'Em_fac_Fluorene_Tot_µg_kg-1char',
               'Em_fac_Phenanthrene_particle_µg_kg-1char', 'Em_fac_Phenanthrene_gas_µg_kg-1char', 'Em_fac_Phenanthrene_tot_µg_kg-1char', 'Em_fac_Anthracene_particle_µg_kg-1char',
               'Em_fac_Anthracene_gas_µg_kg-1char', 'Em_fac_Anthracene_tot_µg_kg-1char', 'Em_fac_Fluoranthene_particle_µg_kg-1char', 'Em_fac_Fluoranthene_gas_µg_kg-1char',
               'Em_fac_Fluoranthene_tot_µg_kg-1char', 'Em_fac_Pyrene_particle_µg_kg-1char', 'Em_fac_Pyrene_gas_µg_kg-1char', 'Em_fac_Pyrene_tot_µg_kg-1char',
               'Em_fac_Benz(a)anthracene_particle_µg_kg-1char', 'Em_fac_Benz(a)anthracene_gas_µg_kg-1char', 'Em_fac_Benz(a)anthracene_tot_µg_kg-1char',
               'Em_fac_Chrysene_particle_µg_kg-1char', 'Em_fac_Chrysene_gas_µg_kg-1char', 'Em_fac_Chrysene_tot_µg_kg-1char', 'Em_fac_Benzo(b)fluoranthene_particle_µg_kg-1char',
               'Em_fac_Benzo(b)fluoranthene_gas_µg_kg-1char', 'Em_fac_Benzo(b)fluoranthene_tot_µg_kg-1char', 'Em_fac_Benzo(k)fluoranthene_particle_µg_kg-1char',
               'Em_fac_Benzo(k)fluoranthene_gas_µg_kg-1char', 'Em_fac_Benzo(k)fluoranthene_tot_µg_kg-1char', 'Em_fac_Benzo(a)pyrene_particle_µg_kg-1char',
               'Em_fac_Benzo(a)pyrene_gas_µg_kg-1char', 'Em_fac_Benzo(a)pyrene_tot_µg_kg-1char', 'Em_fac_Indeno(1,2,3-cd)pyrene_particle_µg_kg-1char',
               'Em_fac_Indeno(1,2,3-cd)pyrene_gas_µg_kg-1char', 'Em_fac_Indeno(1,2,3-cd)pyrene_tot_µg_kg-1char', 'Em_fac_Benzo(ghi)perylene_particle_µg_kg-1char',
               'Em_fac_Benzo(ghi)perylene_gas_µg_kg-1char', 'Em_fac_Benzo(ghi)perylene_tot_µg_kg-1char', 'Em_fac_Dibenz(ah)anthracene_particle_µg_kg-1char',
               'Em_fac_Dibenz(ah)anthracene_gas_µg_kg-1char', 'Em_fac_Dibenz(ah)anthracene_tot_µg_kg-1char', 'Em_fac_ΣPAH-16_particle_µg_kg-1char',
               'Em_fac_ΣPAH-16_gas_µg_kg-1char', 'Em_fac_ΣPAH-16_tot_µg_kg-1char']

yaxisToPlot_3 = ['Em_fac_CO2_g_kg-1feedstock', 'Em_fac_CO2_g_kg-1feedstock_stdev',
               'Em_fac_CO_g_kg-1feedstock', 'Em_fac_CO_g_kg-1feedstock_stdev', 'Em_fac_CH4_g_kg-1feedstock', 'Em_fac_CH4_g_kg-1feedstock_stdev',
               'Em_fac_NMVOC_g_kg-1feedstock', 'Em_fac_NMVOC_g_kg-1feedstock_stdev', 'Em_fac_TSP_g_kg-1feedstock', 'Em_fac_TSP_g_kg-1feedstock_stdev',
               'Em_fac_PIC_g_kg-1feedstock', 'Em_fac_PIC_g_kg-1feedstock_stdev', 'Em_fac_SO2_g_kg-1feedstock', 'Em_fac_SO2_g_kg-1feedstock_stdev',
               'Em_fac_NO_g_kg-1feedstock', 'Em_fac_NO_g_kg-1feedstock_stdev', 'Em_fac_NO2_g_kg-1feedstock', 'Em_fac_NO2_g_kg-1feedstock_stdev',
               'Em_fac_N2O_g_kg-1feedstock', 'Em_fac_N2O_g_kg-1feedstock_stdev', 'Em_fac_NH3_g_kg-1feedstock', 'Em_fac_NH3_g_kg-1feedstock_stdev',
               'Em_fac_HCN_g_kg-1feedstock', 'Em_fac_HCN_g_kg-1feedstock_stdev', 'Em_fac_HCl_g_kg-1feedstock', 'Em_fac_HCl_g_kg-1feedstock_stdev', 
               'Em_fac_NOx_gNO2_kg-1feedstock', 'Em_fac_NOx_gNO2_kg-1feedstock_stdev']

yaxisToPlot_4 = [ 'Em_fac_Naphtalene_particle_µg_kg-1feedstock', 'Em_fac_Naphtalene_gas_µg_kg-1feedstock',
               'Em_fac_Naphtalene_tot_µg_kg-1feedstock', 'Em_fac_Acenaphthylene_particle_µg_kg-1feedstock', 'Em_fac_Acenaphthylene_gas_µg_kg-1feedstock',
               'Em_fac_Acenaphthylene_tot_µg_kg-1feedstock', 'Em_fac_Acenaphthene_particle_µg_kg-1feedstock', 'Em_fac_Acenaphthene_gas_µg_kg-1feedstock', 
               'Em_fac_Acenaphthene_tot_µg_kg-1feedstock', 'Em_fac_Fluorene_particle_µg_kg-1feedstock', 'Em_fac_Fluorene_Gas_µg_kg-1feedstock',
               'Em_fac_Fluorene_Tot_µg_kg-1feedstock', 'Em_fac_Phenanthrene_particle_µg_kg-1feedstock', 'Em_fac_Phenanthrene_gas_µg_kg-1feedstock',
               'Em_fac_Phenanthrene_tot_µg_kg-1feedstock', 'Em_fac_Anthracene_particle_µg_kg-1feedstock', 'Em_fac_Anthracene_gas_µg_kg-1feedstock',
               'Em_fac_Anthracene_tot_µg_kg-1feedstock', 'Em_fac_Fluoranthene_particle_µg_kg-1feedstock', 'Em_fac_Fluoranthene_gas_µg_kg-1feedstock',
               'Em_fac_Fluoranthene_tot_µg_kg-1feedstock', 'Em_fac_Pyrene_particle_µg_kg-1feedstock', 'Em_fac_Pyrene_gas_µg_kg-1feedstock',
               'Em_fac_Pyrene_tot_µg_kg-1feedstock', 'Em_fac_Benz(a)anthracene_particle_µg_kg-1feedstock', 'Em_fac_Benz(a)anthracene_gas_µg_kg-1feedstock',
               'Em_fac_Benz(a)anthracene_tot_µg_kg-1feedstock', 'Em_fac_Chrysene_particle_µg_kg-1feedstock', 'Em_fac_Chrysene_gas_µg_kg-1feedstock', 'Em_fac_Chrysene_tot_µg_kg-1feedstock', 'Em_fac_Benzo(b)fluoranthene_particle_µg_kg-1feedstock', 'Em_fac_Benzo(b)fluoranthene_gas_µg_kg-1feedstock', 'Em_fac_Benzo(b)fluoranthene_tot_µg_kg-1feedstock', 'Em_fac_Benzo(k)fluoranthene_particle_µg_kg-1feedstock', 'Em_fac_Benzo(k)fluoranthene_gas_µg_kg-1feedstock', 'Em_fac_Benzo(k)fluoranthene_tot_µg_kg-1feedstock', 'Em_fac_Benzo(a)pyrene_particle_µg_kg-1feedstock', 'Em_fac_Benzo(a)pyrene_gas_µg_kg-1feedstock', 'Em_fac_Benzo(a)pyrene_tot_µg_kg-1feedstock', 'Em_fac_Indeno(1,2,3-cd)pyrene_particle_µg_kg-1feedstock', 'Em_fac_Indeno(1,2,3-cd)pyrene_gas_µg_kg-1feedstock', 'Em_fac_Indeno(1,2,3-cd)pyrene_tot_µg_kg-1feedstock', 'Em_fac_Benzo(ghi)perylene_particle_µg_kg-1feedstock', 'Em_fac_Benzo(ghi)perylene_gas_µg_kg-1feedstock', 'Em_fac_Benzo(ghi)perylene_tot_µg_kg-1feedstock', 'Em_fac_Dibenz(ah)anthracene_particle_µg_kg-1feedstock', 'Em_fac_Dibenz(ah)anthracene_gas_µg_kg-1feedstock', 'Em_fac_Dibenz(ah)anthracene_tot_µg_kg-1feedstock', 'Em_fac_ΣPAH-16_particle_µg_kg-1feedstock', 'Em_fac_ΣPAH-16_gas_µg_kg-1feedstock', 'Em_fac_ΣPAH-16_tot_µg_kg-1feedstock', 'Tot_gas_exhaust_m3_kg-1char', 'Tot_gas_exhaust_m3_kg-1feedstock']

yaxisToPlot_5=['Em_fac_CO2_g_kg-1dry_ashfree_char', 'Em_fac_CO2_g_kg-1dry_ashfree_char_stdev', 'Em_fac_CO_g_kg-1dry_ashfree_char', 'Em_fac_CO_g_kg-1dry_ashfree_char_stdev',
               'Em_fac_CH4_g_kg-1dry_ashfree_char', 'Em_fac_CH4_g_kg-1dry_ashfree_char_stdev', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char_stdev',
               'Em_fac_TSP_g_kg-1dry_ashfree_char', 'Em_fac_TSP_g_kg-1dry_ashfree_char_stdev', 'Em_fac_PIC_g_kg-1dry_ashfree_char', 'Em_fac_PIC_g_kg-1dry_ashfree_char_stdev',
               'Em_fac_SO2_g_kg-1dry_ashfree_char', 'Em_fac_SO2_g_kg-1dry_ashfree_char_stdev', 'Em_fac_NO_g_kg-1dry_ashfree_char', 'Em_fac_NO_g_kg-1dry_ashfree_char_stdev',
               'Em_fac_NO2_g_kg-1dry_ashfree_char', 'Em_fac_NO2_g_kg-1dry_ashfree_char_stdev', 'Em_fac_N2O_g_kg-1dry_ashfree_char', 'Em_fac_N2O_g_kg-1dry_ashfree_char_stdev',
               'Em_fac_NH3_g_kg-1dry_ashfree_char', 'Em_fac_NH3_g_kg-1dry_ashfree_char_stdev', 'Em_fac_HCN_g_kg-1dry_ashfree_char', 'Em_fac_HCN_g_kg-1dry_ashfree_char_stdev',
               'Em_fac_HCl_g_kg-1dry_ashfree_char', 'Em_fac_HCl_g_kg-1dry_ashfree_char_stdev', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_char', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_stdev']

yaxisToPlot_6=['Em_fac_Naphtalene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Naphtalene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Naphtalene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Acenaphthylene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Acenaphthylene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Acenaphthylene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Acenaphthene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Acenaphthene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Acenaphthene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Fluorene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Fluorene_Gas_µg_kg-1dry_ashfree_char', 'Em_fac_Fluorene_Tot_µg_kg-1dry_ashfree_char', 'Em_fac_Phenanthrene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Phenanthrene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Phenanthrene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Anthracene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Anthracene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Anthracene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Fluoranthene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Fluoranthene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Fluoranthene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Pyrene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Pyrene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Pyrene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Benz(a)anthracene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Benz(a)anthracene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Benz(a)anthracene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Chrysene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Chrysene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Chrysene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Benzo(b)fluoranthene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Benzo(b)fluoranthene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Benzo(b)fluoranthene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Benzo(k)fluoranthene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Benzo(k)fluoranthene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Benzo(k)fluoranthene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Benzo(a)pyrene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Benzo(a)pyrene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Benzo(a)pyrene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Indeno(1,2,3-cd)pyrene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Indeno(1,2,3-cd)pyrene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Indeno(1,2,3-cd)pyrene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Benzo(ghi)perylene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Benzo(ghi)perylene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Benzo(ghi)perylene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_Dibenz(ah)anthracene_particle_µg_kg-1dry_ashfree_char', 'Em_fac_Dibenz(ah)anthracene_gas_µg_kg-1dry_ashfree_char', 'Em_fac_Dibenz(ah)anthracene_tot_µg_kg-1dry_ashfree_char', 'Em_fac_ΣPAH-16_particle_µg_kg-1dry_ashfree_char', 'Em_fac_ΣPAH-16_gas_µg_kg-1dry_ashfree_char', 
               'Em_fac_ΣPAH-16_tot_µg_kg-1dry_ashfree_char', 'Em_fac_CO2_g_kg-1dry_ashfree_feedstock', 'Em_fac_CO2_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_CO_g_kg-1dry_ashfree_feedstock', 'Em_fac_CO_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_CH4_g_kg-1dry_ashfree_feedstock', 'Em_fac_CH4_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_NMVOC_g_kg-1dry_ashfree_feedstock', 'Em_fac_NMVOC_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_TSP_g_kg-1dry_ashfree_feedstock', 'Em_fac_TSP_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_PIC_g_kg-1dry_ashfree_feedstock', 'Em_fac_PIC_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_SO2_g_kg-1dry_ashfree_feedstock', 'Em_fac_SO2_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_NO_g_kg-1dry_ashfree_feedstock', 'Em_fac_NO_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_NO2_g_kg-1dry_ashfree_feedstock', 'Em_fac_NO2_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_N2O_g_kg-1dry_ashfree_feedstock', 'Em_fac_N2O_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_NH3_g_kg-1dry_ashfree_feedstock', 'Em_fac_NH3_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_HCN_g_kg-1dry_ashfree_feedstock', 'Em_fac_HCN_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_HCl_g_kg-1dry_ashfree_feedstock', 'Em_fac_HCl_g_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_feedstock', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_feedstock_stdev', 'Em_fac_Naphtalene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Naphtalene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Naphtalene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Acenaphthylene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Acenaphthylene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Acenaphthylene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Acenaphthene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Acenaphthene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Acenaphthene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Fluorene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Fluorene_Gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Fluorene_Tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Phenanthrene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Phenanthrene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Phenanthrene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Anthracene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Anthracene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Anthracene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Fluoranthene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Fluoranthene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Fluoranthene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Pyrene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Pyrene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Pyrene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benz(a)anthracene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benz(a)anthracene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benz(a)anthracene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Chrysene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Chrysene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Chrysene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benzo(b)fluoranthene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benzo(b)fluoranthene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benzo(b)fluoranthene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benzo(k)fluoranthene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benzo(k)fluoranthene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benzo(k)fluoranthene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benzo(a)pyrene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benzo(a)pyrene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benzo(a)pyrene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Indeno(1,2,3-cd)pyrene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Indeno(1,2,3-cd)pyrene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Indeno(1,2,3-cd)pyrene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benzo(ghi)perylene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benzo(ghi)perylene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Benzo(ghi)perylene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Dibenz(ah)anthracene_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Dibenz(ah)anthracene_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_Dibenz(ah)anthracene_tot_µg_kg-1dry_ashfree_feedstock', 'Em_fac_ΣPAH-16_particle_µg_kg-1dry_ashfree_feedstock', 'Em_fac_ΣPAH-16_gas_µg_kg-1dry_ashfree_feedstock', 'Em_fac_ΣPAH-16_tot_µg_kg-1dry_ashfree_feedstock']



yaxisToPlot_7=['Pyrogas_CO_airadj_kg_ton-1dryfeedstock', 'Pyrogas_CO_airadj_kg_ton-1dryfeedstock_stdev', 'Pyrogas_CO2_airadj_kg_ton-1dryfeedstock', 'Pyrogas_CO2_airadj_kg_ton-1dryfeedstock_stdev', 'Pyrogas_CH4_airadj_kg_ton-1dryfeedstock', 'Pyrogas_CH4_airadj_kg_ton-1dryfeedstock_stdev', 'Pyrogas_CnHm_as_C3H5_airadj_kg_ton-1dryfeedstock', 'Pyrogas_CnHm_as_C3H5_airadj_kg_ton-1dryfeedstock_stdev', 'Pyrogas_H2_airadj_kg_ton-1dryfeedstock', 'Pyrogas_H2_airadj_kg_ton-1dryfeedstock_stdev', 'Pyrogas_C2H4_airadj_kg_ton-1dryfeedstock', 'Pyrogas_C2H4_airadj_kg_ton-1dryfeedstock_stdev', 'Pyrogas_N2_airadj_kg_ton-1dryfeedstock', 'Pyrogas_N2_airadj_kg_ton-1dryfeedstock_stdev', 'Pyrogas_LHV_airadj_MJ_ton-1dryfeedstock', 'Pyrogas_LHV_airadj_MJ_ton-1dryfeedstock_stdev', 'Pyrogas_CO_airadj_kg_ton-1dryashfreefeedstock', 'Pyrogas_CO_airadj_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_CO2_airadj_kg_ton-1dryashfreefeedstock', 'Pyrogas_CO2_airadj_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_CH4_airadj_kg_ton-1dryashfreefeedstock', 'Pyrogas_CH4_airadj_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_CnHm_as_C3H5_airadj_kg_ton-1dryashfreefeedstock', 'Pyrogas_CnHm_as_C3H5_airadj_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_H2_airadj_kg_ton-1dryashfreefeedstock', 'Pyrogas_H2_airadj_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_C2H4_airadj_kg_ton-1dryashfreefeedstock', 'Pyrogas_C2H4_airadj_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_N2_airadj_kg_ton-1dryashfreefeedstock', 'Pyrogas_N2_airadj_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_LHV_airadj_MJ_ton-1dryashfreefeedstock', 'Pyrogas_LHV_airadj_MJ_ton-1dryashfreefeedstock_stdev', 'Pyrogas_CO_noO2noN2_kg_ton-1dryfeedstock', 'Pyrogas_CO_noO2noN2_kg_ton-1dryfeedstock_stdev', 'Pyrogas_CO2_noO2noN2_kg_ton-1dryfeedstock', 'Pyrogas_CO2_noO2noN2_kg_ton-1dryfeedstock_stdev', 'Pyrogas_CH4_noO2noN2_kg_ton-1dryfeedstock', 'Pyrogas_CH4_noO2noN2_kg_ton-1dryfeedstock_stdev', 'Pyrogas_CnHm_as_C3H5_noO2noN2_kg_ton-1dryfeedstock', 'Pyrogas_CnHm_as_C3H5_noO2noN2_kg_ton-1dryfeedstock_stdev', 'Pyrogas_H2_noO2noN2_kg_ton-1dryfeedstock', 'Pyrogas_H2_noO2noN2_kg_ton-1dryfeedstock_stdev', 'Pyrogas_C2H4_noO2noN2_kg_ton-1dryfeedstock', 'Pyrogas_C2H4_noO2noN2_kg_ton-1dryfeedstock_stdev', 'Pyrogas_LHV_noO2noN2_MJ_ton-1dryfeedstock', 'Pyrogas_LHV_noO2noN2_MJ_ton-1dryfeedstock_stdev', 'Pyrogas_CO_noO2noN2_kg_ton-1dryashfreefeedstock', 'Pyrogas_CO_noO2noN2_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_CO2_noO2noN2_kg_ton-1dryashfreefeedstock', 'Pyrogas_CO2_noO2noN2_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_CH4_noO2noN2_kg_ton-1dryashfreefeedstock', 'Pyrogas_CH4_noO2noN2_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_CnHm_as_C3H5_noO2noN2_kg_ton-1dryashfreefeedstock', 'Pyrogas_CnHm_as_C3H5_noO2noN2_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_H2_noO2noN2_kg_ton-1dryashfreefeedstock', 'Pyrogas_H2_noO2noN2_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_C2H4_noO2noN2_kg_ton-1dryashfreefeedstock', 'Pyrogas_C2H4_noO2noN2_kg_ton-1dryashfreefeedstock_stdev', 'Pyrogas_LHV_noO2noN2_MJ_ton-1dryashfreefeedstock', 'Pyrogas_LHV_noO2noN2_MJ_ton-1dryashfreefeedstock_stdev']


xaxisToPlot = ['Feedstock_ID']


yaxisNames_8 = ['CO\u2082 (g/kg biochar)', 'CH\u2084 (g/kg biochar)', 
               'CO (g/kg biochar)', 'NMVOC (g/kg biochar)', 
               'TSP (g/kg biochar)', 'PIC (g/kg biochar)']

yaxisNames_15 = ['NO (g/kg biochar)', 'NO\u2082 (g/kg biochar)', 
               'NO\u2093 (g NO\u2082/kg biochar)', 'N\u2082 O (g/kg biochar)', 
               'NH\u2083 (g/kg biochar)', 'HCN (g/kg biochar)']

yaxisNames_16 = ['HCl (g/kg daf biochar)', 'SO\u2082 (g/kg daf biochar)',
                 'HCl (g/kg dry feedstock)', 'SO\u2082 (g/kg dry feedstock)', 
                 'HCl (g/kg biochar)', 'SO\u2082 (g/kg biochar)']

yaxisNames_10 = ['CO\u2082 (g/kg biochar), counting co-fuel C', 'CH\u2084 (g/kg biochar), counting co-fuel C', 
               'CO (g/kg biochar), counting co-fuel C', 'NMVOC (g/kg biochar), counting co-fuel C', 
               'TSP (g/kg biochar), counting co-fuel C', 'PIC (g/kg biochar), counting co-fuel C']

yaxisNames_11 = ['NO (g/kg biochar), counting co-fuel C', 'NO\u2082 (g/kg biochar), counting co-fuel C', 
               'NO\u2093 (g NO\u2082/kg biochar), counting co-fuel C', 'N\u2082 O (g/kg biochar), counting co-fuel C', 
               'NH\u2083 (g/kg biochar), counting co-fuel C', 'HCN (g/kg biochar), counting co-fuel C']

yaxisNames_12 = ['HCl (g/kg daf biochar), counting co-fuel C', 'SO\u2082 (g/kg daf biochar), counting co-fuel C',
                 'HCl (g/kg dry feedstock)', 'SO\u2082 (g/kg dry feedstock)', 
                 'HCl (g/kg biochar), counting co-fuel C', 'SO\u2082 (g/kg biochar), counting co-fuel C']

# with outliers:
# variables_group = [1,1,1,1,
#                    2,2,2,2,
#                    3,3,3,
#                    4,4,4,4,
#                    5,5,5,5,
#                    6,6,7,7]
#without outliers:
variables_group = [1,1,1,
                   2,2,2,2,
                   3,3,3,
                   4,4,4,4,
                   5,5,5,5,
                   6,7,7]

########################################3
#Primero Escojes las variables a poner en la matriz en yaxisToPlot
#yaxisToPlot =yaxisToPlot_1+yaxisToPlot_3+yaxisToPlot_5+yaxisToPlot_7
yaxisToPlot  = yaxisToPlot_12

# Segundo Escoje el numero de filas i columnas
NumberOfRows = 3
NumberOfColumns = 2

#Tercero pudes jugar con el tamano de la figura
FigureSize = (1*NumberOfRows,5*NumberOfColumns)


#We split between mean and standard deviation of y-axis.
ListaVariables=[]
ListaVariablesSDev=[]
for i in range(1,len(yaxisToPlot),2):
#for i in range(1,2,2):
    ListaVariablesSDev+=[(yaxisToPlot[i])]
    ListaVariables+=[(yaxisToPlot[i-1])]


#print(df[xaxisToPlot[0]].tolist())
#print(df[ListaVariables])
extension = '.pdf'
extensionPNG = '.png'
fig,axs = plt.subplots(nrows=NumberOfRows,ncols=NumberOfColumns,figsize=(14,10))
#fig.tight_layout()
i = 0
bar_labels_x=[]
for ax in axs.ravel():
    #print(i , df[ListaVariables[i]])
    columns = df[xaxisToPlot[0]].tolist()
   # height = 100*np.array(df[ListaVariables[i]].tolist())
    height = np.array(df[ListaVariables[i]].tolist())    
    error  = df[ListaVariablesSDev[i]].tolist()
    ax = Tbx.plotBarCharts(ax,columns, height,error,bar_labels=columns,
                              group_offset = 1.2, group = variables_group )
    if len(bar_labels_x)>0:
        ax.set_xlabel(xaxisToPlot)
    ax.set_ylabel('g/kg biochar')
    ax.set_title(yaxisNames_12[i], fontsize=11)
 #   ax.set_ylim([0,100])
    titulo = 'Em_fac_HClSO2_normalized'+extensionPNG
    i = i +1

for i in range(0,2):
    for j in range(0,2):
         axs[i,j].tick_params( axis='x',          # changes apply to the x-axis
                            which='both',      # both major and minor ticks are affected
                            bottom=False,      # ticks along the bottom edge are off
                            top=False,         # ticks along the top edge are off
                            labelbottom=False) # labels along the bottom edge are off    
# axs[6,1].set_xticks(range(0,len(columns)))
# axs[6,1].set_xticklabels(columns, rotation = 45,fontsize=8)
# axs[6,0].set_xticks(range(0,len(columns)))
# axs[6,0].set_xticklabels(columns, rotation = 45,fontsize=8) 
if os.path.exists(OUPUTPLOT):
    print(f"Saving plots in directory {OUPUTPLOT}.")
else:
    print(f"The directory {OUPUTPLOT} does not exist.")
    os.makedirs(OUPUTPLOT)
    print(f"Directory {OUPUTPLOT} created.")
    print(f"Saving plots in directory {OUPUTPLOT}.")


file_name=os.path.join(OUPUTPLOT,titulo)

fig.savefig(file_name)
  
#print(df.columns.tolist())

plt.show()

#print(ListaVariables)
#print(' ')
#print(ListaVariablesSDev)
#print(' ')



