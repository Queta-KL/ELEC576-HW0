import matplotlib.pyplot as plt

def figureGrayCode(n:int):
    binaryGrayCode=[0,1]
    for i in range(1,n):
        binaryGrayCode.extend([(1<<i)+x for x in binaryGrayCode[::-1]])
    plt.plot(range(1<<n),binaryGrayCode,'o-')
    plt.xlim(0,(1<<n)-1)
    plt.ylim(0,(1<<n)-1)
    plt.xlabel(r'%d-bit uint $n$'%n)
    plt.ylabel(r'Gray($n$)')
    plt.title('Gray code mapping of %d-bit unsigned integer'%n)
    plt.show()
    pass
