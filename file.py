# fileptr = open("myfile1.txt","r") 
# if fileptr: 
#     print("file is opened successfully with read mode only") 
#     a=fileptr.readline(3)
#     print(a)
#     # a=fileptr.readline()
#     # print(a)
#     # a=fileptr.readline()
#     # print(a)
# else:
#     print("File Not Opened")
# # fileptr.close()
# f=open("myfile.txt","a")
# print("file opened")
# f.write("hello,fjdbfuebfu")
# f.close()
# f=open("myfile.txt","r")
# print(f.seek(9))
# # print(f.read())
# # f.close()
# import os
# os.remove("myfile.txt")
# f=open("myfile1.txt","r")
# print(f.mode)
# print(f.name)
# print(f.closed)
# f.close()
# print(f.closed)
f=input("Enyter Fils naksq")
num_line=0
num_word=0
num_char=0
try:
    fp=open(f,"r")
        for i in fp:
            wors=i.split()
            num_line+=1
            num_word+=len(wors)
            num_char+=len(i)
    print("Lines = ",num_lines) 
	print("Words = ",num_words) 
	print("Characters = ",num_chars) 
	fp.close() 
except Exception: 
	print("Enter valid filename") 
