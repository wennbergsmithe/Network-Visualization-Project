
file = open("Airport_Codes.txt", "r")
#dictionary for codes and coords
dic = {}
#parsing file
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
	#adding to dictionary
	dic[strs[0]] = [strs[1], strs[2]]
#close file
file.close()

#open file for nodes
file = open("nodes.txt", "r")
#matching codes in nodes file to coordinates collected from other file
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
#print results to the console
num = 0

for code in codes:
	coords = dic.get(code)
	if(coords != None):
		print(str(num) + ","+code+ ","+ coords[0]+ ","+ coords[1])
	num+=1




