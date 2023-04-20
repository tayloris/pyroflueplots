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
all_colors = [k for k,v in pltc.cnames.items()]

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, "..", ".."))
extensionPDF = '.pdf'
extensionPNG = '.png'

# User input directories

DATA      = os.path.join(parent_dir,'data', 'raw_data_withoutDIV_0_with_outliers.csv')
OUPUTPLOT = os.path.join(parent_dir,'plots', 'Figures_Em_con')

# =============================================================

df = pd.read_csv(DATA, header=1, nrows=24)

#print(df)
#print(df.columns.tolist())
 

yaxisToPlot = ['Em_con_CO2_%', 'Em_con_CO2_%_stdev', 'Em_con_CO_mg_Nm-3', 'Em_con_CO_mg_Nm-3_stdev',
               'Em_con_CH4_mgC_Nm-3', 'Em_con_CH4_mgC_Nm-3_stdev', 'Em_con_NMVOC_mgC_Nm-3', 'Em_con_NMVOC_mgC_Nm-3_stdev',
               'Em_con_TSP_mg_Nm-3', 'Em_con_TSP_mg_Nm-3_stdev', 'Em_con_PIC_mg_Nm-3', 'Em_con_PIC_mg_Nm-3_stdev',
               'Em_con_SO2_mg_Nm-3', 'Em_con_SO2_mg_Nm-3_stdev', 'Em_con_NO_asNO2_mg_Nm-3', 'Em_con_NO_asNO2_mg_Nm-3_stdev',
               'Em_con_NO2_mg_Nm-3', 'Em_con_NO2_mg_Nm-3_stdev', 'Em_con_N2O_mg_Nm-3', 'Em_con_N2O_mg_Nm-3_stdev',
               'Em_con_NH3_mg_Nm-3', 'Em_con_NH3_mg_Nm-3_stdev', 'Em_con_HCN_mg_Nm-3', 'Em_con_HCN_mg_Nm-3_stdev',
               'Em_con_HCl_mg_Nm-3', 'Em_con_HCl_mg_Nm-3_stdev', 'Em_con_NOx_mgNO2_Nm-3', 'Em_con_NOx_mgNO2_Nm-3_stdev',
               'Em_con_H2O_g_kg-1feedstock', 'Em_con_H2O_g_kg-1feedstock_stdev', 'Em_con_CO_mg_Nm-3_normalized', 'Em_con_CO_mg_Nm-3_stdev_normalized',
               'Em_con_CH4_mgC_Nm-3_normalized', 'Em_con_CH4_mgC_Nm-3_stdev_normalized', 'Em_con_NMVOC_mgC_Nm-3_normalized', 'Em_con_NMVOC_mgC_Nm-3_stdev_normalized',
               'Em_con_TSP_mg_Nm-3_normalized', 'Em_con_TSP_mg_Nm-3_stdev_normalized', 'Em_con_PIC_mg_Nm-3_normalized', 'Em_con_PIC_mg_Nm-3_stdev_normalized',
               'Em_con_SO2_mg_Nm-3_normalized', 'Em_con_SO2_mg_Nm-3_stdev_normalized', 'Em_con_NO_asNO2_mg_Nm-3_normalized', 'Em_con_NO_asNO2_mg_Nm-3_stdev_normalized',
               'Em_con_NO2_mg_Nm-3_normalized', 'Em_con_NO2_mg_Nm-3_stdev_normalized', 'Em_con_N2O_mg_Nm-3_normalized', 'Em_con_N2O_mg_Nm-3_stdev_normalized',
               'Em_con_NH3_mg_Nm-3_normalized', 'Em_con_NH3_mg_Nm-3_stdev_normalized', 'Em_con_HCN_mg_Nm-3_normalized', 'Em_con_HCN_mg_Nm-3_stdev_normalized',
               'Em_con_HCl_mg_Nm-3_normalized', 'Em_con_HCl_mg_Nm-3_stdev_normalized', 'Em_con_NOx_mgNO2_Nm-3_normalized', 'Em_con_NOx_mgNO2_Nm-3_stdev_normalized',
               'Em_con_H2O_%_normalized', 'Em_con_H2O_%_stdev_normalized', 'Em_con_CO2_%_normalized', 'Em_con_CO2_%_stdev_normalized',
               'NOx_readjusted_per_11%O2_mgNO2_Nm-3', 'NOx_readjusted_per_11%O2_mgNO2_Nm-3_stdev', ]

yaxisToPlot_1 = ['Em_con_CO2_%', 'Em_con_CO2_%_stdev', 'Em_con_CO_mg_Nm-3', 'Em_con_CO_mg_Nm-3_stdev',
               'Em_con_CH4_mgC_Nm-3', 'Em_con_CH4_mgC_Nm-3_stdev', 'Em_con_NMVOC_mgC_Nm-3', 'Em_con_NMVOC_mgC_Nm-3_stdev',
               'Em_con_TSP_mg_Nm-3', 'Em_con_TSP_mg_Nm-3_stdev', 'Em_con_PIC_mg_Nm-3', 'Em_con_PIC_mg_Nm-3_stdev',
               'Em_con_SO2_mg_Nm-3', 'Em_con_SO2_mg_Nm-3_stdev', 'Em_con_NO_asNO2_mg_Nm-3', 'Em_con_NO_asNO2_mg_Nm-3_stdev',
               'Em_con_NO2_mg_Nm-3', 'Em_con_NO2_mg_Nm-3_stdev', 'Em_con_N2O_mg_Nm-3', 'Em_con_N2O_mg_Nm-3_stdev',
               'Em_con_NH3_mg_Nm-3', 'Em_con_NH3_mg_Nm-3_stdev', 'Em_con_HCN_mg_Nm-3', 'Em_con_HCN_mg_Nm-3_stdev',
               'Em_con_HCl_mg_Nm-3', 'Em_con_HCl_mg_Nm-3_stdev', 'Em_con_NOx_mgNO2_Nm-3', 'Em_con_NOx_mgNO2_Nm-3_stdev',
               'Em_con_H2O_g_kg-1feedstock', 'Em_con_H2O_g_kg-1feedstock_stdev', 
               'Em_con_CH4_mgC_Nm-3_by_gas_comp_normalized', 'Em_con_CH4_mgC_Nm-3_by_gas_comp_normalized_stdev', 'Em_con_NMVOC_mgC_Nm-3_by_gas_comp_normalized', 'Em_con_NMVOC_mgC_Nm-3_by_gas_comp_normalized_stdev',
               'Em_con_TSP_mg_Nm-3_by_gas_comp_normalized', 'Em_con_TSP_mg_Nm-3_by_gas_comp_normalized_stdev', 'Em_con_PIC_mg_Nm-3_by_gas_comp_normalized', 'Em_con_PIC_mg_Nm-3_by_gas_comp_normalized_stdev',
               'Em_con_SO2_mg_Nm-3_by_gas_comp_normalized', 'Em_con_SO2_mg_Nm-3_by_gas_comp_normalized_stdev', 'Em_con_NO_asNO2_mg_Nm-3_by_gas_comp_normalized', 'Em_con_NO_asNO2_mg_Nm-3_by_gas_comp_normalized_stdev',
               'Em_con_NO2_mg_Nm-3_by_gas_comp_normalized', 'Em_con_NO2_mg_Nm-3_by_gas_comp_normalized_stdev', 'Em_con_N2O_mg_Nm-3_by_gas_comp_normalized', 'Em_con_N2O_mg_Nm-3_by_gas_comp_normalized_stdev',
               'Em_con_NH3_mg_Nm-3_by_gas_comp_normalized', 'Em_con_NH3_mg_Nm-3_by_gas_comp_normalized_stdev', 'Em_con_HCN_mg_Nm-3_by_gas_comp_normalized', 'Em_con_HCN_mg_Nm-3_by_gas_comp_normalized_stdev',
               'Em_con_HCl_mg_Nm-3_by_gas_comp_normalized', 'Em_con_HCl_mg_Nm-3_by_gas_comp_normalized_stdev', 'Em_con_NOx_mgNO2_Nm-3_by_gas_comp_normalized', 'Em_con_NOx_mgNO2_Nm-3_by_gas_comp_normalized_stdev',
               'Em_con_H2O_g_kg-1feedstock_by_gas_comp_normalized', 'Em_con_H2O_g_kg-1feedstock_by_gas_comp_normalized_stdev', 'Em_con_CO_mg_Nm-3_by_gas_comp_normalized', 'Em_con_CO_mg_Nm-3_by_gas_comp_normalized_stdev',
               'Em_con_CO2_%_by_gas_comp_normalized', 'Em_con_CO2_%_by_gas_comp_normalized_stdev', 'NOx_readjusted_per_11%O2_mgNO2_Nm-3_by_gas_comp', 'NOx_readjusted_per_11%O2_mgNO2_Nm-3_by_gas_comp_stdev', ]

yaxisToPlot_2 = ['Em_fac_CO2_g_kg-1char',  'Em_fac_CO2_g_kg-1char_stdev', 'Em_fac_CO_g_kg-1char', 'Em_fac_CO_g_kg-1char_stdev',
               'Em_fac_CH4_g_kg-1char', 'Em_fac_CH4_g_kg-1char_stdev', 'Em_fac_NMVOC_g_kg-1char', 'Em_fac_NMVOC_g_kg-1char_stdev',
               'Em_fac_TSP_g_kg-1char', 'Em_fac_TSP_g_kg-1char_stdev', 'Em_fac_PIC_g_kg-1char', 'Em_fac_PIC_g_kg-1char_stdev',
               'Em_fac_SO2_g_kg-1char', 'Em_fac_SO2_g_kg-1char_stdev', 'Em_fac_NO_g_kg-1char', 'Em_fac_NO_g_kg-1char_stdev',
               'Em_fac_NO2_g_kg-1char', 'Em_fac_NO2_g_kg-1char_stdev', 'Em_fac_N2O_g_kg-1char', 'Em_fac_N2O_g_kg-1char_stdev',
               'Em_fac_NH3_g_kg-1char', 'Em_fac_NH3_g_kg-1char_stdev', 'Em_fac_HCN_g_kg-1char', 'Em_fac_HCN_g_kg-1char_stdev',
               'Em_fac_HCl_g_kg-1char', 'Em_fac_HCl_g_kg-1char_stdev', 'Em_fac_NOx_gNO2_kg-1char', 'Em_fac_NOx_gNO2_kg-1char_stdev']

yaxisToPlot_3 = ['Em_fac_CO2_g_kg-1feedstock', 'Em_fac_CO2_g_kg-1feedstock_stdev',
               'Em_fac_CO_g_kg-1feedstock', 'Em_fac_CO_g_kg-1feedstock_stdev', 'Em_fac_CH4_g_kg-1feedstock', 'Em_fac_CH4_g_kg-1feedstock_stdev',
               'Em_fac_NMVOC_g_kg-1feedstock', 'Em_fac_NMVOC_g_kg-1feedstock_stdev', 'Em_fac_TSP_g_kg-1feedstock', 'Em_fac_TSP_g_kg-1feedstock_stdev',
               'Em_fac_PIC_g_kg-1feedstock', 'Em_fac_PIC_g_kg-1feedstock_stdev', 'Em_fac_SO2_g_kg-1feedstock', 'Em_fac_SO2_g_kg-1feedstock_stdev',
               'Em_fac_NO_g_kg-1feedstock', 'Em_fac_NO_g_kg-1feedstock_stdev', 'Em_fac_NO2_g_kg-1feedstock', 'Em_fac_NO2_g_kg-1feedstock_stdev',
               'Em_fac_N2O_g_kg-1feedstock', 'Em_fac_N2O_g_kg-1feedstock_stdev', 'Em_fac_NH3_g_kg-1feedstock', 'Em_fac_NH3_g_kg-1feedstock_stdev',
               'Em_fac_HCN_g_kg-1feedstock', 'Em_fac_HCN_g_kg-1feedstock_stdev', 'Em_fac_HCl_g_kg-1feedstock', 'Em_fac_HCl_g_kg-1feedstock_stdev', 
               'Em_fac_NOx_gNO2_kg-1feedstock', 'Em_fac_NOx_gNO2_kg-1feedstock_stdev']

yaxisToPlot_4=['Em_fac_CO2_g_kg-1dry_ashfree_char', 'Em_fac_CO2_g_kg-1dry_ashfree_char_stdev', 'Em_fac_CO_g_kg-1dry_ashfree_char', 'Em_fac_CO_g_kg-1dry_ashfree_char_stdev',
               'Em_fac_CH4_g_kg-1dry_ashfree_char', 'Em_fac_CH4_g_kg-1dry_ashfree_char_stdev', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char_stdev',
               'Em_fac_TSP_g_kg-1dry_ashfree_char', 'Em_fac_TSP_g_kg-1dry_ashfree_char_stdev', 'Em_fac_PIC_g_kg-1dry_ashfree_char', 'Em_fac_PIC_g_kg-1dry_ashfree_char_stdev',
               'Em_fac_SO2_g_kg-1dry_ashfree_char', 'Em_fac_SO2_g_kg-1dry_ashfree_char_stdev', 'Em_fac_NO_g_kg-1dry_ashfree_char', 'Em_fac_NO_g_kg-1dry_ashfree_char_stdev',
               'Em_fac_NO2_g_kg-1dry_ashfree_char', 'Em_fac_NO2_g_kg-1dry_ashfree_char_stdev', 'Em_fac_N2O_g_kg-1dry_ashfree_char', 'Em_fac_N2O_g_kg-1dry_ashfree_char_stdev',
               'Em_fac_NH3_g_kg-1dry_ashfree_char', 'Em_fac_NH3_g_kg-1dry_ashfree_char_stdev', 'Em_fac_HCN_g_kg-1dry_ashfree_char', 'Em_fac_HCN_g_kg-1dry_ashfree_char_stdev',
               'Em_fac_HCl_g_kg-1dry_ashfree_char', 'Em_fac_HCl_g_kg-1dry_ashfree_char_stdev', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_char', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_stdev']

yaxisToPlot_5 = ['Em_fac_CO2_g_kg-1char_by_gas_comp',  'Em_fac_CO2_g_kg-1char_by_gas_comp_stdev', 'Em_fac_CO_g_kg-1char_by_gas_comp', 'Em_fac_CO_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_CH4_g_kg-1char_by_gas_comp', 'Em_fac_CH4_g_kg-1char_by_gas_comp_stdev', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_TSP_g_kg-1char_by_gas_comp', 'Em_fac_TSP_g_kg-1char_by_gas_comp_stdev', 'Em_fac_PIC_g_kg-1char_by_gas_comp', 'Em_fac_PIC_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_SO2_g_kg-1char_by_gas_comp', 'Em_fac_SO2_g_kg-1char_by_gas_comp_stdev', 'Em_fac_NO_g_kg-1char_by_gas_comp', 'Em_fac_NO_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_NO2_g_kg-1char_by_gas_comp', 'Em_fac_NO2_g_kg-1char_by_gas_comp_stdev', 'Em_fac_N2O_g_kg-1char_by_gas_comp', 'Em_fac_N2O_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_NH3_g_kg-1char_by_gas_comp', 'Em_fac_NH3_g_kg-1char_by_gas_comp_stdev', 'Em_fac_HCN_g_kg-1char_by_gas_comp', 'Em_fac_HCN_g_kg-1char_by_gas_comp_stdev',
               'Em_fac_HCl_g_kg-1char_by_gas_comp', 'Em_fac_HCl_g_kg-1char_by_gas_comp_stdev', 'Em_fac_NOx_gNO2_kg-1char_by_gas_comp', 'Em_fac_NOx_gNO2_kg-1char_by_gas_comp_stdev',
               'Em_fac_CO2_g_kg-1char_by_gas_comp_normalized',  'Em_fac_CO2_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_CO_g_kg-1char_by_gas_comp_normalized', 'Em_fac_CO_g_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_CH4_g_kg-1char_by_gas_comp_normalized', 'Em_fac_CH4_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp_normalized', 'Em_fac_NMVOC_g_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_TSP_g_kg-1char_by_gas_comp_normalized', 'Em_fac_TSP_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_PIC_g_kg-1char_by_gas_comp_normalized', 'Em_fac_PIC_g_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_SO2_g_kg-1char_by_gas_comp_normalized', 'Em_fac_SO2_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_NO_g_kg-1char_by_gas_comp_normalized', 'Em_fac_NO_g_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_NO2_g_kg-1char_by_gas_comp_normalized', 'Em_fac_NO2_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_N2O_g_kg-1char_by_gas_comp_normalized', 'Em_fac_N2O_g_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_NH3_g_kg-1char_by_gas_comp_normalized', 'Em_fac_NH3_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_HCN_g_kg-1char_by_gas_comp_normalized', 'Em_fac_HCN_g_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_HCl_g_kg-1char_by_gas_comp_normalized', 'Em_fac_HCl_g_kg-1char_by_gas_comp_normalized_stdev', 'Em_fac_NOx_gNO2_kg-1char_by_gas_comp_normalized', 'Em_fac_NOx_gNO2_kg-1char_by_gas_comp_normalized_stdev',
               'Em_fac_CO2_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_CO2_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_CO_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_CO_g_kg-1dry_ashfree_char_by_gas_comp_stdev',
               'Em_fac_CH4_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_CH4_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char_by_gas_comp_stdev',
               'Em_fac_TSP_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_TSP_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_PIC_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_PIC_g_kg-1dry_ashfree_char_by_gas_comp_stdev',
               'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_NO_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_NO_g_kg-1dry_ashfree_char_by_gas_comp_stdev',
               'Em_fac_NO2_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_NO2_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_N2O_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_N2O_g_kg-1dry_ashfree_char_by_gas_comp_stdev',
               'Em_fac_NH3_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_NH3_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_HCN_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_HCN_g_kg-1dry_ashfree_char_by_gas_comp_stdev',
               'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp_stdev', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_by_gas_comp', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_by_gas_comp_stdev',
               'Em_fac_CO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_CO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_CO_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_CO_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev',
               'Em_fac_CH4_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_CH4_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_NMVOC_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev',
               'Em_fac_TSP_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_TSP_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_PIC_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_PIC_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev',
               'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_SO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_NO_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_NO_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev',
               'Em_fac_NO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_NO2_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_N2O_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_N2O_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev',
               'Em_fac_NH3_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_NH3_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_HCN_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_HCN_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev',
               'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_HCl_g_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_by_gas_comp_normalized', 'Em_fac_NOx_gNO2_kg-1dry_ashfree_char_by_gas_comp_normalized_stdev']

xaxisToPlot = ['T° burner', 'Feed_N%_readj_for_pyro_water','Gas_flow_kg_h', 'Feed_N_load_kg_h-1', 'Gas_N_load_kg_h-1_by_diff', 
               'Flue_gas_comb_incl_prop_excess_air_O2%mol', 'Est_excess_air_flow_kg_h-1',
               'Est_excess_air_flow_Nm3_h-1', 'Est_excess_air_flow_kmol_h-1', 'Propane_C_load_kg_h-1_by_diff', 'Gas_C_load_kg_h-1_by_diff', 
               'Feed_wet_flow_kg_h', 'Feed_dry_flow_kg_h', 'Est_prop_flow_kmol_h-1', 'Flue_gas_comb_incl_prop_excess_air_mass_flow_kg_h-1', 'Flue_gas_comb_incl_prop_excess_air_vol_flow_Nm3_h-1',
               'Theo_flue_gas_comp_stoic_air_no_prop_mass_flow_kg_h-1', 'Theo_flue_gas_comp_stoic_air_no_prop_gas_flow_Nm3_h-1',
               'Est_prop_mass_flow_kg_h-1', 'Est_prop_flow_Nm3_h-1', ]

xaxisToPlot_1 = ['T° burner','Flue_gas_comb_incl_prop_excess_air_O2%mol_by_gas_comp', 'Gas_flow_kg_h', 'Feed_N_load_kg_h-1', 'Gas_N_load_kg_h-1_by_diff', 
               'Flue_gas_comb_incl_prop_excess_air_mass_flow_kg_h-1_by_gas_comp', 'Flue_gas_comb_incl_prop_excess_air_vol_flow_Nm3_h-1_by_gas_comp_normalized',
               'Theo_flue_gas_comp_stoic_air_no_prop_mass_flow_kg_h-1_by_gas_comp', 'Theo_flue_gas_comp_stoic_air_no_prop_gas_flow_Nm3_h-1_by_gas_comp',
               'Est_prop_mass_flow_kg_h-1_by_gas_comp', 'Est_prop_flow_Nm3_h-1_by_gas_comp', 'Est_prop_flow_kmol_h-1_by_gas_comp', 'Est_excess_air_flow_kg_h-1_by_gas_comp',
               'Est_excess_air_flow_Nm3_h-1_by_gas_comp', 'Est_excess_air_flow_kmol_h-1_by_gas_comp', 'Propane_C_load_kg_h-1_by_gas_comp', 'Gas_C_load_kg_h-1_by_gas_comp', 
               'Feed_wet_flow_kg_h', 'Feed_dry_flow_kg_h', 'Feed_N%_readj_for_pyro_water', ]

ListaVariables=[]
ListaVariablesSDev=[]
for i in range(1,len(yaxisToPlot_1),2):
    ListaVariablesSDev+=[(yaxisToPlot_1[i])]
    ListaVariables+=[(yaxisToPlot_1[i-1])]
#ListaVariables=['Em_con_NOx_mgNO2_Nm-3','']
#ListaVariablesSDev=['Em_con_NOx_mgNO2_Nm-3_stdev','']

categories = df['A_Feedstock_name'].unique()
#colorSelection = all_colors[0:len(categories)]
#colorSelection=['tab:blue','tab:orange','tab:green','tab:red','tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive','tab:cyan']
colorSelection=['#8c510a', '#d8b365', '#f6e8c3', '#c7eae5', '#5ab4ac', '#01665e', '#762a83', '#80cdc1', '#35978f', '#bf812d', '#dfc27d', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
colorDict = Tbx.TwoListToDict(categories,colorSelection)

ListaLinea = ['Em_con_NOx_mgNO2_Nm-3','NOx_readjusted_per_11%O2_mgNO2_Nm-3_by_gas_comp']
categoriesSetpoint = df['Setpoint SPJ temp'].unique()
colorTemp=['black','black','black', 'black','black']
colorDict2 = Tbx.TwoListToDict(categoriesSetpoint,colorTemp)

output_folder = 'Figures_Em_con'
extension = '.pdf'
extensionPNG = '.png'
for j in range(len(xaxisToPlot_1)):
    for i in range(len(ListaVariables)):
        print('plotting:', xaxisToPlot_1[j],',   ',ListaVariables[i],',  og,',ListaVariablesSDev[i])
        fig, ax =  plt.subplots()
        if ListaVariables[i] in ListaLinea: ax.axhline(y = 300, color = 'r', linestyle = '-',label='Norwegian emission limit')
        ax = Tbx.plotFlueGasStatter(ax,df, xKey=xaxisToPlot_1[j],
                                        yKey=ListaVariables[i],
                                        yErrKey=ListaVariablesSDev[i],
                                        cDict1=colorDict,
                                        cDict2=colorDict2)
        # titulo = ListaVariables[i]+extension
        # file_name=os.path.join(output_folder,titulo)
        # fig.savefig(file_name)
        titulo = ListaVariables[i]+'_'+xaxisToPlot_1[j]+extensionPNG
        if not os.path.exists(OUPUTPLOT):
            print(f"The directory {OUPUTPLOT} does not exist.")
            os.makedirs(OUPUTPLOT)
            print(f"Directory {OUPUTPLOT} created.")
            print(f"Saving plots in directory {OUPUTPLOT}.")

        file_name=os.path.join(OUPUTPLOT,titulo)
        fig.savefig(file_name)
        plt.close('all')
# fig, ax =  plt.subplots()
# ax = Tbx.plotFlueGasStatter(ax,df, xKey=xaxisToPlot[0],
#                                    yKey=ListaVariables[0],
#                                    yErrKey=ListaVariablesSDev[0],
#                                    cDict1=colorDict,
#                                    cDict2=colorDict2)


#plt.show()

print(ListaVariables)
print(' ')
print(ListaVariablesSDev)
print(' ')
print('colorDict  :',colorDict)
print(' ')
print('colorDict  :',colorDict2)


