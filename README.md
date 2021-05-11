# PHSX815_Project4

## Instructions

### Part 1

Use the decay.py file to create Higgs decays. Use "-Nexp " and "-Ndecays " at the command line to specify the number of experiments and number of decays per experiment generated. The user should pipe the output from this program to a text file. 

eg: "python decay.py -Nexp 500 -Ndecays 1000 > data.txt"

### Part 2
To analyze and "measure" these decays, use the analyze.py file. Use "-input " to specify your data file at the command line. This will generate 2 histograms showing examples of measured branching fractions. All the "measured" branching fractions will be printed as output. 

eg: "python analyze.py -input data.txt" 