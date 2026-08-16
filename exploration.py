#%%
# commiting with git
# git add exploration.py            # tells Git to include this files changes in my next staging (checkpoint)
# git commit -m "noted instructions on how to push and commit for git" # git creates this staging only on mac
# git push # checkpoint is uploaded to github and visible to anyone who looks at remote repository (repo) aka the project folder
# %%
# install and import geopandas
# bash: conda install -c conda-forge geopandas 
import geopandas as gpd
# install and import fiona
# bash : conda install -c conda-forge fiona
import fiona
# %%
# first created .gitignore file and pasted RDS-2013-0009.7_Data_Format2_GDB/ inside so it doesnt commit
# inspect file
gdb_path = "RDS-2013-0009.7_Data_Format2_GDB/Data/FPA_FOD_20260615.gdb"
layers = fiona.listlayers(gdb_path)
print(layers)
# %%
# load and check head of fires data
fires = gpd.read_file(gdb_path, layer="Fires")
print(fires.shape)
print(fires.columns.tolist())
fires.head()
# %%
