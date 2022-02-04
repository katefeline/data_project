import matplotlib.pyplot as plt
plt.style.use('seaborn')

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c='green')

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([-100, 1100, -100, 1100000])

plt.show()