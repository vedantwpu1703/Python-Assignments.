#Creating a list
student_list = ["Divyansh","Tanmay","Divy","Rishi","Jainam"]
print("student_list:",student_list)
student_list.append("Parth")
print(student_list)
student_list.remove("Rishi")
print(student_list)
student_list = ["Divyansh","Tanmay","Divy","Rishi","Jainam"]
student_list.pop(1)
print(student_list)
del student_list[3]
print(student_list)
student_list[2] = "Shreya"
print(student_list)



#Creating the Tuple

student_tuple = ["Divyansh","Tanmay","Divy","Rishi","Jainam"]
print("student_tuple:",student_tuple)
y = list(student_tuple)
y.append("Parth")
y.append("Himesh")
y.append("Karan")
student_tuple = tuple(y)
print(student_tuple)
y = ("Riley",)
student_tuple  += y
print(student_tuple)
y = list(student_tuple)
y.remove("Divyansh")
y.remove("Jainam")
student_tuple = tuple(y)
print(student_tuple)

#Creating a Dictionary

student_dict = {1:"Divyansh",2:"Tanmay",3:"Divy",4:"Rishi",5:"Jainam"}
print("student dictionary:",student_dict)
student_dict[6] = "Rohan"
print("after adding Rohan,studeny_dict")
del student_dict[3]
print("after deleting Divy:",student_dict)
student_dict [2] = "Shreya"
print("After updating Shreya:",student_dict)
