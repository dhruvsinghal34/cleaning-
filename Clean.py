import pandas as pd
import csv 

df = pd.read_csv("final.csv")

del df["name"]
del df["star_name_distance,"] 
del df["host_mass"] 
del df["star_radius,"] 
del df["star_luminosity"] 

df = df.rename({
    "st_hostname":"star_name",
    "st_mass":"mass",
    "st_rad":"radius",
    "lu_lumi":"luminosity",
    "dis_dist":"distance",
}, axis = "columns")

df.to_csv("main_star_file.csv")

print (df.shape)