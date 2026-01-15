plt.title("Student Marks Analysis",fontsize = 20,color = "red")

students = np.array(["Arth","Rohan","Priya","Nobita","Sanwal"])
plt.xlabel("Names of all Students")

marks = np.array([90,78,80,45,87])
plt.ylabel("Marks of all students")

highest_marks = np.max(marks)
highest_student = students[marks == np.max(marks)]
print("Higest mark student from this table :",highest_student,"-",highest_marks,"\n")

lowest_marks = np.min(marks)
lowest_student = students[marks == np.min(marks)]
print("Lowest mark student from this table :",lowest_student,"-",lowest_marks,"\n")

avg = np.mean(marks)
print("Average marks of all students from this table :",avg,"\n")

grade = np.where(marks <= 40,"Fail","Pass")
print("Grade Assignment :",grade)


plt.bar(students,marks,color = ["pink","green","purple","violet","skyblue"],edgecolor = "black",linewidth = 0.5,width = 0.5,linestyle = ":",alpha = 0.5,align = "edge")
plt.axhline(40)
plt.show()
