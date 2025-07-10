# MoresCreekWatershed_Seasonal_Precipitaiton_EndMembers
# MoresCreekWatershed_ID
Mores Creek Watershed, ID - Boise State University - Hydrologic Sciences

This code compares precipitation end-member methods and their varying contributions to streamflow in a snow-dominated watershed. 

## Notebooks/
- 01_MWL.ipynb
  - Treasure Valley; Mores Creek Watershed; Dry Creek Experimental Watershed; GMWL
    - Distribution Plot
- 02_wrf_analysis.ipynb
  - MCW (Temp; SWE; Precip Accumulation; Precip; Snow)
  - WY_2023.nc (Not provided in Github ; BSU)     
- 03_Weather_Data
  - Meteoric Weather Station Analysis  
- 04_Isotope_Analysis.ipynb
  - MCW & DCEW Stream Isotopes
  - Elevation vs. Precipiation Isotope Analysis
  - Individual Site Analysis
  - Sine Curve Fitting
  - Site Precipiation Accumulation vs Isotope Value
- 05_Mixing_Model.ipynb
  - MCW; BCW End-Member Mixing Analysis
    - Base vs Alternative Methods
  - Percent Difference
  - MCW Hydrograph
  - Additional Analysis
    - Over-under Representation of End-Members
- 06_precip_stream_stats.ipynb
  - Precipiation Mass and Area Weighted Isotopes
      - Precip vs Elevation vs Total Watershed Area
  - Sine Cureve SE Calculations
  - MCW Weighted Stream Samples  
- 07_Error_Calculation_EMMA.ipynb
  -   Wighted vs Unweighted Alternative Methods
  -   Gaussian Error Propigation for End-Member Mixing Analysis
  -   Cold vs Warm Season Alternative Methods Precipiation Fraction w/ SE
  -   Variance in AM

## Scripts/
- packages.py
- colors.py
- read_mcw.py
- read_dcew.py

## Data/
1. MCW_Processed_Iso_NOV23.csv
2. DCEW_Stream_Isotopes.csv
3. swe_daily_site7_wrf.csv
4. ACPRCP_daily_site7_wrf.csv
5. Temp_daily_site7_wrf.csv  
6. swe_daily_snotel.csv
7. SN_WaterYear_2023.csv # Mores Creek Snotel
8. Town_Creek_metdata.csv # Boise National Forest Met Station
9. met_station_temps.csv # MCW Meteorological Stations
10. PP_weather_FY22.csv # Piolot Peak Met Station
11. Temp_allsites_weekly.csv
12. precip_Accum_RC_IB.csv 
13. morescreekmassweighting.csv

14. MCW_Precip_Iso_Metrics.csv
15. RC_Accum_BySite.csv
16. DCEW_Danny_Precip_Isotopes.csv 
17. MCW_DCEW_Stream_Iso.csv

18. MoresCreek_USGS_Gage.csv
19. precip_accum_site_metrics.csv
