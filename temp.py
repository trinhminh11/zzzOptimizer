import pyperclip

while True:
	data = input()
	# with open("temp.txt", "r") as f:
		# data = f.readline().strip("\n")

	PHYSCIAL = "<span style=\\\"color: rgb(192,168,47)\\\">Physical DMG</span>"
	ICE = "<span style=\\\"color: rgb(140,216,218)\\\">Ice DMG</span>"
	ELECTRIC = "<span style=\\\"color: rgb(46,182,255)\\\">Electric DMG</span>"
	ETHER = "<span style=\\\"color: rgb(248,66,123)\\\">Electric DMG</span>"

	ans = "self.passiveDescription = \"<p>"

	i= 0
	t = 0

	stats = []

	while i < len(data):
		if data[i] == " ":
			if "/" in data[i+1:i+8] and " " not in data[i+1:i+8]:
				for j in range(i+1, len(data)):
					if data[j] == " " or data[j] == ",":
						break

				temp = list(map(lambda x: float(x) if float(x) != int(float(x)) else int(x), data[i+1:j].strip(" ").strip(".").strip("%").strip("s").split("/")))

				stats.append(temp)
				
				if data[j-1] == "%":
					ans += " <span style=\\\"color: rgb(237,197,84)\\\">{" + str(t) + "}%</span> "
				elif data[j-1] == "s":
					ans += " <span style=\\\"color: rgb(237,197,84)\\\">{" + str(t) + "}s</span> "
				else:
					ans += " <span style=\\\"color: rgb(237,197,84)\\\">{" + str(t) + "}</span> "

				t+=1
				i = j+1
				
				continue
		
			
		ans += data[i]
		
		i+=1

	statstring = "self.passiveStats = " + str(stats)

	pyperclip.copy(statstring + "\n\t\t" + ans.replace("Ice DMG", ICE).replace("Physical DMG", PHYSCIAL).replace("Electric DMG", ELECTRIC).replace("Ether DMG", ETHER) + "</p>\"" + "\n")
# print(ans)
