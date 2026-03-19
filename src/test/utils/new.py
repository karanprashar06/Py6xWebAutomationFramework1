n= int(input("Enter the number"))


def fibonachi(n):

    if n<=1:
        return n
    else:
        return fibonachi(n-1)+fibonachi(n-2)


    #
    # a =0,
    # b=1
    # for i in range(n):
    #     print(a, end=' ')
    #     a,b = b,a+b


for i in range(n):
    print(fibonachi(i),end=" ")