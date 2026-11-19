import numpy as np
import matplotlib.pyplot as plt
name=["khaqan","eyas","bacha","salman","babar","saim","sunny","shayan","abdullah","asad"]
marks=np.random.randint(1,100,10)
plt.hist(marks,bins=[1,20,40,60,80,100],edgecolor="red")
plt.title("student data")
plt.xlabel("range")
plt.ylabel("count")
plt.savefig("student histogram.png")
plt.show()
print(marks)