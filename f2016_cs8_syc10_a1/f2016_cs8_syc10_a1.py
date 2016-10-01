# name       : Spencer Chen
# email      : syc10@pitt.edu
# date       : 09/06/2016
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Assignment #1
#
# Notes:
# In the comments, I tried to describe what I intended the for following line to do.

#Ask the user for preferred system of input, choices being "USC" or "Metric" as strings
Unit = input("USC or Metric?")
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


if cm > 20:
    Rating = "Extremely Poor"
elif cm >15:
    Rating = "Poor"
elif cm > 10:
    Rating = "Average"
elif cm > 8:
    Rating = "Good"
else:
    Rating = "Excellent"

print(Distance, Distance_Metric, Gas, Gas_Metric, Consumption, cm, Rating)

#print("Distance" + format(Distance,'.3f') + format(Distance_Metric,'.3f'))


