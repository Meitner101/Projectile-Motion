import matplotlib.pyplot as plt
import numpy as np
try:
    initial_vel = int(input("Enter a initial Velocity:"))
    angle_deg = int(input("Enter a angle of projection:"))
except ValueError:
    print("Enter a valid number")
    

g = 9.8

angle_rad = np.radians(angle_deg)

time_of_flight = (2*initial_vel*np.sin(angle_rad))/g


t = np.linspace(0, time_of_flight, num=100)
x = initial_vel * np.cos(angle_rad) * t
y = initial_vel * np.sin(angle_rad) * t - 0.5 * g * t**2

plt.figure(figsize=(10,5))
plt.plot(x, y, label='Projectile Path', color='blue', linewidth=2)    
plt.title("Projectile Motion Path")
plt.xlabel("Horizontal Range")
plt.ylabel("Maximum height")
plt.grid(True)
plt.legend()
plt.show()