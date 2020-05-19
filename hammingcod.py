import numpy
import math

G=numpy.zeros(1)
H=numpy.zeros(1)
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
    parity_mtrx=numpy.zeros((no_syndrome_rows, message_length))

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
                parity_mtrx[parity_mtrx.shape[0] -1 -j][s_col]=row[j]
            s_col+=1
        syndrome+=1
    
    if(extra):
        for i in range(message_length):
            parity_mtrx[no_syndrome_rows-1][i]=1

    return parity_mtrx.transpose()

def encode(message):
    global G
    msg=numpy.array([message])

    A=get_parity_matrix(len(message)).transpose()

    G=numpy.zeros((A.shape[1], sum(A.shape))).transpose()
    c=0

    for i in range(G.shape[0]):
        if math.log2(i+1)%1==0:
            for j in range(G.shape[1]):
                G[i][j]=A[int(math.log2(i+1))][j]
        else:
            for j in range(G.shape[1]):
                G[i][j]=int(j==c)
            c+=1
    G=G.transpose()
    #print(G, G.shape)

    coded=msg@G%2
    return coded.tolist()[0]

def decode(message):
    global H
    message_array=numpy.array([message]).transpose()
    H=numpy.zeros((len(message), int(math.log2(1+len(message)))))

    for i in range(H.shape[0]):
        r=to_bin_array(i+1, H.shape[1])[::-1]
        for j in range(H.shape[1]):
            H[i][j]=r[j]
    
    H=H.transpose()
    syndrome=H@message_array%2
    pos=0
    for i in range(syndrome.shape[0]-1, -1, -1):
        pos=pos*2+syndrome[i][0]
    pos=int(pos)
    message[pos-1]=int(not message[pos-1])
    return pos