# course: Project Computational Science, University of Amsterdam
# authors: Tamara Stoof, Emma Kok, Esmée van der Mark
# group: Stralend
# date: 26-01-2021

# this file contains the codes that create all
# figures shown in the poster and report

 
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


###############################################################################################################################
# # first violinplot, comparing the fraction burned of the constructed (dis2/shape1), temporary (placed directly on the propogation front) and no firelines

# g = pd.DataFrame({ 'Type of fireline': np.repeat('Constructed' , 150), 'Fraction burned': dis1_shape2})
# h = pd.DataFrame({ 'Type of fireline': np.repeat('Temporary' , 150), 'Fraction burned': temporary1})
# i = pd.DataFrame({ 'Type of fireline': np.repeat('No fireline' , 150), 'Fraction burned': noFirelines})

# # dataframe to use for the violinplot 
# plt.figure(1)
# df1 = g.append(h).append(i)

# # making the box lines black, with exception of the median which will be red
# PROPS = {
#     'boxprops':{'facecolor':'none', 'edgecolor':'black'},
#     'medianprops':{'color':'red'},
#     'whiskerprops':{'color':'black'},
#     'capprops':{'color':'black'}}

# sns.violinplot( x = 'Type of fireline', y = 'Fraction burned', saturation = 1, linewidth = 1.75, palette = 'husl', data = df1).set_title('Efficiency of the best constructed and temporary firelines (compared to no firelines)')


###############################################################################################################################
# Second plot, which is a barplot of all the constructed firelines (all the shapes and distances)

k = pd.DataFrame({ 'Distance': np.repeat('1.25 km', 150), 'Fraction burned': dis1_shape1, 'Shape': np.repeat('1', 150)})
l = pd.DataFrame({ 'Distance': np.repeat('1.25 km', 150), 'Fraction burned': dis1_shape2, 'Shape': np.repeat('2', 150)})
m = pd.DataFrame({ 'Distance': np.repeat('1.25 km', 150), 'Fraction burned': dis1_shape3, 'Shape': np.repeat('3', 150)})

o = pd.DataFrame({ 'Distance': np.repeat('2.50 km', 150), 'Fraction burned': dis2_shape1, 'Shape': np.repeat('1', 150)})
p = pd.DataFrame({ 'Distance': np.repeat('2.50 km', 150), 'Fraction burned': dis2_shape2, 'Shape': np.repeat('2', 150)})
q = pd.DataFrame({ 'Distance': np.repeat('2.50 km', 150), 'Fraction burned': dis2_shape3, 'Shape': np.repeat('3', 150)})

r = pd.DataFrame({ 'Distance': np.repeat('3.75 km', 150), 'Fraction burned': dis3_shape1, 'Shape': np.repeat('1', 150)})
s = pd.DataFrame({ 'Distance': np.repeat('3.75 km', 150), 'Fraction burned': dis3_shape2, 'Shape': np.repeat('2', 150)})
t = pd.DataFrame({ 'Distance': np.repeat('3.75 km', 150), 'Fraction burned': dis3_shape3, 'Shape': np.repeat('3', 150)})

# dataframe combining all the information, which will be used in the barplot 
plt.figure(2)
df2 = k.append(l).append(m).append(o).append(p).append(q).append(r).append(s).append(t)

sns.barplot( x = 'Distance', y = 'Fraction burned', hue = 'Shape', saturation = 1, palette = 'husl', data = df2, capsize = .1, linewidth = 0.5, errwidth = 1.5, ci = "sd").set_title('Efficiency of the nine different constructed firelines')


####################################################################################################################
# third plot, which is a boxplot combining the three temporary fireline distances 

u = pd.DataFrame({ 'Location of temporary fireline relative to PF': np.repeat('Directly on PF' , 150), 'Fraction burned': temporary1})
v = pd.DataFrame({ 'Location of temporary fireline relative to PF': np.repeat('Behind PF' , 150), 'Fraction burned': temporary2})
w = pd.DataFrame({ 'Location of temporary fireline relative to PF': np.repeat('Distance ahead of PF' , 150), 'Fraction burned': temporary3})

# dataframe combining all the information, which will be used in the boxplot 
df3 = u.append(v).append(w)

# making the box lines black, with exception of the median which will be red
PROPS = {
    'boxprops':{'facecolor':'none', 'edgecolor':'black'},
    'medianprops':{'color':'red'},
    'whiskerprops':{'color':'black'},
    'capprops':{'color':'black'}}

plt.figure(3)
sns.boxplot( x = 'Location of temporary fireline relative to PF', y = 'Fraction burned', data = df3, palette = 'husl', linewidth = 1.2,**PROPS).set_title('Fraction burned, using temporary firelines at different locations relative to PF')


#############################################################################################################################################
# fourth plot, which is a barplot combining the best and worst mitigation strategies and also comparing it to the situation which has no fireline

x = pd.DataFrame({ 'Type of fireline': np.repeat('Temporary' , 150), 'Fraction burned': temporary1, 'situation': np.repeat('best', 150)})
y = pd.DataFrame({ 'Type of fireline': np.repeat('Constructed' , 150), 'Fraction burned': dis1_shape2, 'situation': np.repeat('best', 150)})
z = pd.DataFrame({ 'Type of fireline': np.repeat('Temporary' , 150), 'Fraction burned': temporary3, 'situation': np.repeat('worst', 150)})
zz = pd.DataFrame({ 'Type of fireline': np.repeat('Constructed' , 150), 'Fraction burned': dis3_shape3, 'situation': np.repeat('worst', 150)})

normal = pd.DataFrame({ 'Type of fireline': np.repeat('None' , 150), 'Fraction burned': noFirelines, 'situation': np.repeat('normal', 150)})

# dataframe combining all the information, which will be used in a barplot 
df4 = x.append(y).append(z).append(zz).append(normal)
plt.figure(4)
sns.barplot( x = 'situation', y = 'Fraction burned', hue = 'Type of fireline', data = df4, palette = 'husl', linewidth = 1.2, ci = 'sd').set_title('Fraction burned, comparing best and worst mitigation strategies')
plt.show()


