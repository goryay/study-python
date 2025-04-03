import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)

    ax.plot(rw.x_values, rw.y_values, linewidth=1, color='blue')

    ax.plot(0, 0, 'go', markersize=8)
    ax.plot(rw.x_values[-1], rw.y_values[-1], 'ro', markersize=8)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Do you want to continue? [y/n]: ")
    if keep_running == 'n':
        break
