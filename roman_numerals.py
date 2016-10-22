def BasicRomanNumerals(str): 
	arabic_total = 0#	the final result will be an int
	str_cap = str.upper()#	just to catch any case issues
	input_list = list(str_cap)#	break them out to individual elements for conversion & comparison
	roman_list = []# to hold the int values for each roman numeral
	for i in input_list:#	convert each element from roman to arabic (int)
		if i == "I":
			roman_list.append(1)# had to google to find append :(
		elif i == "V":# STILL keep forgtting these damn colons!!!!!!!!
			roman_list.append(5)
		elif i == "X":
			roman_list.append(10)		
		elif i == "L":
			roman_list.append(50)
		elif i == "C":
			roman_list.append(100)
		elif i == "D":
			roman_list.append(500)
		elif i == "M":
			roman_list.append(1000)
		else:
			return False# in case the input is not appropriate for this calculation

	for x in range(len(str)):
		if (x+1) in range(len(str)):#		to fix out of range error, IF there is a num to the right
			if roman_list[x] < roman_list[x+1]:# when the left value is less than the right value			
				arabic_total = arabic_total - roman_list[x] #value becomes negative
			else:
				arabic_total = arabic_total + roman_list[x] #otherwise add value to total
		else:#  to cathc the last value that has no value to the right
			arabic_total = arabic_total + roman_list[x]# added be default

	return arabic_total

 
print BasicRomanNumerals(raw_input("I can convert your roman numeral!")) 