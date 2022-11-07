
import numpy as np
import matplotlib.pyplot as plt


totalMass = 1
dryMass = 0.728
burnTime = 2.1 #klima d9 e7 engine
totalImpulse = 19.6
propellantMass = 0.0282


averageThrust = totalImpulse/burnTime
massFlowRate = propellantMass/burnTime

time = np.linspace(0, 10, 100, False)

index = int(np.where(time==burnTime)[0] + 1)
thrust = np.append(np.repeat(averageThrust, index), np.repeat(0, len(time) - index))
mass = np.append(np.repeat(totalMass, index) - time[0:index] * massFlowRate, np.repeat(dryMass, len(time) - index))


acceleration = thrust/mass - 9.81

plt.style.use('dark_background')
plt.plot(time, acceleration)
plt.ylabel("Acceleration")
plt.xlabel("Time")
plt.show()


def integrateGraph(time, array):
    pass
    resArray = [0]
    for n in range(0, len(time)-1):
        resArray.append(
        resArray[-1] + 0.5*(array[n+1] + array[n])*(time[n+1] -
        time[n])
    )
    return np.array(resArray)