import matplotlib.pyplot as plt

cubes = [1, 8, 27, 64, 125]
fig , ax = plt.subplots()
ax.plot(cubes, linewidth=3)

ax.set_title('Cubes Number', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

ax.tick_params(labelsize=14)

plt.show()