# Communication Networks
# Implementation of (24,12) Golay Code 
# Karen Galstyan (A09130138)

#!/usr/bin/python
import numpy as np

def createnoise(l,num):
	temp=np.random.randint(24, size=num)
	#Show error positions
	print ("Error poisitoins at "+str(temp)) 
	l=np.copy(v)
	l[temp]+=1
	l[temp]=np.remainder(l[temp],2)
	return l

#Input is Randomized can be added manually for testing
i=np.random.randint(2, size=12)



a = np.array([1,1,0,1,1,1,0,0,0,1,0])
j= np.array([1,1,1,1,1,1,1,1,1,1,1,0])

I=np.identity(12)
Bc=list()
Bc.append(np.append(a,1))

for x in range(1,11):
	b=np.roll(a,-x)
	b=np.append(b,1)
	Bc.append(b)
Bc.append(j)
Bc=np.array(Bc)


G=np.hstack((Bc,I))
H=np.hstack((I,Bc))

v=np.dot(i,G)
v=np.remainder(v,2)
print("Encoded message"+str(v)) 
#Enconding done 

#Create channel noise in random positions
#Number of errors is currently hardcoded to 3. Can be changed for further tests
res=createnoise(v,3)
print("Result after noise "+str(res))


def detecterror(input):
	s=np.dot(H,input)
	s=np.remainder(s,2)

	w=np.sum(s)
	#print w
	
	if w<=3:
		return np.append(s,np.zeros(12))
	for i in range(12):
		tmp=np.remainder(np.add(Bc[i],s),2)
		w2=np.sum(tmp)
		#print w2
		if w2<=2:
			ei=np.zeros(12)
			ei[i]=1
			return np.append(tmp,ei)

	s2=np.remainder(np.dot(s,Bc),2)
	w3=np.sum(s2)
	if w3<=3:
		return np.append(np.zeros(12),s2)
	for i in range(12):
		tmp=np.remainder(np.add(Bc[i],s2),2)
		w2=np.sum(tmp)
		#print w2
		if w2<=2:
			ei=np.zeros(12)
			ei[i]=1
			return np.append(ei,tmp)
	return "Undetectable Error!"	

u=detecterror(res)
print("Error vector= "+str(u))

def decode():
	input=np.remainder(np.add(u,res),2)
	result=np.remainder(np.dot(input,H.T),2)
	if np.sum(result)==0:
		return input 

if u is not "Undetectable Error!":
	print ("Codeword after Decoding ="+str(decode()))
	#Double Checking
	print(np.sum(v-decode()))





