# import matplotlib
# print(matplotlib.__version__) # 3.10.7
import matplotlib.pyplot as plt
import numpy as np 
# creating basic plot using python lists 
# x = [2023,2024,2025,2026]
# y = [38,40,57,68]
# plt.plot(x,y)
# plt.show()
# creating basic plot using numpy arrays becuse they are faster 
# a = np.array([2023,2024,2025,2026])
# b = np.array([38,40,57,68])
# plt.plot(a,b)
# plt.show()
# markers in matplot
# x = [2023,2024,2025,2026]
# y = [38,40,57,68]
# plt.plot(x,y,marker="." )
# plt.show()
# changing the color of the marker 
x = [2023,2024,2025,2026]
y = [38,40,57,68]
plt.title("Class sizes")
plt.plot(x,y,marker=".",markersize=20,markerfacecolor="cyan")
plt.show()

x = [2023,2024,2025,2026]
y = [38,40,57,68]
plt.title("Class sizes",
          fontsize=20,
          family ="arial",
          color="red")
plt.plot(x,y,marker=".",markersize=20,markerfacecolor="cyan")
plt.show()