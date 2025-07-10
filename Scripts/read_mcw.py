# read_mcw.py
import pandas as pd
import numpy as np

def read_and_process():
    df = pd.read_csv('../Data/1.MCW_Processed_Iso_NOV23.csv', parse_dates=[2])

    # From the site ID, just take the first two characters to snow rain, snow, or stream for the type
    df['Type'] = df.Site_ID.str[:2]

    # Take just the site number from the site ID, removing rain or snow labeling
    df['Site_no'] = df.Site_ID.str[3:5]
    df['Site_no'] = df['Site_no'].apply(pd.to_numeric)

    # Create new columns of isotope values only from rain, snow, and stream 
    df['D_18O_Rain'] = np.where(df['Type'] == 'RC', df['D_18O'], np.nan)
    df['D_18O_Snow'] = np.where(df['Type'] == 'IB', df['D_18O'], np.nan)
    df['D_18O_MC'] = np.where(df['Type'] == 'MC', df['D_18O'], np.nan)
    df['D_18O_BC'] = np.where(df['Type'] == 'BC', df['D_18O'], np.nan)
    # Added D2H rain vs snow for weighted precip 
    df['D_2H_Rain'] = np.where(df['Type'] == 'RC', df['D_2H'], np.nan)
    df['D_2H_Snow'] = np.where(df['Type'] == 'IB', df['D_2H'], np.nan)

    # Create column for std deviation
    df['D_18O_std_Rain'] = np.where(df['Type'] == 'RC', df['D_18O_StDev'], np.nan)
    df['D_18O_std_Snow'] = np.where(df['Type'] == 'IB', df['D_18O_StDev'], np.nan)
    df['D_18O_StDev_Precip'] = np.where((df['Type'] == 'RC')|
                                   (df['Type'] == 'IB'), df['D_18O_StDev'], np.nan)
    
    # Set precip values to only rain or snow, not stream samples
    df['D_18O_Precip'] = np.where((df['Type'] == 'RC')|
                                   (df['Type'] == 'IB'), df['D_18O'], np.nan)

    df['D_2H_Precip'] = np.where((df['Type'] == 'RC') |
                                   (df['Type'] == 'IB'), df['D_2H'], np.nan)
    return df