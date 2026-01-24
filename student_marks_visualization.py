import numpy as np
import matplotlib.pyplot as plt

plt.title("Student Performance on the basics of number of student and average marks",fontsize = 10, color ="red")

np.random.seed(2)

study_hours = np.random.randint(1,5,size = 100)

atten = np.random.randint(20,30,size = 100)

sub_marks = np.array([
    [78, 85, 74], [65, 70, 60], [90, 92, 88], [55, 48, 52], [82, 79, 85],
    [40, 42, 38], [72, 75, 70], [88, 90, 92], [60, 58, 62], [95, 94, 96],
    [68, 65, 70], [45, 50, 48], [76, 80, 78], [33, 35, 30], [84, 82, 80],
    [71, 69, 73], [59, 61, 60], [91, 89, 93], [47, 44, 46], [66, 68, 64],
    [88, 85, 90], [54, 56, 52], [79, 77, 81], [62, 60, 58], [86, 88, 84],
    [49, 45, 50], [73, 75, 78], [92, 90, 94], [35, 38, 40], [67, 65, 69],
    [81, 83, 85], [58, 55, 60], [74, 72, 70], [90, 88, 92], [44, 42, 46],
    [69, 71, 68], [77, 79, 76], [52, 50, 54], [85, 87, 89], [63, 61, 65],
    [48, 46, 44], [70, 73, 75], [91, 93, 95], [56, 58, 54], [82, 80, 78],
    [64, 66, 62], [39, 41, 43], [76, 78, 80], [88, 86, 90], [57, 59, 55],
    [72, 74, 76], [84, 82, 86], [60, 62, 58], [45, 47, 43], [90, 92, 88],
    [68, 70, 66], [52, 54, 50], [79, 81, 83], [61, 63, 65], [87, 89, 85],
    [34, 36, 38], [75, 77, 79], [92, 94, 96], [58, 56, 60], [83, 81, 85],
    [66, 64, 68], [49, 51, 47], [71, 73, 75], [89, 87, 91], [55, 57, 53],
    [78, 76, 80], [62, 60, 64], [85, 83, 87], [41, 43, 45], [74, 72, 76],
    [90, 88, 92], [59, 61, 57], [67, 69, 65], [82, 84, 86], [54, 52, 56],
    [76, 78, 74], [88, 90, 86], [63, 65, 61], [47, 49, 45], [91, 93, 89],
    [70, 68, 72], [56, 58, 54], [84, 86, 82], [60, 62, 58], [73, 75, 71],
    [77, 79, 75], [64, 66, 62], [88, 90, 92], [53, 55, 51], [81, 83, 85],
    [46, 48, 44], [72, 74, 76], [90, 92, 88], [58, 60, 56], [69, 71, 73],
])



avg_stu = np.mean(sub_marks,axis = 1)
plt.ylabel("Average marks")

Pass = np.sum(avg_stu>=42)
Fail = np.sum(avg_stu<42)
pie_li = []
pie_li.append(Pass)
pie_li.append(Fail)

sr_no = np.arange(1,101)
plt.xlabel("Number of student")

plt.bar(sr_no,avg_stu,color = "skyblue",edgecolor = "black",linestyle = ":",linewidth = 0.5,label = "Average_number_of_each_student")
plt.legend()
plt.show()

plt.title("Student Performance on the basics of study hours and average marks",fontsize = 10, color ="red")
plt.xlabel("Study hours of each student")
plt.ylabel("Average marks of each student")

plt.scatter(study_hours,avg_stu,color = "pink",marker = "s",edgecolor ="black",linewidth = 0.5)
plt.show()

plt.title("Distribution of Average Marks of each student",fontsize = 15,color ="red")
plt.xlabel("Average marks of each student")
plt.ylabel("Frequency of graph from 0")

plt.hist(avg_stu,bins = [40,50,60,70,80,90],color = "lightgreen",edgecolor = "black",linestyle = ":",linewidth = 0.5,rwidth = 0.8)
plt.show()

plt.title("Pass vs Fail",fontsize = 15,color= "red")

plt.pie(pie_li,colors = ["pink","skyblue"],labels = ["Pass","Fail"],rotatelabels = True,autopct = "%0.1f%%",shadow = True,pctdistance = 0.4,textprops = {"fontsize":9})
plt.show()
