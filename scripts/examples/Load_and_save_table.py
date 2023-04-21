# To activate Python enviroment $  C:\PythonEnv\pythonEnv\Scripts\activate.bat

import pandas as pd
import numpy as np


# Read the CSV file
df = pd.read_csv('raw_data_withoutDIV_0_with_outliers.csv', header=1, nrows=24)

# Select the desired columns
selected_columns = df[['Feedstock_short', 'Feedstock_ID', 'T° product', 'T° product.1', 'Feed_TS%mass', 'Feed_ash%TS', 'Char_Ash%', 'Char_yield%', 'Condensate_yield%', 'Gas_yield%', 'Feed_C%_readj_for_pyro_water', 'Feed_H%_readj_for_pyro_water', 'Feed_N%_readj_for_pyro_water', 'Feed_S%_readj_for_pyro_water', 'Feed_O%_readj_for_pyro_water','Feed_C%_readj_for_pyro_water_stdev', 'Feed_H%_readj_for_pyro_water_stdev', 'Feed_N%_readj_for_pyro_water_stdev', 'Feed_S%_readj_for_pyro_water_stdev', 'Feed_O%_readj_for_pyro_water_stdev', 'Char_C%', 'Char_H%', 'Char_N%', 'Char_O%', 'Char_S%', 'Char_C%_stdev', 'Char_H%_stdev', 'Char_N%_stdev', 'Char_O%_stdev', 'Char_S%_stdev']]

# Create a copy of the selected_columns DataFrame
selected_columns_copy = selected_columns.copy()



columns_to_multiply = ['Feed_TS%mass', 'Feed_ash%TS', 'Char_Ash%', 'Char_yield%', 'Condensate_yield%', 'Gas_yield%', 'Feed_C%_readj_for_pyro_water', 'Feed_H%_readj_for_pyro_water', 'Feed_N%_readj_for_pyro_water', 'Feed_S%_readj_for_pyro_water', 'Feed_O%_readj_for_pyro_water','Feed_C%_readj_for_pyro_water_stdev', 'Feed_H%_readj_for_pyro_water_stdev', 'Feed_N%_readj_for_pyro_water_stdev', 'Feed_S%_readj_for_pyro_water_stdev', 'Feed_O%_readj_for_pyro_water_stdev', 'Char_C%', 'Char_H%', 'Char_N%', 'Char_O%', 'Char_S%', 'Char_C%_stdev', 'Char_H%_stdev', 'Char_N%_stdev', 'Char_O%_stdev', 'Char_S%_stdev']
for column in columns_to_multiply:
    selected_columns_copy[column] *= 100

# Custom function to round to n significant digits
def round_to_n(x, n=3):
    if x == 0:
        return 0
    return round(x, -int(np.floor(np.log10(abs(x))) - (n - 1)))

# Apply the custom function to round the values in the columns
columns_to_round = columns_to_multiply + ['T° product', 'T° product.1']
for column in columns_to_round:
    selected_columns_copy[column] = selected_columns_copy[column].apply(lambda x: round_to_n(x, 3))

# Group the data by 'Feedstock_short' and calculate the mean and standard deviation
grouped_mean = selected_columns_copy.groupby('Feedstock_short').mean(numeric_only=True)
grouped_std = selected_columns_copy.groupby('Feedstock_short').std(numeric_only=True)

# Reset the index of the grouped DataFrames
grouped_mean = grouped_mean.reset_index()
grouped_std = grouped_std.reset_index()

# Merge the mean and standard deviation columns for the grouped DataFrames
for column in columns_to_multiply:
    if column not in ['Feedstock_short', 'Feedstock_ID']:
        mean_column = f"{column}_mean"
        std_column = f"{column}_std"
        merged_column = f"{column}_mean±std"
        
        grouped_mean[mean_column] = grouped_mean[column].apply(lambda x: round_to_n(x, 3))
        grouped_std[std_column] = grouped_std[column].apply(lambda x: round_to_n(x, 3))
        
        # Replace this line:
# grouped_mean[merged_column] = grouped_mean[mean_column] + "±" + grouped_std[std_column]  # Change this line

# With this line:
        grouped_mean[merged_column] = grouped_mean[mean_column].astype(str) + "±" + grouped_std[std_column].astype(str)


# Drop the original mean and standard deviation columns for the grouped DataFrames
grouped_mean = grouped_mean.drop(columns=[col for col in columns_to_multiply if col not in ['Feedstock_short', 'Feedstock_ID']])

# Add the grouped mean±std rows to the original DataFrame
result = pd.concat([selected_columns_copy, grouped_mean], ignore_index=True)

# Save the result to a spreadsheet
result.to_excel('result_with_grouped_mean_std.xlsx', index=False)


# Merge mean and stdev columns with rounded values
# The rest of the code remains the same
# Merge mean and stdev columns
selected_columns_copy['T° product±T° product.1'] = selected_columns_copy.apply(lambda row: f"{row['T° product']}±{row['T° product.1']}", axis=1)
selected_columns_copy['Feed_C%_readj_for_pyro_water±Feed_C%_readj_for_pyro_water_stdev'] = selected_columns_copy.apply(lambda row: f"{row['Feed_C%_readj_for_pyro_water']}±{row['Feed_C%_readj_for_pyro_water_stdev']}", axis=1)
selected_columns_copy['Char_C%±Char_C%_stdev'] = selected_columns_copy.apply(lambda row: f"{row['Char_C%']}±{row['Char_C%_stdev']}", axis=1)
selected_columns_copy['Feed_H%_readj_for_pyro_water±Feed_H%_readj_for_pyro_water_stdev'] = selected_columns_copy.apply(lambda row: f"{row['Feed_H%_readj_for_pyro_water']}±{row['Feed_H%_readj_for_pyro_water_stdev']}", axis=1)
selected_columns_copy['Char_H%±Char_H%_stdev'] = selected_columns_copy.apply(lambda row: f"{row['Char_H%']}±{row['Char_H%_stdev']}", axis=1)
selected_columns_copy['Feed_N%_readj_for_pyro_water±Feed_N%_readj_for_pyro_water_stdev'] = selected_columns_copy.apply(lambda row: f"{row['Feed_N%_readj_for_pyro_water']}±{row['Feed_N%_readj_for_pyro_water_stdev']}", axis=1)
selected_columns_copy['Char_N%±Char_N%_stdev'] = selected_columns_copy.apply(lambda row: f"{row['Char_N%']}±{row['Char_N%_stdev']}", axis=1)
selected_columns_copy['Feed_O%_readj_for_pyro_water±Feed_O%_readj_for_pyro_water_stdev'] = selected_columns_copy.apply(lambda row: f"{row['Feed_O%_readj_for_pyro_water']}±{row['Feed_O%_readj_for_pyro_water_stdev']}", axis=1)
selected_columns_copy['Char_O%±Char_O%_stdev'] = selected_columns_copy.apply(lambda row: f"{row['Char_O%']}±{row['Char_O%_stdev']}", axis=1)

# Drop the original mean and stdev columns
selected_columns_copy = selected_columns_copy.drop(columns=['T° product', 'T° product.1', 'Feed_C%_readj_for_pyro_water', 'Feed_H%_readj_for_pyro_water', 'Feed_N%_readj_for_pyro_water', 'Feed_S%_readj_for_pyro_water', 'Feed_O%_readj_for_pyro_water','Feed_C%_readj_for_pyro_water_stdev', 'Feed_H%_readj_for_pyro_water_stdev', 'Feed_N%_readj_for_pyro_water_stdev', 'Feed_S%_readj_for_pyro_water_stdev', 'Feed_O%_readj_for_pyro_water_stdev', 'Char_C%', 'Char_H%', 'Char_N%', 'Char_O%', 'Char_S%', 'Char_C%_stdev', 'Char_H%_stdev', 'Char_N%_stdev', 'Char_O%_stdev', 'Char_S%_stdev'])

# Save the modified columns to a spreadsheet
selected_columns_copy.to_excel('selected_columns.xlsx', index=False)

