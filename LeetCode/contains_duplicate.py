x = [1,2,3,1]
y = [1,2,3,4]
z = [1,1,1,3,3,4,3,2,4,2]

def contains_duplicate(l):
	if len(l) == len(set(l)):
		return False 
	else:
		return True 

print(contains_duplicate(z))
