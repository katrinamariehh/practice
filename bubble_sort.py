# array main(array){
# 	i = len(array) - 1;
# 	while (i > 0) {
# 	j = 0;
# 	while (j < (len(array-1))){
# 	# swap them
# 	j++;
# 	} else {j++;}
# 	}
# 	i--;}
# 	return array



def bubble_sort(l1):
	i = len(l1)-1
	while i > 0:
		j = 0
		while j < (len(l1)-1):
			if l1[j] > l1[j+1]:
				l1[j], l1[j+1] = l1[j+1], l1[j]
				j+=1
			else:
				j+=1
		i-=1

print "\a"