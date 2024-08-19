
# while True:
# 	# printing class for Wengine
# 	name = input('name: ')
# 	if name == 'q':
# 		exit()

# 	clssname = name.replace(' ', '').replace('[', '').replace(']', '').replace('-', '')
# 	rank = 'B'
# 	mainStat = 'atk'
# 	fightingStyle = input("type: ")
# 	subStat = input('substat: ')


# 	ans = ''

# 	ans += f'class {clssname}(WEngine):\n'
# 	ans += f'\tdef __init__(self):\n'
# 	ans += f'\t\tsuper().__init__(\"{name}\", \"{rank}\", \"{fightingStyle}\", Stat(\"{mainStat}\"), Stat(\"{subStat}\"))\n\n'


# 	import pyperclip
# 	pyperclip.copy(ans)



# # printing WEngine

# data = ''


# with open('test.txt', 'r') as f:
# 	for i in range(12):
# 		s = f.readline()
# 		if i%2 == 0:
# 			s = s[3:]
# 		# s = s.split('\t')
# 		# print()
# 		# print(s)
# 		data += s


# data = data.split('\n')


# for i in range(len(data)):
# 	data[i] = data[i].split("\t")[1:]
	


# ans = ''

# promotion = -1
# level = 0

# temp = '%'

# for i in range(len(data)):
# 	if i % 2 == 0:
# 		promotion += 1
# 	else:
# 		level += 10
	
# 	if i != 0:
# 		ans += '\t\t'

# 	ans += f'self.baseStatLevel[\'mainStat\'][{promotion}][{level}], self.baseStatLevel[\'subStat\'][{promotion}][{level}] = {data[i][0]} , {data[i][1] if data[i][1][-1] != temp else data[i][1][:-1]}\n'



# import pyperclip
# pyperclip.copy(ans)


import os

f = 'apps/backend/media/wengines/'

for name in os.listdir(f):
	if name[-4:] == "webp":
		new_name = ""
		for c in name[9:]:
			if c == ".":
				break
			if c.isalpha() or c == "_":
				new_name += c
		
		os.rename(f+name, f+new_name + ".png")