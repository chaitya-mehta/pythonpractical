# Write a program to find reciprocal of the elements of list [12,0, ‟a‟,20,‟hi‟] withException handling.

class AlphaException(Exception):
    pass

l = [12,0, 'a',20,'hi']
for n in l:
    n = str(n)
    try:
        if n.isalpha():
            raise AlphaException
        elif n == 0:
            raise ZeroDivisionError()
        else:
            n = int(n)
            print("reciprocal of", n, "is 1 /", n, "=", 1/n)
    except ZeroDivisionError:
        print("Can not define 0's reciprocal.")
    except AlphaException:
        print("Can not find alpha letters reciprocal.")
