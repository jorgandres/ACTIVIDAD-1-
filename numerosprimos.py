def primos(n):
        losprimos=[]
        for i in range(2,n):
            if (n%i==0):
                print("")
            else:
                losprimos.append( i)
        return losprimos
    n=9
    print(primos(n))