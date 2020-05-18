import numpy
import math

def to_bin_array(n, l):
    s=bin(n)[2:]
    if len(s)<l:
        s="0"*(l-len(s))+s
    else:
        s=s[len(s)-l:]
    return [int(x) for x in s]

def get_parity_matrix(message_length, extra=False):
    syndrome=1
    p_col=0
    s_col=0

    no_parity_bits=0
    while 2**no_parity_bits<no_parity_bits+message_length+1:
        no_parity_bits+=1
    
    no_syndrome_rows=math.ceil(math.log2(message_length+no_parity_bits+1))

    if(extra):
        no_parity_bits+=1
        no_syndrome_rows+=1
    syndrome_matrix=numpy.zeros((no_syndrome_rows, message_length))

    for i in range(no_parity_bits+message_length):
        row=list()
        if(extra):
            row=to_bin_array(syndrome, no_syndrome_rows-1)
        else:
            row=to_bin_array(syndrome, no_syndrome_rows)
        
        if syndrome==2**p_col:
            p_col+=1
        else:
            for j in range(len(row)):
                syndrome_matrix[j][s_col]=row[j]
            s_col+=1
        syndrome+=1
    
    if(extra):
        for i in range(message_length):
            syndrome_matrix[no_syndrome_rows-1][i]=1

    return syndrome_matrix

def encode(message):
    msg=numpy.array([message])
    #print(msg)

    A=get_parity_matrix(len(message)).transpose()
    #print(A,A.shape)

    G=numpy.zeros((A.shape[0], sum(A.shape)))
    #print(G.shape)

    for i in range(G.shape[0]):
        for j in range(G.shape[1]):
            if j>=A.shape[1]:
                G[i][j]=i==j-A.shape[1]
            else:
                G[i][j]=A[i][j]
    #print(G)

    coded=msg.dot(G)
    return [int(coded[0][i]%2) for i in range(coded.shape[1])]

def detect_error(message):
    message_array=numpy.array([message]).transpose()
    #print(message_array)
    message_length=int(len(message)-math.log2(len(message)+1))

    A=get_parity_matrix(message_length)
    #print(A, A.shape)

    H=numpy.zeros((A.shape[0], sum(A.shape)))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            if j<H.shape[0]:
                H[i][j]=int(i==j)
            else:
                H[i][j]=A[i][j-H.shape[0]]
    #print(H)
    syndrome=H.dot(message_array)
    pos=0
    for i in range(syndrome.shape[0]-1, -1, -1):
        pos=pos*2+syndrome[i][0]%2
    print(pos, syndrome)
    return int(pos)

def decode(message):
    p=detect_error(message)
    message_length=int(len(message)-math.log2(len(message)+1))
    print(message_length)
    if p==0:
        return (message[len(message)-message_length:])
    else:
        message[p-1]=int(not message[p-1])
        return decode(message)

a=[1,1,1,1]
v=encode(a)
v[0]=0
print(decode(v))