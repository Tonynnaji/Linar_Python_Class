# import plotting library
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns




plt.figure(figsize=([7.4]))
plt.xticks(rotation =([90]))
fuel_unit = pd.Dataframe({'unit':['BBL', 'GAL','GRAMSU','KGU','MCF',
'MMBTU','MWDTH','MWHTH','TON'], 'count':[7998,84,464,110,11354,180,95,100,8958]})
sns.barplot(data=fuel_unit, x ='unit', y = 'count')
plt.xlabel('fuel Unit')

# Because of the extreme range of the values for the fuel 
# unit, we can plot the barchart by taking the logarthm of the y-axis as follows:

g = sns.barplot(data = fuel_unit, x ='unit', y ='count')
g.set_yscale("log")
g.set_ylim([1,12000])
plt.xscale('fuel_uni  xcvbt')
 