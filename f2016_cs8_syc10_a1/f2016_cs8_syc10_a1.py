# name       : Spencer Chen
# email      : syc10@pitt.edu
# date       : 09/30/2016
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Assignment #1
#
# Notes:
# In the comments, I tried to describe what I intended the for following line to do.

#Ask the user for preferred system of input, choices being "USC" or "Metric" as strings
Unit = input("USC or Metric? ")
#If the user inputs "USC" as the measurement system, it will run the following code
if Unit == "USC":
#Ask user for distance in miles, assign to variable Distance as a float
    Distance = float(input("Distance driven in miles? "))
#Ask user for gas used in gallons, assign to varible Gas as a float
    Gas = float(input("Gasoline used in gallons? "))
#Calculate distance in kilometers by using Distance, assign to variable Distance_Metric. Answer will be a float
    Distance_Metric = Distance * 1.60934
#Calculate volume of gas in liters by using Gas, assign to variable Gas_Metric. Answer will be a float
    Gas_Metric = Gas * 3.78541
#Alternatively, if the user inputs "Metric" as the measurement system, it will run the following code
#I tried to account for errors by allowing both "Metric" and "metric" to work
elif Unit == "Metric" or Unit == "metric":
#Ask the user for distance in kilometers, assign to variable Distance_Metric as a float
    Distance_Metric = float(input("Distance driven in km? "))
#Ask the user for gas used in liters, assign to variable Gas_Metric as a float
    Gas_Metric = float(input("Gasoline used in liters? "))
#Calculate distance in miles by using Distance_Metric, assign to variable Distance. Answer will be a float
    Distance = Distance_Metric * 0.621371
#Calculate volume of gas in gallons by using Gas_Metric, assign to variable Gas. Answer will be a float
    Gas = Gas_Metric * 0.264172
#Exit the "if...elif" structure
#Calculate USC consumption by dividing Distance by Gas, assign to variable Consumption. Answer will be a float
Consumption = Distance / Gas
#Calculate metric consumption by multiplying Gas_Metric by 100, then dividing the product by Distance_Metric
#Answer will be assigned to cm and will be a float
cm = (Gas_Metric * 100)/ Distance_Metric

#compare cm value to given scale
#check if cm is larger than 20
if cm > 20:
#if so, assign "Extremely Poor" to variable Rating
    Rating = "Extremely Poor"
#check if cm is larger than 15. Since anything larger than 20 was already ruled out, this checks for 15>cm>=20
elif cm >15:
#if so, assign "Poor" to variable Rating
    Rating = "Poor"
#check if cm is larger than 10. Since anything larger than 15 was already ruled out, this checks for 10>cm>=15
elif cm > 10:
#if so, assign "Average" to variable Rating
    Rating = "Average"
#check if cm is larger than 8. Since anything larger than 10 was already ruled out, this checks for 8>cm>=10
elif cm > 8:
#if so, assign "Good" to variable Rating
    Rating = "Good"
#Anything else should be less or equal to 8, so assign "Excellent" to variable Rating
else:
    Rating = "Excellent"
#Here it goes...printing the results
#I lined up the columns using tabs and spaces
print("\t\t\t\t\t\t\t   USC\t\t\t   Metric\n"
#I printed both USC distance and metric distance with an accuracy of 3
#The width was 10 (6 digits + 1 decimal point + 3 decimal places). I then labelled with units
      "Distance _____________ :" + format(Distance, '10.3f') + " miles   " + \
      format (Distance_Metric, '10.3f') + " Km\n"\
#I did a similar thing for USC gas and metric gas
      "Gas __________________ :" + format(Gas, '10.3f') + " gallons " + \
      format (Gas_Metric, '10.3f') + " Liters\n"\
#I did a similar thing for USC consumption and metric consumption
      "Consumption __________ :" + format(Consumption, '10.3f') + " mpg     " + \
      format (cm, '10.3f') + " 1/100Km\n\n"\
#I finally printed the gas consumption rating
      "Gas Consumption Rating : " + Rating)


