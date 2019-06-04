

file = open("Airport_Codes.txt", "r")

dic = {}
for line in file:
	string = ""
	strs = []
	for char in line:
		if(char != ","):
			string += char
		else:
			strs.append(string)
			string = ""

	leng = len(string)
	num = leng - 1
	strs.append(string[:num])
	string = ""
	dic[strs[0]] = [strs[1], strs[2]]
file.close()





file = open("nodes.txt", "r") 
codes = []
for line in file: 
	record = False
	code = ""
	for char in line:
		if (char == ' '):
			record = True
		if (record and (char!='"')):
			code += char

	leng = len(code)
	num = leng - 1
	codes.append(code[1:num])

file.close()

num = 0
for code in codes:
	
	coords = dic.get(code)
	if(coords != None):
		print(str(num) + ","+code+ ","+ coords[0]+ ","+ coords[1])

	

	num+=1




