import os

def sort_list(lst):
	i = 0
	while i < len(lst):
		j = 0
		while j < (len(lst) - i - 1):
			if lst[j] > lst[j+1]:
				tmp = lst[j]
				lst[j] = lst[j+1]
				lst[j+1] = tmp
			j+=1
		i+=1
	return lst

if __name__ == "__main__":
	lst = [-3, 3, -12, 6, 2]
	print(sort_list(lst))
