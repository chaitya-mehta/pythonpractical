#  Write a program to remove empty strings from a list of strings
l=['chaitya','pratham','parth','','']
while('' in l):
    l.remove('')
# for i in l:
#     if(l[i]==''):
#         l.remove('')
print(l)