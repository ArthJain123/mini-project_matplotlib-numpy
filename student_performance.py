import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)

subject = np.array(["Maths","Science","English"])
plt.xlabel("Name of subjects")

unit = np.random.randint(25,70,(100,3)) 
mid  = np.random.randint(25,80,(100,3)) 
final= np.random.randint(25,100,(100,3)) 

# average marks per student

unit_avg = np.mean(unit,axis = 1)

unit_avg_sub = np.mean(unit,axis = 0)
x = np.sum(unit_avg_sub)

mid_avg = np.mean(mid,axis = 1)

mid_avg_sub = np.mean(mid,axis = 0)
y = np.sum(mid_avg_sub)

final_avg = np.mean(final,axis = 1)

final_avg_sub = np.mean(final,axis = 0)
z = np.sum(final_avg_sub)
plt.ylabel("Average number of each subject")

py_li =[]
py_li.append(x)
py_li.append(y)
py_li.append(z)

plt.title("Subject-wise Final Exam Average",fontsize =15)

plt.bar(subject,final_avg_sub,color = ["skyblue","pink","lightgreen"],width = 0.5,edgecolor = "black",linestyle = ":",linewidth = 1,label = "Final_exam")
plt.legend()
plt.show()

plt.title("Mid Term vs Final Performance",fontsize = 15)
plt.xlabel("Average number of Final exam")
plt.ylabel("Average number of Mid exam")

plt.scatter(final_avg_sub,mid_avg_sub,color = "green",sizes = [80])
plt.plot(final_avg_sub,mid_avg_sub,color = "green",linestyle = ":")
plt.show()

plt.title("Final Exam Marks Distribution",fontsize = 15)
plt.xlabel("Average number of each student of Final exam")
plt.ylabel("Frequency of final exam")

plt.hist(final_avg,color = "lightgreen",edgecolor = "black",linestyle = ":",linewidth = 1,rwidth = 0.9,bins = [20,30,40,50,60,70,80,90])
plt.show()

plt.title("Performance Trend",fontsize = 15)

plt.pie(py_li,colors = ["skyblue","lightgreen","pink"],labels = ["Unit test","Mid exam","Final exam"],autopct = "%0.1f%%")
plt.show()
