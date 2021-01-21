# Stralend

Course: Project Computational Science, University of Amsterdam

Authors: Esmée van der Mark, Emma Kok, Tamara Stoof

Group: Stralend

Date: 26-01-2021

This repository consists of a number of files. Three python files and 13 txt files. The .txt files contain the data that was used in the statistics.py and visualisation.py files. The dat ain the txt files were created using the CA_Dumai_forest_fires.py file. As the simulation of the forest fires in the latter file makes uses of probability, the values will always be different between any number of runs. Therefore, to ensure that others can reproduce our exact figures, the data from the CA_Dumai_forest_fires.py file was stored separately. 

The CA_Dumai_forest_fires.py file contains the code that was used to construct a two dimensionsal cellular automaton that can simulate a forest fire in Dumai based on the paper of Mutthulakshmi et al. (2020). This CA makes use of Moore neighborhoods and the state of the cells depend on the vegetation types and density, as well as whether or not a cell is burning or has already been burnt to the ground. Burnt down areas, as well as city areas and areas outside of the area of interest cannot burn. Whether or not a cell can burn also depends on the probability of a neighbouring cell causing the cell to catch a flame. This burning probability depends on the vegation types and density, as well as the wind speed and direction. The location of the burning neighbouring cell relative to the cell is therefore an important factor that influences a neighbouring cell's chances of setting the cell ablaze.  
The CA_Dumai_forest_fires.py file tests the efficiency of numerous mitigation methods to stop the forest fire propagation front. Two main mitigation methods were used: constructed fire lines and temporary fire lines. The difference between the two lies in the fact that constructed fire lines, once initialized, will remain in the grid, while temporary fire lines will be removed affter several time steps. The type of fire lines used can be chosen on line 102. If you want to turn of the fire lines altogether, you can set the variable noFireLines on line 97 to 1.
Withing the two methods, we have further divided the fire lines based on distance from the fire propagation front. The constructed and temporary fire lines can be placed on three different distances. The distance can be changed at line 109 or 115 for the temporary and constructed fire lines respectively. In addition to distance, we have created three different types of shapes the constructed fire lines can be: a triangle, a square or a straight line (similar to the temporary fire line, but permanent). The shape of the constructed fire lines can be changed on line 121. 

The CA_Dumai_forest_fires.py file computes the fraction of burnt cells at the end of a simulation run  (14 time steps/2 weeks) and adds it to a list. You can manually change how many simulation runs you want to run (and thus the size of your fraction burtn data) by changing the repeats variable on line 133. The final list containing the final burnt fractions for all n simulation runs will be automatically appened to a txt file depending on which combination of fire lines, distances, and shapes were used to run the simulation. 


To reproduce the same statistics and figures as was shown in our report and poster presentation, you should use the txt files in this repository. Simply run either the statistics.py file or the visualisation.py file. The visualisation.py can be run without any further adjustments and it will produce the figures (i.e. figures.......) we have used. The statistics.py file contains all the codes, but no print statements. If you want to find the p-value of one of the tests, you should add the print statement manually. However, the p-value (either p < 0.05 or p > 0.05) of each test is added as a comment to ensure you don't have to. 
The statistics.py file first loads the data from all the txt files and stores them in variables. These variables are subsequently tested for normallity. All variables were non-Gaussian, so we made use of two non-parametric tests, the Kruskal-Wallis test and the Wilcoxon-Mann-Whitney test. These tests are used to compare whether there is a significant difference in the mean of 2 (Wilcoxon-Mann-Whitney) or more (Kruskal-Wallis) groups. The latter test only tells you if one of the groups differs from the others, but does not say which one is different. That's why the Wilcoxon-Mann-Whitney test was used. If the p-value of one of the tests was less than 0.05, then there was a significant difference.
Lastly, the Wilcoxon-Mann-Whitney test offers an option to specify whether to use a one-side (both sides) or a two-sided test. We have chosen the type of alternative hypothesis based on findings drom the paper of Mutthulakshmi et al. (2020). The comments in the statistics.py file should provide sufficient information to interpret the findings.


Modules that were used in this project:
matplotlib.pyplot
numpy
random
math
ijson
pylab
scipy.stats
seaborn


Version of python used and the version of the used modules




