def list_of_multiples (num, length):
	final_list = []
	for i in range(1,length+1):
		final_list.append(num*i)
	return final_list

#return [ num*i for i in range(1,length+1)]

print(list_of_multiples(12,10))