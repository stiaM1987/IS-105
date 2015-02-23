#Set the car variable to 100
cars = 100
#Set the space in the car variable to 4.0
space_in_car = 4.0
#Set driver variable to 30
drivers = 30
#Passenger variable
passengers = 90

#cars not driven variable to cars variable - driver variable
cars_not_driven = cars - drivers
#cars driven = drivers variable
cars_driven = drivers
#Carpool variable
carpool_capacity =  cars_driven * space_in_car
#passengers / cars driven = the value of appc variable.
average_passenger_per_car = passengers  / cars_driven

print "There are", cars, "cars aviable."
print "There are only", drivers, "drivers aviable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passenger_per_car, "in each car."

