import matplotlib.pyplot as plt
import numpy as np

np.random.seed(4)

sub = np.array(["Maths","Science","English"])

marks = np.random.randint(44,98,size = (50,3))
# print(marks)

plt.style.use("default")

avg_stu = np.mean(marks,axis = 1)
# print(avg_stu)

avg_sub = np.mean(marks,axis = 0)
# print(avg_sub)

max_avg = np.max(avg_stu)
print("Highest average score: ",max_avg,"\n")

min_avg = np.min(avg_stu)
print("Lowest average score: ",min_avg,"\n")

total_sum = np.sum(marks,axis = 1)
print("Total sum of 3 subjects for each student:\n ",total_sum,"\n")

sum_max = np.max(total_sum)
print("Highest sum of 3 subjects: ",sum_max,"\n")

sum_min = np.min(total_sum)
print("Lowest sum of 3 subjects: ",sum_min,"\n")

high_num_sub = np.max(marks,axis = 0)
print("Highest score of Maths,Science,English: ",high_num_sub,"\n")


plt.title("Performance of students for each subject",fontsize = 15,color = "green")

plt.xlabel("Names of the subjects")
plt.ylabel("Average number of the each subjects")

plt.bar(sub,avg_sub,color = ["lightgreen","pink","skyblue"],width = 0.5)
plt.show()

plt.title("Journey of the Topper student",fontsize = 15,color = "green")

plt.xlabel("Names of Subjects")
plt.ylabel("Topper student")

plt.plot(sub,high_num_sub,color = "green",marker = "*",markersize = 12)
plt.show()

plt.title("Score distribution",fontsize = 15,color = "green")

plt.xlabel("Average number of each student")
plt.ylabel("Frequency of Average numbers")

x = np.arange(50,91,5)

plt.hist(avg_stu,bins = x,color = "pink",edgecolor = "white",linestyle = "-.",linewidth = 1,rwidth = 0.9)
plt.show()

plt.title("Score comparision by using box plot",fontsize = 15,color = "green")

plt.boxplot(marks,showmeans = True,labels = sub,patch_artist = True,boxprops = dict(facecolor = "pink",alpha = 0.7),whiskerprops = dict(color = "skyblue",linewidth = 2),capprops = dict(color = "skyblue",linewidth = 2),)
plt.show()


plt.title("Pass and Fail comparion",fontsize = 15)

pass_stu = np.sum(total_sum >= 160)

fail_stu = np.sum(total_sum < 160)

x = [pass_stu,fail_stu]

plt.pie(x,colors = ["pink","skyblue"],labels = ["Passed","Failed"],autopct = "%0.1f%%",wedgeprops = dict(edgecolor = "black",linestyle = "-",linewidth = 1))
plt.legend()

pass_percent = (pass_stu / len(total_sum)) * 100
print("Pass Percentage:", pass_percent,"%")


plt.show()
