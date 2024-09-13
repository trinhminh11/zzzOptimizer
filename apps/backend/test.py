import Processing.driveDisc as f

rank = 'A'
incre = f.mainStatIncrement[rank]

level = 12

stat = 'hp'

print(f.mainStatBase[rank][stat] + incre[stat]*level)