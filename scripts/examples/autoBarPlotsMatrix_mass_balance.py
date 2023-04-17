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

DATAFILE      = os.path.join(parent_dir,'data', 'raw_data_withoutDIV_0_with_outliers.csv')
OUPUTPLOT     = os.path.join(parent_dir,'plots', 'BarCharsMatrix_MassBalance')

# =============================================================

df = pd.read_csv(DATAFILE, header=1, nrows=23)

#print(df)
 
# Tuve que separar la liste de variables porque hay grupos que no tienen "stdev"
yaxisToPlot_1 = ['Char_yield%',  'Remove_stdev', 'Char_HHV%yield', 'Char_HHV%yield_stdev',
               'Condensate_yield%', 'Remove_stdev', 'Condensate_HHV%yield', 'Condensate_HHV%yield_stdev',
               'Gas_yield%', 'Remove_stdev', 'Gas_HHV%yield_by_diff', 'Gas_HHV%yield_by_diff_stdev',
               'Char_yield%_ashfreedry', 'Char_yield%_ashfreedry_stdev', 'Char_HHV%dry_ashfree_yield', 'Char_HHV%dry_ashfree_yield_stdev',
               'Condensate_yield%_ashfreedry', 'Condensate_yield%_ashfreedry_stdev', 'Condensate_HHV%dry_ashfree_yield', 'Condensate_HHV%dry_ashfree_yield_stdev',
               'Gas_yield%_ashfreedry', 'Gas_yield%_ashfreedry_stdev', 'Gas_HHV%yield_dryashfreefeedstock_by_diff', 'Gas_HHV%yield_dryashfreefeedstock_by_diff_stdev',
               'Gas_HHV%yield_by_composition', 'Gas_HHV%yield_by_composition_stdev', 'Gas_HHV%yield_dryashfreefeedstock_by_composition', 'Gas_HHV%yield_dryashfreefeedstock_by_composition_stdev']

yaxisToPlot_9 = ['Char_yield%',  'Remove_stdev', 'Char_HHV%yield', 'Char_HHV%yield_stdev',
               'Condensate_yield%', 'Remove_stdev', 'Condensate_HHV%yield', 'Condensate_HHV%yield_stdev',
               'Gas_yield%', 'Remove_stdev', 'Gas_HHV%yield_by_diff', 'Gas_HHV%yield_by_diff_stdev']

yaxisToPlot_10 = ['Char_yield%',  'Remove_stdev', 'Char_HHV%yield', 'Char_HHV%yield_stdev',
               'Condensate_yield%', 'Remove_stdev', 'Readjusted_condensate_HHV_yield_%_by_gas_comp', 'Condensate_HHV%yield_stdev',
               'Gas_yield%', 'Remove_stdev', 'Gas_HHV%yield_by_composition', 'Gas_HHV%yield_by_composition_stdev']

yaxisToPlot_12 = ['Char_yield%',  'Remove_stdev', 'Char_C%yield', 'Char_C%yield_stdev',
               'Condensate_yield%', 'Remove_stdev', 'Readjusted_condensate_C_yield_%_by_gas_comp', 'Readjusted_condensate_C_yield_%_by_gas_comp_stdev',
               'Gas_yield%', 'Remove_stdev', 'Gas_C%_calc_yield', 'Gas_C%_calc_yield_stdev']

yaxisToPlot_14 = ['Char_yield%_ashfreedry',  'Char_yield%_ashfreedry_stdev', 'Char_H%dry_yield', 'Char_H%dry_yield_stdev',
               'Condensate_yield%_ashfreedry', 'Condensate_yield%_ashfreedry_stdev', 'Readjusted_condensate_H_yield_%_by_gas_comp_dry_feed', 'Readjusted_condensate_H_yield_%_by_gas_comp_dry_feed_stdev',
               'Gas_yield%_ashfreedry', 'Gas_yield%_ashfreedry_stdev', 'Gas_H%_calc_yieldashfreedry', 'Gas_H%_calc_yieldashfreedry_stdev']

yaxisToPlot_13 = ['CO2(%)_adj_noO2N2',  'CO2(%)_adj_noO2N2_stdev', 'CO(%)_adj_noO2N2', 'CO(%)_adj_noO2N2_stdev',
               'CH4(%)_adj_noO2N2', 'CH4(%)_adj_noO2N2_stdev', 'H2(%)_adj_noO2N2', 'H2(%)_adj_noO2N2_stdev',
               'CnHm(%)_adj_noO2N2', 'CnHm(%)_adj_noO2N2_stdev', 'C2H4(%)_adj_noO2N2', 'C2H4(%)_adj_noO2N2_stdev']

yaxisToPlot_11 = ['Char_yield%',  'Remove_stdev', 'Char_C%yield', 'Char_C%yield_stdev',
               'Condensate_yield%', 'Remove_stdev', 'Condensate_C%yield', 'Condensate_C%yield_stdev',
               'Gas_yield%', 'Remove_stdev', 'Gas_C%yield_by_diff', 'Gas_C%yield_by_diff_stdev']

yaxisToPlot_8 = ['Em_fac_CO2_g_kg-1char',  'Em_fac_CO2_g_kg-1char_stdev', 'Em_fac_CO_g_kg-1char', 'Em_fac_CO_g_kg-1char_stdev',
               'Em_fac_CH4_g_kg-1char', 'Em_fac_CH4_g_kg-1char_stdev', 'Em_fac_NMVOC_g_kg-1char', 'Em_fac_NMVOC_g_kg-1char_stdev',
               'Em_fac_TSP_g_kg-1char', 'Em_fac_TSP_g_kg-1char_stdev', 'Em_fac_PIC_g_kg-1char', 'Em_fac_PIC_g_kg-1char_stdev',
               'Em_fac_SO2_g_kg-1char', 'Em_fac_SO2_g_kg-1char_stdev', 'Em_fac_NO_g_kg-1char', 'Em_fac_NO_g_kg-1char_stdev',
               'Em_fac_NO2_g_kg-1char', 'Em_fac_NO2_g_kg-1char_stdev', 'Em_fac_N2O_g_kg-1char', 'Em_fac_N2O_g_kg-1char_stdev',
               'Em_fac_NH3_g_kg-1char', 'Em_fac_NH3_g_kg-1char_stdev', 'Em_fac_HCN_g_kg-1char', 'Em_fac_HCN_g_kg-1char_stdev',
               'Em_fac_HCl_g_kg-1char', 'Em_fac_HCl_g_kg-1char_stdev', 'Em_fac_NOx_gNO2_kg-1char', 'Em_fac_NOx_gNO2_kg-1char_stdev']

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


yaxisNames_1 = ['Char yield (%mass of feedstock as received)',  'Char energy yield (%HHV of feedstock as received)', 
               'Condensate yield (% mass of feedstock as received)', 'Condensate energy yield (%HHV of feedstock as received)', 
               'Gas yield (% mass of feedstock as received, by difference)', 'Gas  energy yield (%HHV of feedstock as received, by difference)', 
               'Char yield (%mass of dry, ash free feedstock)', 'Char energy yield (%HHV of dry, ash free feedstock)', 
               'Condensate yield (%mass of dry, ash free feedstock)', 'Condensate energy yield (%HHV of dry, ash free feedstock)', 
               'Gas yield (%mass of dry, ash free feedstock, by difference)', 'Gas energy yield (%HHV of dry, ash free feedstock, by difference)', 
               'Gas energy yield (%HHV of feedstock as received, by analysed gas composition)', 'Gas energy yield (%HHV of dry, ash free feedstock, by analysed gas composition)']

yaxisNames_2 = ['Char yield (%mass of feedstock as received)',  'Char energy yield (%HHV of feedstock as received)', 
               'Condensate yield (% mass of feedstock as received)', 'Condensate energy yield (%HHV of feedstock as received)', 
               'Gas yield (% mass of feedstock as received, by difference)', 'Gas  energy yield (%HHV of feedstock as received,\n by difference)']

yaxisNames_3 = ['Char yield (%mass of feedstock as received)',  'Char energy yield (%HHV of feedstock as received)', 
               'Condensate yield (% mass of feedstock as received)', 'Condensate energy yield (%HHV of feedstock as received,\n adjusted from gas composition)', 
               'Gas yield (% mass of feedstock as received, by difference)', 'Gas  energy yield (%HHV of feedstock as received,\n by gas composition)']

yaxisNames_4 = ['Char yield (%mass of feedstock as received)',  'Char C yield (%mass of feedstock C, as received)', 
               'Condensate yield (% mass of feedstock as received)', 'Condensate C yield (%mass of feedstock C, as received)', 
               'Gas yield (% mass of feedstock as received, by difference)', 'Gas C yield (%mass of feedstock C, as received,\n by difference)']

yaxisNames_5 = ['Char yield (%mass of feedstock as received)',  'Char C yield (%mass of feedstock C, as received)', 
               'Condensate yield (% mass of feedstock as received)', 'Condensate C yield (%mass of feedstock C, as received,\n adjusted from gas composition)', 
               'Gas yield (% mass of feedstock as received, by difference)', 'Gas C yield (%mass of feedstock C, as received,\n by gas composition)']

yaxisNames_6 = ['CO2 (% of gas composition)',  'CO (% of gas composition)', 
               'CH4 (% of gas composition)', 'H2 (% of gas composition)', 
               'CnHm (% of gas composition)', 'C2H4 (% of gas composition)']

yaxisNames_7 = ['Char yield (%mass of feedstock, dry ash free)',  'Char H yield (%mass of feedstock H, dry ash free)', 
               'Condensate yield (% mass of feedstock, dry ash free', 'Condensate H yield (%mass of feedstock H, dry ash free,\n adjusted from gas composition)', 
               'Gas yield (% mass of feedstock, dry ash free, by difference)', 'Gas H yield (%mass of feedstock H, dry ash free,\n by gas composition)']

variables_group = [1,1,1,1,
                   2,2,2,2,
                   3,3,3,
                   4,4,4,4,
                   5,5,5,5,
                   6,6,7,7]

########################################3
#Primero Escojes las variables a poner en la matriz en yaxisToPlot
#yaxisToPlot =yaxisToPlot_1+yaxisToPlot_3+yaxisToPlot_5+yaxisToPlot_7
yaxisToPlot  = yaxisToPlot_14

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
    height = 100*np.array(df[ListaVariables[i]].tolist())
    error  = df[ListaVariablesSDev[i]].tolist()
    ax = Tbx.plotBarCharts(ax,columns, height,error,bar_labels=columns,
                              group_offset = 1.2, group = variables_group )
    if len(bar_labels_x)>0:
        ax.set_xlabel(xaxisToPlot)
    ax.set_ylabel('%')
    ax.set_title(yaxisNames_7[i], fontsize=11)
    ax.set_ylim([0,100])
    titulo = 'Matrix_mass_H_daf'+extensionPNG
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



