# Write a program that opens a file and writes data to it. Handle exceptions that can begenerated during the I/O operations.
try:
    f=open('7_a.txt',"a")
    f.write("\nHello Baby ")
    f.close()
except:
    print("Exception Found")