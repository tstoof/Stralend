# course name: Project Computational Science, University of Amsterdam
# author: Tamara Stoof
# group: Stralend
# date: 26-01-2021

# this file contains the statistic tests used
# to test if the different mitigation techniques
# had significantly different efficiencies


import json
import matplotlib.pyplot as plt
import pylab
import scipy.stats as stats


# open and store all txt files containing the simulation data

# load data of simulation without firelines
with open("noFireLines.txt") as f:
    noFireLine = json.load(f)

# load data of simulation with 
# temporary firelines and different distances
with open("temporary_distance_1.txt") as f:
    temporary_distance_1 = json.load(f)

with open("temporary_distance_2.txt") as f:
    temporary_distance_2 = json.load(f)

with open("temporary_distance_3.txt") as f:
    temporary_distance_3 = json.load(f)

# load data of simulation with constructed
# firelines and different distances and of shape 1
with open("constructed_distance_1_shape_1.txt") as f:
    constructed_distance_1_shape_1 = json.load(f)

with open("constructed_distance_2_shape_1.txt") as f:
    constructed_distance_2_shape_1 = json.load(f)

with open("constructed_distance_3_shape_1.txt") as f:
    constructed_distance_3_shape_1 = json.load(f)

# load data of simulation with constructed
# firelines and different distances and of shape 2
with open("constructed_distance_1_shape_2.txt") as f:
    constructed_distance_1_shape_2 = json.load(f)

with open("constructed_distance_2_shape_2.txt") as f:
    constructed_distance_2_shape_2 = json.load(f)

with open("constructed_distance_3_shape_2.txt") as f:
    constructed_distance_3_shape_2 = json.load(f)


# load data of simulation with constructed
# firelines and different distances and of shape 3
with open("constructed_distance_1_shape_3.txt") as f:
    constructed_distance_1_shape_3 = json.load(f)

with open("constructed_distance_2_shape_3.txt") as f:
    constructed_distance_2_shape_3 = json.load(f)

with open("constructed_distance_3_shape_3.txt") as f:
    constructed_distance_3_shape_3 = json.load(f)



# one could use a probplot to viually asses 
# the gaussianity of the variable
# plt.figure()
# stats.probplot(variable_name, dist="norm",plot=pylab)
# pylab.show()

# a non-visual way to assess normality
# p < 0.05 means the variable is 
# not normally distributed


# check if data is normally distributed
# constructed fire lines, distance 1, shape 1 is non-gaussian
stat, p = stats.shapiro(constructed_distance_1_shape_1)

# constructed fire lines, distance 2, shape 1 is non-gaussian
stat, p = stats.shapiro(constructed_distance_2_shape_1)

# constructed fire lines, distance 3, shape 1 is non-gaussian
stat, p = stats.shapiro(constructed_distance_3_shape_1)

# constructed fire lines, distance 1, shape 2 is non-gaussian
stat, p = stats.shapiro(constructed_distance_1_shape_2)

# constructed fire lines, distance 2, shape 2 is non-gaussian
stat, p = stats.shapiro(constructed_distance_2_shape_2)

# constructed fire lines, distance 3, shape 2 is non-gaussian
stat, p = stats.shapiro(constructed_distance_3_shape_2) 

# constructed fire lines, distance 1, shape 3 is non-gaussian
stat, p = stats.shapiro(constructed_distance_1_shape_3)

# constructed fire lines, distance 2, shape 3 is non-gaussian
stat, p = stats.shapiro(constructed_distance_2_shape_3)

# constructed fire lines, distance 3, shape 3 is non-gaussian
stat, p = stats.shapiro(constructed_distance_3_shape_3)

# temporary fire lines, distnace 1 is non-gaussian
stat, p = stats.shapiro(temporary_distance_1)

# temporary fire lines, distnace 2 is non-gaussian
stat, p = stats.shapiro(temporary_distance_2)

# temporary fire lines, distnace 3 is non-gaussian
stat, p = stats.shapiro(temporary_distance_3)

# no fire lines is non-gaussian
stat, p= stats.shapiro(noFireLine)

 

"""
# all variables are non-gaussian
# the followoing non-parametric tests will be used
# Kruskal-Wallis test 
# wilcoxon-Mann-Whitney test 

# general usage of these tests
# stats.mannwhitneyu(group1, group2, alternative='two-sided')
# stats.kruskal(x,y,z)

# Kruskal-Wallis hypothesis
# Ho: no difference in means
# Ha: difference in means

# Mann-whitney hypothesis
# Ho: no difference in means
# Ha1: mu_1 < mu_2
# Ha2: mu_1 > mu_2

# choice of alternative hypothesis depends 
# on the combination of variables to be compared 
"""

# constants: constructed fire lines, distance 1
# variable: shapes

# p < 0.05 
# the group means differ significantly
stats.kruskal(constructed_distance_1_shape_1,constructed_distance_1_shape_2, constructed_distance_1_shape_3)

# testing difference between shape 1 and shape 2
# p < 0.05
# shape 2 is more efficient than shape 1
stats.mannwhitneyu(constructed_distance_1_shape_1, constructed_distance_1_shape_2, alternative='greater')

# testing difference between shape 1 and shape 3
# p < 0.05
# shape 1 is more efficient than shape 3
stats.mannwhitneyu(constructed_distance_1_shape_1, constructed_distance_1_shape_3, alternative='less')

# testing difference between shape 2 and shape 3
# p < 0.05
# shape 2 is more efficient than shape 3
stats.mannwhitneyu(constructed_distance_1_shape_2, constructed_distance_1_shape_3, alternative='less')



# constants: constructed fire lines, distance 2
# variable: shapes

# P < 0.05 
# the group means differ significantly
stats.kruskal(constructed_distance_2_shape_1, constructed_distance_2_shape_2, constructed_distance_2_shape_3)

# testing difference between shape 1 and shape 2
# p < 0.05
# shape 1 is more efficient than shape 2
stats.mannwhitneyu(constructed_distance_2_shape_1, constructed_distance_2_shape_2, alternative='less')

# testing difference between shape 1 and shape 3
# p < 0.05
# shape 1 is more efficient than shape 3
stats.mannwhitneyu(constructed_distance_2_shape_1, constructed_distance_2_shape_3, alternative='less')

# testing difference between shape 2 and shape 3
# p < 0.05
# shape 2 is more efficient than shape 3
stats.mannwhitneyu(constructed_distance_2_shape_2, constructed_distance_2_shape_3, alternative='less')



# constants: constructed fire lines, distance 3
# variable: shapes

# p < 0.05 
# the group means differ significantly
stats.kruskal(constructed_distance_3_shape_1,constructed_distance_3_shape_2, constructed_distance_3_shape_3)

# testing difference between shape 1 and shape 2
# p > 0.05
# shape 1 is more efficient than shape 2
stats.mannwhitneyu(constructed_distance_3_shape_1, constructed_distance_3_shape_2, alternative='less')

# testing difference between shape 1 and shape 3
# p > 0.05
# shape 1 is more efficient than shape 3
stats.mannwhitneyu(constructed_distance_3_shape_1, constructed_distance_3_shape_3, alternative='less')

# testing difference between shape 2 and shape 3
# p > 0.05
# shape 2 is more efficient than shape 3
stats.mannwhitneyu(constructed_distance_3_shape_2, constructed_distance_3_shape_3, alternative='less')

"""
    Summary:
    For constructed fire lines at distance 1, the best shapes are: 2 > 1 > 3
    For constructed fire lines at distance 2, the best shapes are: 1 > 2 > 3
    For constructed fire lines at distance 3, the best shapes are: 1 > 2 > 3 
"""

# constants: temporary fire lines
# variable: distance

# p < 0.05
# the group means differ significantly
stats.kruskal(temporary_distance_1, temporary_distance_2, temporary_distance_3)

# testing difference between distance 1 and 2
# p < 0.05
# distance 1 is more efficient than distance 2
stats.mannwhitneyu(temporary_distance_1, temporary_distance_2, alternative="less")

# testing difference between distance 1 and 3
# p < 0.05
# distance 1 is more efficient than distance 3
stats.mannwhitneyu(temporary_distance_1, temporary_distance_3, alternative="less")

# testing difference between distance 2 and 3
# p < 0.05
# distance 2 is more efficient than distance 3
stats.mannwhitneyu(temporary_distance_2, temporary_distance_3, alternative="less")


"""
    Summary:
    For temporary fire lines, the best distances are: 1 > 2 > 3
"""

# constants: constructed fire lines, shape 1
# variable: distance

# p < 0.05
# the group means differ significantly
stats.kruskal(constructed_distance_1_shape_1, constructed_distance_2_shape_1,constructed_distance_3_shape_1)

# testing difference between distance 1 and 2
# p < 0.05
# distance 2 is more efficient than distance 1
stats.mannwhitneyu(constructed_distance_1_shape_1, constructed_distance_2_shape_1, alternative="greater")

# testing difference between distance 1 and 3
# p < 0.05
# distance 3 is more efficient than distance 1
stats.mannwhitneyu(constructed_distance_1_shape_1, constructed_distance_3_shape_1, alternative="greater")

# testing difference between distance 2 and 3
# p < 0.05
# distance 2 is more efficient than distance 3
stats.mannwhitneyu(constructed_distance_2_shape_1, constructed_distance_3_shape_1, alternative="less")


# constants: constructed fire lines, shape 2
# variable: distance

# p < 0.05
# the group means differ significantly
stats.kruskal(constructed_distance_1_shape_2, constructed_distance_2_shape_2,constructed_distance_3_shape_2)

# testing difference between distance 1 and 2
# p < 0.05
# distance 1 is more efficient than distance 2
stats.mannwhitneyu(constructed_distance_1_shape_2, constructed_distance_2_shape_2, alternative="less")

# testing difference between distance 1 and 3
# p < 0.05
# distance 1 is more efficient than distance 3
stats.mannwhitneyu(constructed_distance_1_shape_2, constructed_distance_3_shape_2, alternative="less")

# testing difference between distance 2 and 3
# p < 0.05
# distance 2 is more efficient than distance 3
stats.mannwhitneyu(constructed_distance_2_shape_2, constructed_distance_3_shape_2, alternative="less")


# constants: constructed fire lines, shape 3
# variable: distance

# p < 0.05
# the group means differ significantly
stats.kruskal(constructed_distance_1_shape_3, constructed_distance_2_shape_3,constructed_distance_3_shape_3)

# testing difference between distance 1 and 2
# p < 0.05
# distance 1 is more efficient than distance 2
stats.mannwhitneyu(constructed_distance_1_shape_3, constructed_distance_2_shape_3, alternative="less")

# testing difference between distance 1 and 3
# p < 0.05
# distance 1 is more efficient than distance 3
stats.mannwhitneyu(constructed_distance_1_shape_3, constructed_distance_3_shape_3, alternative="less")

# testing difference between distance 2 and 3
# p < 0.05
# distance 2 is more efficient than distance 3
stats.mannwhitneyu(constructed_distance_2_shape_3, constructed_distance_3_shape_3, alternative="less")


"""
    Summary:
    For constructed fire lines of shape 1, the best distances are: 2 > 3 > 1
    For constructed fire lines of shape 2, the best distances are: 1 > 2 > 3
    For constructed fire lines of shape 3, the best distances are: 1 > 2 > 3
"""

# constants: distance 1, temporary lines
# variables: constructed fire line shapes

# testing difference between temporary fire line and
# constructed fire line of shape 1 at distance 1
# p < 0.05
# constructed fire lines with shape 1 < temporary fire line
stats.mannwhitneyu(constructed_distance_1_shape_1, temporary_distance_1, alternative="greater")

# testing difference between temporary fire line and
# constructed fire line of shape 2 at distance 1
# p < 0.05
# constructed fire lines with shape 2 > temporary fire line
stats.mannwhitneyu(constructed_distance_1_shape_2, temporary_distance_1, alternative="less")

# testing difference between temporary fire line and
# constructed fire line of shape 3 at distance 1
# p < 0.05
# constructed fire lines with shape 3 < temporary fire line
stats.mannwhitneyu(constructed_distance_1_shape_3, temporary_distance_1, alternative="greater")


# constants: distance 2, temporary lines
# variables: constructed fire line shapes

# testing difference between temporary fire line and
# constructed fire line of shape 1 at distance 2
# p < 0.05
# constructed fire lines with shape 1 > temporary fire line
stats.mannwhitneyu(constructed_distance_2_shape_1, temporary_distance_2, alternative="less")

# testing difference between temporary fire line and
# constructed fire line of shape 2 at distance 2
# p < 0.05
# constructed fire lines with shape 2 > temporary fire line
stats.mannwhitneyu(constructed_distance_2_shape_2, temporary_distance_2, alternative="less")

# testing difference between temporary fire line and
# constructed fire line of shape 3 at distance 2
# p < 0.05
# constructed fire lines with shape 2 > temporary fire line
stats.mannwhitneyu(constructed_distance_2_shape_3, temporary_distance_2, alternative="less")


# constants: distance 2, temporary lines
# variables: constructed fire line shapes

# testing difference between temporary fire line and
# constructed fire line of shape 1 at distance 3
# p < 0.05
# constructed fire lines with shape 2 > temporary fire line
stats.mannwhitneyu(constructed_distance_3_shape_1, temporary_distance_3, alternative="less")

# testing difference between temporary fire line and
# constructed fire line of shape 2 at distance 3
# p < 0.05
# constructed fire lines with shape 2 > temporary fire line
stats.mannwhitneyu(constructed_distance_3_shape_2, temporary_distance_3, alternative="less")

# testing difference between temporary fire line and
# constructed fire line of shape 3 at distance 3
# p < 0.05
# constructed fire lines with shape 2 > temporary fire line
stats.mannwhitneyu(constructed_distance_3_shape_3, temporary_distance_3, alternative="less")


"""
    Summary:
    At distance 1, the constructed fire lines with shapes 2 > temporary lines.
    At distance 1, the temporary lines > constructed lines of shape 1 and 3
    At distance 2, the constructed fire lines of all shapes > temporary lines.
    At distance 3, the constructed fire lines of all shapes > temporary lines.
"""

# constants: no fire lines, distance 1
# variables: shapes

# testing difference between no fire lines and shape 1
# p < 0.05
# no fire lines is worse than constructed fire lines with shape 1
stats.mannwhitneyu(noFireLine, constructed_distance_1_shape_1, alternative="greater")

# testing difference between no fire lines and shape 2
# p < 0.05
# no fire lines is worse than constructed fire lines with shape 2
stats.mannwhitneyu(noFireLine, constructed_distance_1_shape_2, alternative="greater")

# testing difference between no fire lines and shape 3
# p < 0.05
# no fire lines is worse than constructed fire lines with shape 3
stats.mannwhitneyu(noFireLine, constructed_distance_1_shape_3, alternative="greater")


# constants: no fire lines, distance 2
# variables: shapes

# testing difference between no fire lines and shape 1
# p < 0.05
# no fire lines is worse than constructed fire lines with shape 1
stats.mannwhitneyu(noFireLine, constructed_distance_2_shape_1, alternative="greater")

# testing difference between no fire lines and shape 2
# p < 0.05
# no fire lines is worse than constructed fire lines with shape 2
stats.mannwhitneyu(noFireLine, constructed_distance_2_shape_2, alternative="greater")

# testing difference between no fire lines and shape 3
# p < 0.05
# no fire lines is worse than constructed fire lines with shape 3
stats.mannwhitneyu(noFireLine, constructed_distance_2_shape_3, alternative="greater")


# # constants: no fire lines, distance 3
# # variables: shapes

# testing difference between no fire lines and shape 1
# p < 0.05
# no fire lines is worse than constructed fire lines with shape 1
stats.mannwhitneyu(noFireLine, constructed_distance_3_shape_1, alternative="greater")

# testing difference between no fire lines and shape 2
# p < 0.05
# no fire lines is worse than constructed fire lines with shape 2
stats.mannwhitneyu(noFireLine, constructed_distance_3_shape_2, alternative="greater")

# testing difference between no fire lines and shape 3
# p < 0.05
# no fire lines is worse than constructed fire lines with shape 3
stats.mannwhitneyu(noFireLine, constructed_distance_3_shape_3, alternative="greater")


# constants: no fire lines, temporary fire lines
# variables: distance

# testing difference between no fire lines and distance 1
# p < 0.05
# no fire is worse than temporary fire lines at distance 1
stats.mannwhitneyu(noFireLine, temporary_distance_1, alternative="greater")

# testing difference between no fire lines and distance 2
# p > 0.05
# no fire is worse than temporary fire lines at distance 2
stats.mannwhitneyu(noFireLine, temporary_distance_2, alternative="greater")

# testing difference between no fire lines and distance 2
# p < 0.05
# no fire is worse than temporary fire lines at distance 3
stats.mannwhitneyu(noFireLine, temporary_distance_3, alternative="greater")

"""
    Summary:
    Constructed Fire lines are always better than no fire lines
    Temporary fire lines are always better than no fire lines
"""
