"""
Author: Prabha Sapkota

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import from Python Standard Library




# Use \n to add a blank new line to the terminal before we ask for input

plant1_leafnumbers = input("\nEnter the plant1 leafnumbers.")
plant2_leafnumbers = input("\nEnter the plant2 leafnumbers")
number_of_plants = input("\nEnter the total number of plants")

# convert the radius_string to a number
plant1 = int(plant1_leafnumbers)
plant2 = int(plant2_leafnumbers)
plants = int(number_of_plants)

# calculate the minimum and maximum leafnumbers. 
minimum = plant1

if plant2 < minimum:
    minimum = plant2
    maximum = plant1

if plant2 > maximum:
    maximum = plant2    

#calculations
total_leafnumbers = plant1 + plant2
average_leafnumbers = (total_leafnumbers)/ plants
lowest_leafnumbers = minimum
highest_leafnumbers = maximum

#average
average_total_leafnumberes = round(average_leafnumbers)

# log the results
logger.info(f"The total leafnumbers is {total_leafnumbers}.")
logger.info(f"The average leafnumbers per plant is {average_leafnumbers}.")
logger.info(f"The lowest leafnumbers is {lowest_leafnumbers}.")
logger.info(f"The highedt leafnumbers is {highest_leafnumbers}.")


