l1=['chaitya','abhi','smit']
l2=[1,2,3]
#method 1
d=dict(zip(l2,l1))
print(d)
#method 2
a=dict(map(reversed,d.items()))
print(a)