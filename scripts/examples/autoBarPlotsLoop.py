# To activate Python enviroment $  C:\PythonEnv\pythonEnv\Scripts\activate.bat

import pandas as pd
import os
try:
    import ToolboxGF as Tbx
except:
    print('ToolboxGF not found')
    print('Please ToolboxGF in to PYTHONPATH by typing:')
    #print('export PYTHONPATH = $PYTHONPATH; C:\pathToDirectory\pyroflueplots\src')
    print("$ set PYTHONPATH=%PYTHONPATH%;C:\pathToDirectory\pyroflueplots\src")
    quit()
import ToolboxGF as Tbx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib.colors as pltc
import numpy as np
all_colors = [k for k,v in pltc.cnames.items()]


# User input directories
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, "..", ".."))
extensionPDF = '.pdf'
extensionPNG = '.png'
DATAFILE     = os.path.join(parent_dir,'data', 'raw_data_withoutDIV_0_with_outliers.csv')
OUPUTPLOT    = os.path.join(parent_dir,'plots', 'BarChatsLoop')

# =============================================================
df = pd.read_csv(DATAFILE, header=1, nrows=23)

#print(df)
#print(df.columns.tolist())
 
# Tuve que separar la liste de variables porque hay grupos que no tienen "stdev"
yaxisToPlot_1 = ['Em_fac_CO2_g_kg-1char',  'Em_fac_CO2_g_kg-1char_stdev', 'Em_fac_CO_g_kg-1char', 'Em_fac_CO_g_kg-1char_stdev',
               'Em_fac_CH4_g_kg-1char', 'Em_fac_CH4_g_kg-1char_stdev', 'Em_fac_NMVOC_g_kg-1char', 'Em_fac_NMVOC_g_kg-1char_stdev',
               'Em_fac_TSP_g_kg-1char', 'Em_fac_TSP_g_kg-1char_stdev', 'Em_fac_PIC_g_kg-1char', 'Em_fac_PIC_g_kg-1char_stdev',
               'Em_fac_SO2_g_kg-1char', 'Em_fac_SO2_g_kg-1char_stdev', 'Em_fac_NO_g_kg-1char', 'Em_fac_NO_g_kg-1char_stdev',
               'Em_fac_NO2_g_kg-1char', 'Em_fac_NO2_g_kg-1char_stdev', 'Em_fac_N2O_g_kg-1char', 'Em_fac_N2O_g_kg-1char_stdev',
               'Em_fac_NH3_g_kg-1char', 'Em_fac_NH3_g_kg-1char_stdev', 'Em_fac_HCN_g_kg-1char', 'Em_fac_HCN_g_kg-1char_stdev',
               'Em_fac_HCl_g_kg-1char', 'Em_fac_HCl_g_kg-1char_stdev', 'Em_fac_NOx_gNO2_kg-1char', 'Em_fac_NOx_gNO2_kg-1char_stdev']

yaxisToPlot_8 = ['Em_fac_CO2_g_kg-1char_by_gas_comp', 'Em_fac_CO2_g_kg-1char_by_gas_comp_stdev', 'Em_fac_CO_g_kg-1char_by_gas_comp', 'Em_fac_CO_g_kg-1char_by_gas_comp_stdev', 'Em_fac_TSP_g_kg-1char_by_gas_comp', 'Em_fac_TSP_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_PIC_g_kg-1char_by_gas_comp', 'Em_fac_PIC_g_kg-1char_by_gas_comp_stdev', 'Em_fac_CH4_g_kg-1char_by_gas_comp', 'Em_fac_CH4_g_kg-1char_by_gas_comp_stdev', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_NOx_gNO2_kg-1char_by_gas_comp', 'Em_fac_NOx_gNO2_kg-1char_by_gas_comp_stdev', 'Em_fac_N2O_g_kg-1char_by_gas_comp', 'Em_fac_N2O_g_kg-1char_by_gas_comp_stdev', 'Em_fac_NH3_g_kg-1char_by_gas_comp', 'Em_fac_NH3_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_NO_g_kg-1char_by_gas_comp', 'Em_fac_NO_g_kg-1char_by_gas_comp_stdev', 'Em_fac_NO2_g_kg-1char_by_gas_comp', 'Em_fac_NO2_g_kg-1char_by_gas_comp_stdev', 'Em_fac_HCN_g_kg-1char_by_gas_comp', 'Em_fac_HCN_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_SO2_g_kg-1char_by_gas_comp', 'Em_fac_SO2_g_kg-1char_by_gas_comp_stdev', 'Em_fac_HCl_g_kg-1char_by_gas_comp', 'Em_fac_HCl_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp_stdev',
               'Em_fac_CO2_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_CO2_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_CO_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_CO_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_TSP_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_TSP_g_kg-1dry_ashfree_char_by_gas_comp_stdev',
               'Em_fac_PIC_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_PIC_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_CH4_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_CH4_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char_by_gas_comp_stdev',
               'Em_fac_N2O_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_N2O_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_NH3_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_NH3_g_kg-1dry_ashfree_char_by_gas_comp_stdev',
               'Em_fac_NO_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_NO_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_NO2_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_NO2_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_HCN_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_HCN_g_kg-1dry_ashfree_char_by_gas_comp_stdev']


yaxisToPlot_9 = ['Em_fac_CO2_g_kg-1char_by_gas_comp_normalized', 'Em_fac_CO2_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_CO_g_kg-1char_by_gas_comp_normalized', 'Em_fac_CO_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_TSP_g_kg-1char_by_gas_comp_normalized', 'Em_fac_TSP_g_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_PIC_g_kg-1char_by_gas_comp_normalized', 'Em_fac_PIC_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_CH4_g_kg-1char_by_gas_comp_normalized', 'Em_fac_CH4_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp_normalized', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_NOx_gNO2_kg-1char_by_gas_comp_normalized', 'Em_fac_NOx_gNO2_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_N2O_g_kg-1char_by_gas_comp_normalized', 'Em_fac_N2O_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_NH3_g_kg-1char_by_gas_comp_normalized', 'Em_fac_NH3_g_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_NO_g_kg-1char_by_gas_comp_normalized', 'Em_fac_NO_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_NO2_g_kg-1char_by_gas_comp_normalized', 'Em_fac_NO2_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_HCN_g_kg-1char_by_gas_comp_normalized', 'Em_fac_HCN_g_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_SO2_g_kg-1char_by_gas_comp_normalized', 'Em_fac_SO2_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_HCl_g_kg-1char_by_gas_comp_normalized', 'Em_fac_HCl_g_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev',
               'Em_fac_CO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_CO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_CO_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_CO_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_TSP_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_TSP_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev',
               'Em_fac_PIC_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_PIC_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_CH4_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_CH4_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev',
               'Em_fac_N2O_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_N2O_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_NH3_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_NH3_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev',
               'Em_fac_NO_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_NO_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_NO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_NO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_HCN_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_HCN_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev',
               'Em_fac_CO2_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_CO2_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_CO_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_CO_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_TSP_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_TSP_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_PIC_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_PIC_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_CH4_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_CH4_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_NOx_gNO2_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NOx_gNO2_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_N2O_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_N2O_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_NH3_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NH3_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_NO_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NO_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_NO2_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NO2_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_HCN_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_HCN_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_SO2_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_SO2_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_HCl_g_kg-1char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_HCl_g_kg-1char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_CO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_CO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_CO_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_CO_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_TSP_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_TSP_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_PIC_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_PIC_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_CH4_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_CH4_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_N2O_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_N2O_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_NH3_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NH3_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev',
               'Em_fac_NO_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NO_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_NO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_NO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev', 'Em_fac_HCN_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition', 'Em_fac_HCN_g_kg-1dry_ashfree_char_by_gas_comp_normalized_by_fuel_addition_stdev']


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



variables_group = [1,1,1,1,
                   2,2,2,2,
                   3,3,3,
                   4,4,4,4,
                   5,5,5,5,
                   6,6,7,7]

########################################3
# Primero graficamos las variables que tienen STDEV
#yaxisToPlot =yaxisToPlot_1+yaxisToPlot_3+yaxisToPlot_5+yaxisToPlot_7
yaxisToPlot =yaxisToPlot_8

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
for i in range(len(ListaVariables)):
    #print(df[ListaVariables[i]])
    fig,ax = plt.subplots()
    columns = df[xaxisToPlot[0]].tolist()
    height = df[ListaVariables[i]].tolist()
    error  = df[ListaVariablesSDev[i]].tolist()
    bar_labels = df[xaxisToPlot[0]].tolist()
    ax = Tbx.plotBarCharts(ax,columns, height,error,bar_labels,
                           group_offset = 1.2, group = variables_group)
    ax.set_xlabel(xaxisToPlot)
    ax.set_ylabel(ListaVariables[i])
    ax.set_title(ListaVariables[i])
    titulo = ListaVariables[i]+'_'+xaxisToPlot[0]+extensionPNG

    if not os.path.exists(OUPUTPLOT):
        print(f"The directory {OUPUTPLOT} does not exist.")
        os.makedirs(OUPUTPLOT)
        print(f"Directory {OUPUTPLOT} created.")
        print(f"Saving plots in directory {OUPUTPLOT}.")

    file_name=os.path.join(OUPUTPLOT,titulo)
    fig.savefig(file_name)

#########################################################################
########################################################################
# SEgundo Graficamos las variables que no tienen STDEV
#ListaVariables=yaxisToPlot_2+yaxisToPlot_4+yaxisToPlot_6

#print(df[xaxisToPlot[0]])
#print(df[ListaVariables])
#output_folder = 'BarCharWithoutSTDEV'
#extension = '.pdf'
#extensionPNG = '.png'
#for i in range(len(ListaVariables)):
#    print(df[ListaVariables[i]])
#    fig,ax = plt.subplots()
 #   columns = df[xaxisToPlot[0]].tolist()
  #  height = df[ListaVariables[i]].tolist()
   # bar_labels = df[xaxisToPlot[0]].tolist()
    #ax = Tbx.plotBarCharts(ax,columns, height,[],bar_labels)
    #ax.set_xlabel(xaxisToPlot)
    #ax.set_ylabel(ListaVariables[i])
    #ax.set_title(ListaVariables[i])
    #titulo = ListaVariables[i]+'_'+xaxisToPlot[0]+extensionPNG
    #file_name=os.path.join(output_folder,titulo)
    #fig.savefig(file_name)

    

#plt.show()

#print(ListaVariables)
#print(' ')
#print(ListaVariablesSDev)
#print(' ')



