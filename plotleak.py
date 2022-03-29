import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('GC.csv',usecols=['Total leak SS1+SS2 [kg/d]','C6F14 concentration in Tracker [g]', 'isNewFlag'])
df.plot(x='Total leak SS1+SS2 [kg/d]',y='C6F14 concentration in Tracker [g]', kind='scatter')
leak = []
concentration = []


isNew = []
newleak = []
newconcentration = []


for i in df.to_numpy():
        print(i)
        leak.append(i[0])
        concentration.append(i[1])
        isNew.append(i[2])
        if i[2] > 0: ## these are the new ones, fill their own lists
            newleak.append(i[0])
            newconcentration.append(i[1])            

plt.plot(leak,concentration,'bo')
plt.plot(newleak,newconcentration,'ro')

p=np.polyfit(leak,concentration,1)
predict = np.poly1d(p)
leak_predicted = []
concentration_predicted = []

for step in range(30):
        leak_predicted.append(-step)
for ileak in leak_predicted:
        concentration_predicted.append(predict(ileak))

# repeat for the newest set of points
nleak_predicted = []
nconcentration_predicted = []

#for step in range(26,30):
#        nleak_predicted.append(-step)
#for ileak in nleak_predicted:
#        nconcentration_predicted.append(predict(ileak))

print("plot black")

plt.plot(leak_predicted, concentration_predicted, c='purple')
#print("plot purple")
#plt.plot(nleak_predicted, nconcentration_predicted, c='purple')

plt.show()