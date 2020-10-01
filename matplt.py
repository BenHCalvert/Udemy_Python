# Mat Plot Lib Module, used to make charts. to install, in terminal: pip3 install matplotlib

# import the module and name as plt
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1500, 1200, 1100, 1800]
legend = ["January", "February", "March", "April"]
# assign the legend to the x values
plt.xticks(x,legend)

# Plot the x & y coordinates
plt.plot(x,y)
# Show the plot
plt.show()

