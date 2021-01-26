# course: Project Computational Science, University of Amsterdam
# authors: Tamara Stoof, Emma Kok, Esmée van der Mark
# group: Stralend
# date: 26-01-2021

# this file contains the codes that create 
# figures 6, 7 and 8 as shown in the poster and report


import statistics
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
import json


# import all data from the txt files

# load data of simulation without firelines
with open("noFireLines.txt") as f:
    noFirelines = json.load(f)

# load data of simulation with 
# temporary firelines and different distances
with open("temporary_distance_1.txt") as f:
    temporary1 = json.load(f)

with open("temporary_distance_2.txt") as f:
    temporary2 = json.load(f)

with open("temporary_distance_3.txt") as f:
    temporary3 = json.load(f)

# load data of simulation with constructed
# firelines and different distances and of shape 1
with open("constructed_distance_1_shape_1.txt") as f:
    dis1_shape1 = json.load(f)

with open("constructed_distance_2_shape_1.txt") as f:
    dis2_shape1 = json.load(f)

with open("constructed_distance_3_shape_1.txt") as f:
    dis3_shape1 = json.load(f)

# load data of simulation with constructed
# firelines and different distances and of shape 2
with open("constructed_distance_1_shape_2.txt") as f:
    dis1_shape2 = json.load(f)

with open("constructed_distance_2_shape_2.txt") as f:
    dis2_shape2 = json.load(f)

with open("constructed_distance_3_shape_2.txt") as f:
    dis3_shape2 = json.load(f)


# load data of simulation with constructed
# firelines and different distances and of shape 3
with open("constructed_distance_1_shape_3.txt") as f:
    dis1_shape3 = json.load(f)

with open("constructed_distance_2_shape_3.txt") as f:
    dis2_shape3 = json.load(f)

with open("constructed_distance_3_shape_3.txt") as f:
    dis3_shape3 = json.load(f)


# set theme grid
sns.set_style("whitegrid")


"""
    First plot; a barplot of all the constructed firelines (incl. all shapes and distances).
    Corresponds to Figure 6 of the poster. Figure number does not correspond to the figure number in the report.
"""

# construct data frames consisting of constructed 
# fire lines variables used to create figure 6 of the poster
k = pd.DataFrame({ 'Distance': np.repeat('1.25 km', 150), 'Fraction burned': dis1_shape1, 'Shape': np.repeat('1', 150)})
l = pd.DataFrame({ 'Distance': np.repeat('1.25 km', 150), 'Fraction burned': dis1_shape2, 'Shape': np.repeat('2', 150)})
m = pd.DataFrame({ 'Distance': np.repeat('1.25 km', 150), 'Fraction burned': dis1_shape3, 'Shape': np.repeat('3', 150)})

o = pd.DataFrame({ 'Distance': np.repeat('2.50 km', 150), 'Fraction burned': dis2_shape1, 'Shape': np.repeat('1', 150)})
p = pd.DataFrame({ 'Distance': np.repeat('2.50 km', 150), 'Fraction burned': dis2_shape2, 'Shape': np.repeat('2', 150)})
q = pd.DataFrame({ 'Distance': np.repeat('2.50 km', 150), 'Fraction burned': dis2_shape3, 'Shape': np.repeat('3', 150)})

r = pd.DataFrame({ 'Distance': np.repeat('3.75 km', 150), 'Fraction burned': dis3_shape1, 'Shape': np.repeat('1', 150)})
s = pd.DataFrame({ 'Distance': np.repeat('3.75 km', 150), 'Fraction burned': dis3_shape2, 'Shape': np.repeat('2', 150)})
t = pd.DataFrame({ 'Distance': np.repeat('3.75 km', 150), 'Fraction burned': dis3_shape3, 'Shape': np.repeat('3', 150)})

# combine data frames so it can be used in the barplot 
df1 = k.append(l).append(m).append(o).append(p).append(q).append(r).append(s).append(t)

# create the barplot of figure 6 (in the poster)

plt.figure(1)
sns.barplot( x = 'Distance', y = 'Fraction burned', hue = 'Shape', \
    saturation = 1, palette = 'husl', data = df1, capsize = .1, \
    linewidth = 0.5, errwidth = 1.5, ci = "sd")\
    .set_title('Efficiency of the nine different constructed firelines', fontweight = 'bold')

"""
    Second plot; a boxplot of the three temporary fireline distances.
    Corresponds to Figure 7 of the poster. Figure number does not correspond to the figure number in the report.
"""

# construct data frames consisting of temporary
# fire lines variables used to create Figure 7 of the poster
u = pd.DataFrame({ 'Location of temporary fireline relative to PF': \
    np.repeat('Directly on PF' , 150), 'Fraction burned': temporary1})

v = pd.DataFrame({ 'Location of temporary fireline relative to PF': \
    np.repeat('Behind PF' , 150), 'Fraction burned': temporary2})

w = pd.DataFrame({ 'Location of temporary fireline relative to PF': \
    np.repeat('Distance ahead of PF' , 150), 'Fraction burned': temporary3})

# combine data frames so it can be used in the boxplot
df2 = u.append(v).append(w)

# make box lines black and median red
PROPS = {
    'boxprops':{'facecolor':'white', 'edgecolor':'black'},
    'medianprops':{'color':'red'},
    'whiskerprops':{'color':'black'},
    'capprops':{'color':'black'}}


# create the boxplot of figure 7 (in the poster)
plt.figure(2)
sns.boxplot( x = 'Location of temporary fireline relative to PF',\
    y = 'Fraction burned', data = df2, palette = 'husl' ,linewidth = 1.5, **PROPS ).set_title('Efficiency of temporary firelines at different locations relative to PF',\
    fontweight = 'bold')

"""
    Third plot; a barplot of the best mitigation strategies, and the situation without firelines.
    Corresponds to Figure 8 of the poster. Figure number does not correspond to the figure number in the report.
"""

# construct data frames consisting of best and worst constructed and temporary
# fire lines and the NoFireLines variables used to create Figure 8 and Figure 9 of the poster
temp_most = pd.DataFrame({ 'Type of fireline': np.repeat('Temporary (directly on)' , 150), \
    'Fraction burned': temporary1})

cons_most = pd.DataFrame({ 'Type of fireline': np.repeat('Constructed (1.25 km/shape 1)' , 150), \
    'Fraction burned': dis1_shape1})

temp_least = pd.DataFrame({ 'Type of fireline': np.repeat('Temporary (placed behind)' , 150), \
    'Fraction burned': temporary2})

cons_least = pd.DataFrame({ 'Type of fireline': np.repeat('Constructed (3.75 km/shape 3)' , 150), \
    'Fraction burned': dis3_shape3})

no_firelines = pd.DataFrame({ 'Type of fireline': np.repeat('None' , 150), \
    'Fraction burned': noFirelines})

plt.figure(3)
# combine data frames so it can be used in the barplot to compare the most effective mitigation strategies to no fire lines at all
df3 = temp_most.append(cons_most).append(no_firelines)

sns.barplot( x = 'Type of fireline',\
    y = 'Fraction burned', data = df3, errwidth = 3, palette = 'bright', ci = 'sd', capsize = .1).set_title('Most effective mitigation techniques compared to no fire lines',\
    fontweight = 'bold', fontsize = 15)


"""
    Fourth plot; a barplot of the worst mitigation strategies, and the situation without firelines.
    Corresponds to Figure 4b of the poster.
"""

plt.figure(4)

# combine data frames so it can be used in the barplot to compare the least effective mitigation strategies to no fire lines at all
df4 = temp_least.append(cons_least).append(no_firelines)

sns.barplot( x = 'Type of fireline',\
    y = 'Fraction burned', data = df4, palette = 'bright', errwidth = 3, ci = 'sd', capsize = .1).set_title('Least effective mitigation techniques compared to no fire lines',\
    fontweight = 'bold', fontsize = 15)

plt.show()