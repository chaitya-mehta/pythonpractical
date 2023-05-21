# Write a program to read n integers from the keyboard and store them into a file total.txtfile, separate odd and even numbers and store them in odd.txt and even.txt file. Display the content of all three files.

length = int(input("Enter Total Number: "))
f = open("total.txt", 'w+')
fo = open("odd.txt", 'w+')
fe = open("even.txt", 'w+')
for n in range(0, length):
    a = input("Enter the number: ")
    f.write(a)
    a = int(a)
    if a % 2 == 0:
        fe.write(str(a))
    else:
        fo.write(str(a))
f.close()
fo.close()
fe.close()