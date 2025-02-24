import plotly.express as px
from die import Die

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

fig = px.bar(x=poss_results, y=frequencies)
title = "Results of Rolling a D6 and a D10 50000 Times"
lables = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=lables)

fig.update_layout(xaxis_dtick=1)

fig.show()
fig.write_html('test_d6d10.html')
