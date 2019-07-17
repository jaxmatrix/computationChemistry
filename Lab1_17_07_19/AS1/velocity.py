'''

Author : Jai Shukla
Department : Chemistry 
Assignment : 1

'''

import math
import numpy 




# tell the complete or relative address of the file

def readVelocites(fileAddress):
	
	velocity_dat = open(fileAddress,"r")
	velocities = []

	for x in velocity_dat:
		#print(x)
		if x[0]=='#':
			continue
		else:
			tempVal = x.split()
			velocity = numpy.array([float(tempVal[1]),float(tempVal[2]),float(tempVal[3])])
		#	print(velocity)
			velocities.append(velocity)

	return velocities


# We are reading the file velcoity data to check the working of the function 

velocities = readVelocites("../velocity-data")


# Calculate kinectic energy of a single particle 
# Input are the mass of the particle and numpy array of the velocity vector

def kineticEnergy(mass,vector):
	sq = vector**2
	#print(vector,sq)
	sq_sum = sq[0] + sq[2] + sq[2]
	
	return mass*0.5*sq_sum


# Returns sum of energy of all the particle 
# Input velocity array | array of vector containing the velcity of one type of particle and mass of the particular atoms

def totalKineticEnergy(velocities, mass):
	sum = 0
	for velocity in velocities:
		sum += kineticEnergy(1,velocity)
	return sum

print("Total Kinectic Energy of the 10 partilce is :: ",totalKineticEnergy(velocities,1))


# General Routines as given in the program

def generalRoutine_SimilarParticle(mass,velocityDataFileAddress):
	velData = readVelocites(velocityDataFileAddress)	
	return totalKineticEnergy(velData,mass)

def generalRoutine_TwoDifferentParticle(mass1, mass2, velocityDataFile1, velocityDataFile2):
	velData1 = readVelocities(velocityDataFile1);
	velData2 = readVelocities(velocityDataFile2);
	
	return totalKineticEnergy(velData1,mass1) + totalKineticEnergy(velData2,mass2)


