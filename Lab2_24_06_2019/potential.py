import math
import numpy as np
import matplotlib.pyplot as plt

# Cutoff Vr
maxVr = input("Cutoff value ::")


# Discuss about infinity

def getPotential():
    global maxVr
    
    # welcomeFile = open("welcome", "r")
    
    # Inputs

    startX  = float(input("1. Enter starting value of 'r' ::"))
    endX    = float(input("2. End value of 'r' ::"))
    step    = float(input("3. Step size ::"))
    sigma   = float(input("4. Sigma ::"))
    epsilon = float(input("5. episilon ::"))
#    nu      = float(input("6. neu :: "))
    lam     = float(input("6. lam ::"))
    

    # calculations
    r = np.arange(startX,endX,step)
    
    lj = lennardJone(r,epsilon,sigma)
    swp = squareWellPotential(r,epsilon,sigma,lam)
    ss1 = softSphere(r,epsilon,sigma,1)
    ss10 =  softSphere(r,epsilon,sigma,10)

    print(lj)
    print(swp)
    print(ss1)
    print(ss10)

    # Writing Data to a csv file 
    config = np.array([maxVr,startX,endX,step,sigma,epsilon,lam])
    
    np.savetxt("Config",config)
    np.savetxt("Lennard Jones",np.array([r,lj]).transpose())
    np.savetxt("Square well potential",np.array([r,swp]).transpose())
    np.savetxt("Soft Sphere 1",np.array([r,ss1]).transpose())
    
    np.savetxt("Soft Sphere 10",np.array([r,ss10]).transpose())
    # Generating Graph
    
    fig , axs = plt.subplots(3,sharex=True)
    

    axs[0].plot(r,lj)
    axs[0].set_title("Lennard Jones Potential ("+ str(epsilon) + "," + str(sigma) + ")")


    axs[1].plot(r,swp)
    axs[1].set_title("Square Wave Potential ("+ str(epsilon) + "," + str(sigma) + "," + str(lam) + ")")
    
    axs[2].plot(r,ss1,label="nue = 1")
    axs[2].set_title("Soft Sphere Potential ("+ str(epsilon) + "," + str(sigma) + ")")
    axs[2].plot(r,ss10,'r',label="nue = 10")
    
    plt.legend()

    
    for ax in axs.flat:
        ax.set(ylabel='Potential Kj/mol', xlabel='Distance (Angstrom)')
    
    plt.show()

def lennardJone(r,epsilon,sigma):
    potential = np.minimum(maxVr,4.0*epsilon*((sigma/r)**12 - (sigma/r)**6))
    return potential

def squareWellPotential(r,epsilon,sigma,lam):
    global maxVr

    potential = np.zeros(r.shape[0])
    
    for x in range(0,r.shape[0]):
        if(r[x] < sigma):
            potential[x] = maxVr
        elif ( r[x] >= sigma and r[x] < lam*sigma):
            potential[x] = -1.0*epsilon
        else : 
            potential[x] = 0 
    return potential

def softSphere(r,epsilon,sigma,nu):
    global maxVr
    potential =  np.minimum(maxVr,epsilon*(sigma/r)**nu)
    return potential
    

getPotential()    
