import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

input_file = "csv_pandas/russia_losses_personnel.csv"

data = pd.read_csv(input_file)

data = data.replace(np.nan, 0)
data = data.drop_duplicates()

arr = data['personnel'].values
arrX = list(arr)

arrY = data['day'].values
arrY = list(arrY)

xvalues = arrX

yvalues = arrY

df = pd.DataFrame({'xvalues': xvalues, 'yvalues': yvalues})

fig, ax = plt.subplots(1, 1)
ax.plot('xvalues', 'yvalues', data=df, color='#a10000', label="Personnel losses")

plt.xlabel('Russian military losses')
plt.ylabel('Days')
plt.legend()
plt.title('2022 Russian invasion of Ukraine - Personnel losses')

################################################################


input_file2 = "csv_pandas/russia_losses_equipment.csv"
data2 = pd.read_csv(input_file2)

data2 = data2.replace(np.nan, 0)
data2 = data2.drop_duplicates()

del data2['day']
data2 = data2.max(numeric_only=True)

df2 = pd.DataFrame(data=data2)
df2.plot.bar(label="Equipment losses")
plt.xlabel("System type")
plt.ylabel("Number destroyed")
plt.title('2022 Russian invasion of Ukraine - Equipment losses')
plt.legend().set_visible(False)
plt.subplots_adjust(bottom=0.325)
plt.xticks(rotation=70)
# plt.show()


################################################################


labels = 'aircraft', 'helicopter', 'tank', 'APC', 'field artillery', 'MRL', 'military auto', 'fuel tank', 'drone', 'naval ship', 'anti-aircraft', 'special equipment', 'mobile SRBM'
sizes = list(data2)
fig1, ax1 = plt.subplots()
ax1.pie(sizes)

plt.legend(labels,loc=(1.04,0))
plt.show()
