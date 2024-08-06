import pyperclip

name = "Yuan"

with open("test.txt", "r") as f:
	data = f.read()

print(data)

# exit()

data = data.split("\n")


for i in range(len(data)):
	data[i] = data[i].split("\t")
	data[i] = data[i][1:]
	if i % 2 == 0:
		data[i] = data[i][1:]

	data[i] = list(map(lambda x: int (x.replace(",", "")), data[i]))


ans = f"\"name\": \"{name}\",\n"

ans += "\t\t\"stats\": {\n"


for i in range(len(data)):
	if i%2 == 0:
		ans += f'\t\t\t\"{i//2}\": ' + "{\n"
		if i == 0:
			ans += '\t\t\t\t\"1\"'
		else:
			ans += f'\t\t\t\t\"{i//2*10}\"'
	else:
		ans += f'\t\t\t\t\"{(i//2+1)*10}\"'
	
	ans += f": {data[i]}"

	if i%2 == 0:
		ans += ","
	
	ans += "\n"
	if i%2 == 1:
		if i == len(data)-1:
			ans += "\t\t\t}\n"
		else:
			ans += "\t\t\t},\n"

ans += "\t\t}"

pyperclip.copy(ans)



