"""

A python program to perform selection sort operation on a list of numbers.
Input : li=[500,4,2,1,8,6,10,24,0,11]
output : li=[0, 1, 2, 4, 6, 8, 10, 11, 24, 500]

"""

def selectionsort(li):
	for i in range(len(li)):
		for j in range(i+1,len(li)):
			if(li[i]>li[j]):
				(li[i],li[j])=(li[j],li[i]) # swap two numbers

	return li

if(__name__=='__main__'):
	li=[500,4,2,1,8,6,10,24,0,11]
	print(selectionsort(li))