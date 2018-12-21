#variables provided by Codecademy
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

#function definitions

#converts a temperature in fahrenheit to celcius
def fToC(fTemp):
	cTemp = float((fTemp - 32) * 5/9)
	return cTemp

#converts a temperature in celcius to fahrenheit
def cToF(cTemp):
	fTemp = float((cTemp * 5/9) + 32)
	return fTemp

#calculates the force given the mass and acceleration
def getForce(mass,acceleration):
	return mass*acceleration

#calculates the energy given the mass and a constant (called speedOfLight, but the user could change thing if they wanted)
def getEnergy(mass, speedOfLight = 3*10**8):
	return mass * (speedOfLight**2)

#calculates the work done by an object. Calls the getForce() function to calculate the force.
def get_work(mass,acceleration,distance):
	force = getForce(mass,acceleration)
	workDone = force * distance
	return workDone

#begin output testing to ensure validity

f100_in_celcius = fToC(100)
print(f100_in_celcius)
c0_in_fahrenheit = cToF(0)
print(c0_in_fahrenheit)
forceOfTrain = getForce(train_mass, train_acceleration)
print("The GE train supplies " + str(forceOfTrain) + " Newtons of force.")
bomb_energy = getEnergy(bomb_mass) 
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")
trainWork = get_work(train_mass, train_acceleration,train_distance)
print("The GE train does " + str(trainWork) + " Joules of work over " + str(train_distance) + ".")
