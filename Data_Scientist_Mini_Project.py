import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(5)

marks = np.random.randint(35,101,size = (100,5))
# print(marks)

stu_id = np.arange(1,101)

data = pd.DataFrame(dict(ID = stu_id,
                         Math = marks[:,0],
                         Physics = marks[:,1],
                         Chemistry = marks[:,2],
                         IT = marks[:,3],
                         English = marks[:,4]))

total = np.sum(marks,axis = 1)

stu_avg = np.mean(marks,axis = 1)

grade = np.where(stu_avg >= 90,"A",
                 np.where(stu_avg >= 75,"B",
                          np.where(stu_avg >=60,"C"
                          ,np.where(stu_avg >= 50,"D","E"))))
data["Total"] = total

data["Average"] = stu_avg

data["Grade"] = grade

data["Result"] = np.where(stu_avg >50 , "Pass","Fail")
print(data)

sorted_data = data.sort_values(by = "Total",ascending = False)
# print(sorted_data)

top = sorted_data.head()
print("Topper: ",top)

# Each Subject Average
print("Subjects Average: \n",np.mean(marks,axis = 0))

unique,counts = np.unique(data["Grade"],return_counts = True)
print(unique,"\n",counts)


math_max =  data.loc[data["Math"].idxmax()]
print("Highest Score in Maths: \n",math_max,"\n")

physics_max = data.loc[data["Physics"].idxmax()]
print("Highest Score in Physics: \n",physics_max,"\n")

chemistry_max = data.loc[data["Chemistry"].idxmax()]
print("Highest Score in Chemistry: ",chemistry_max,"\n")

it_max = data.loc[data["IT"].idxmax()]
print("Highest Score in It: ",it_max,"\n")

english_max = data.loc[data["English"].idxmax()]
print("Highest Score in English: ",english_max,"\n")



fail_stu = data[data["Average"]<50]
print("Fail Student: \n",fail_stu)

plt.title("Subject Average Chart",fontsize = 20)

sub = ["Maths","Physics","Chemistry","IT","English"]
plt.xlabel("Name of all subjects",fontsize = 12)

sub_avg = np.mean(marks,axis = 0)
plt.ylabel("Average marks of all subjects",fontsize = 15)

plt.bar(sub,sub_avg,color = "skyblue",edgecolor = "black",label = "Students Performance",width = 0.8)
plt.legend()
plt.show()


plt.title("Grade Distribution on Bar Graph",fontsize = 15)

plt.xlabel("All Grades")
plt.ylabel("Frequency of Grades")

plt.bar(unique,counts,color = "pink",edgecolor = "black",width = 0.8,label = "Students Performance")

plt.legend()
plt.show()


plt.title("Grade Distibution on Pie Chart",fontsize = 15)

plt.pie(counts,labels = unique,colors = ["pink","skyblue","lightgreen","yellow"],autopct = "%0.1f%%",wedgeprops = dict(edgecolor = "black"))

plt.legend()
plt.show()

plt.title("Average Marks of all Students",fontsize = 15)

x = np.arange(50,81,5)

plt.xlabel("All Students")
plt.ylabel("Frequency of their Marks")

plt.hist(stu_avg,bins = x,color = "lightgreen",rwidth = 0.9,edgecolor = "black",histtype = "bar")

plt.show()
