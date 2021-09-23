def create_id(firstname, lastname):
	return firstname[0].lower()+(lastname[0:3].lower()).capitalize()

print(create_id("mary", "lamb"))
print(create_id("John", "SMITH"))