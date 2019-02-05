def count_sheep(n):
    murmur=''
    for i in range(n):
        murmur = murmur+(str(i+1)+" sheep...")
    return murmur
