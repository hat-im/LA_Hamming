import golay_code
import hammingcod
import time
import random

test_cases=10000

def int_to_bin_array(n, l):
    s=bin(n)[2:]
    if len(s)<l:
        s="0"*(l-len(s))+s
    else:
        s=s[len(s)-l:]
    return [int(x) for x in s]

def compare_codes():
    numbers=[random.randint(0, 2**11-1) for i in range(test_cases)]

    hamming_inputs=[int_to_bin_array(i, 11) for i in numbers]
    golay_inputs=[int_to_bin_array(i, 12) for i in numbers]

    hamming_encoded=[]
    print("Hamming code analysis.\nTime taken to encode.")
    start=time.time()
    for i in hamming_inputs:
        hamming_encoded.append(hammingcod.encode(i))
    end=time.time()
    print("Took",end-start,"seconds for",test_cases,"test cases")
    print("The size of the encoded message is",100*(len(hamming_encoded[0])-len(hamming_inputs[0]))/len(hamming_inputs[0]),"%","bigger than the original.")
    print("Time taken to correct single error messages, which is equivalent to detecting two bit errors")
    hamming_corrupted=[x for x in hamming_encoded]
    for i in hamming_corrupted:
        i[random.randint(0, len(hamming_encoded[0])-1)]=int(not i[random.randint(0, len(hamming_encoded[0])-1)])
    start=time.time()
    hamming_decoded=[]
    for i in hamming_corrupted:
        hamming_decoded.append(hammingcod.decode(i))
    end=time.time()
    print("Time taken to detect/correct",test_cases,"errors=",end-start,"seconds")

    golay_encoded=[]
    print("Golay code analysis.\nTime taken to encode.")
    start=time.time()
    for i in golay_inputs:
        golay_encoded.append(golay_code.encode(i))
    end=time.time()
    print("Took",end-start,"seconds for",test_cases,"test cases")
    print("The size of the encoded message is",100*(len(golay_encoded[0])-len(golay_inputs[0]))/len(golay_inputs[0]),"%","bigger than the original.")
    print("Time taken to correct single error messages")
    golay_corrupted=[x for x in golay_encoded]
    for i in golay_corrupted:
        i[random.randint(0, len(golay_encoded[0])-1)]=int(not i[random.randint(0, len(golay_encoded[0])-1)])
    start=time.time()
    golay_decoded=[]
    for i in golay_corrupted:
        golay_decoded.append(golay_code.decode(i))
    end=time.time()
    print("Time taken to detect/correct",test_cases,"errors=",end-start,"seconds")


compare_codes()