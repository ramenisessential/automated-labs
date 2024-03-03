import math
import matplotlib.pyplot as plt

voltages = [11.6, 15.1, 11.2, 12.4, 14.2, 12.6, 16.8, 13.4, 10.7, 11.3]
radii = [250, 535, 460, 520, 500, 380, 460, 425, 360, 365]
oilcharges = []
masses = []
# since radii are in nm, we need to convert them

print("radii : \n")

for i in range(len(radii)):
    radius = int(radii[i])*10**(-9)
    radii[i]=radius
    print(f"  {radius: .4e}")

print("\nmasses : \n")

for i in range(len(radii)):
    mass = ((4/3*math.pi*(radii[i])**3))*900
    masses.append(mass)
    print(f"  {mass: .4e}")

print("\noil charges : \n")

for i in range(len(radii)):
    chargeoil = ((masses[i])*10*0.003)/voltages[i]
    oilcharges.append(chargeoil)
    print(f"  {chargeoil: .4e}")

# the following figures are named after what their axis represent: x-y
plt.scatter(oilcharges, masses)
plt.savefig("oilcharges-masses")
plt.clf()
plt.scatter(oilcharges, radii)
plt.savefig("oilcharges-radii")