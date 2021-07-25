fileName = './RR.txt'
with open(fileName) as f:
    lines = f.readlines()

def divide_chunks(l, n):
    for i in range(0, len(l), n): 
        yield l[i:i + n]
  
groupSize = 4
groups = list(divide_chunks(lines, groupSize))
for i in groups:
	print(i)
	print("\n")
	
	

