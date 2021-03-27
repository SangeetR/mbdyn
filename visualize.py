import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

output_path = r"C:\Users\DELL\Desktop\sync\mbdyn\output\free_fall_under_force.mov"
ffd = pd.read_csv(output_path, sep=" ", names=["node_no", "x", "y", "z", "eular_x", "eular_y", "eular_z", "vx", "vy", "vz", "wx", "wy", "wz"])
t = [x for x in range(1001)]

#started to plot graph
# we have 3 coordinates x, y, z   
# sns.lineplot(x=t,y=ffd['x']) # Uncomment this line to get graph of x-coordinate with time 
sns.lineplot(x=t,y=ffd['y'])   # comment this if you don't want graph of y-coordinate
# sns.lineplot(x=t,y=ffd['z']) # Uncomment this line to get graph of z-coordinate with time

#Please avoid to plot x and z at same time the will coincide 
plt.show()