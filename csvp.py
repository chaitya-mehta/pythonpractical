# # import csv
# # with open ('people.csv','w',newline='') as file :
# #     writer=csv.writer(file)
# #     writer.writerow(["SN", "Enrollment_No.", "Name"])
# #     writer.writerow([1, "190630116001", "ASTHANA SANDEEP"])
# #     writer.writerow([2, "190630116002", "AVAIYA RAHIL"])
# import csv
# # my data rows as dictionary objects
# mydict =[{'branch': 'COE', 'cgpa': '9.0', 
#           'name': 'Nikhil', 'year': '2'},
#         {'branch': 'COE', 'cgpa': '9.1', 
#          'name': 'Sanchit', 'year': '2'},
#         {'branch': 'IT', 'cgpa': '9.3', 
#          'name': 'Aditya', 'year': '2'},
#         {'branch': 'SE', 'cgpa': '9.5', 
#          'name': 'Sagar', 'year': '1'},
#         {'branch': 'MCE', 'cgpa': '7.8', 
#          'name': 'Prateek', 'year': '3'},
#         {'branch': 'EP', 'cgpa': '9.1', 
#          'name': 'Sahil', 'year': '2'}]
# fields = ['name', 'branch', 'year', 'cgpa']
#  # name of csv file
# filename = "people.csv"
#  # writing to csv file
# with open(filename, 'w') as csvfile:
#  # creating a csv dict writer object
#  writer = csv.DictWriter(csvfile, fieldnames = fields)
#  # writing headers (field names)
#  writer.writeheader()
#  # writing data rows
#  writer.writerows(mydict)
# import pickle  
# my_list = [11, 'Python', 'bLove Python'] 
# # Pickling 
# with open("data.pickle","wb") as file_handle: 
#     pickle.dump(my_list,file_handle,pickle.HIGHEST_PROTOCOL) 
# print("Pickling completed!") 
import pickle 
# Pickling 
with open("data.pickle","rb") as file_handle: 
    retrieved_data = pickle.load(file_handle) 
print(retrieved_data) 
