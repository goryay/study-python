import plotly.express as px
from die import Die

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

fig = px.bar(x=poss_results, y=frequencies)
title = "Results of Rolling One D6 1000 Times"
lables = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=lables)
fig.show()
