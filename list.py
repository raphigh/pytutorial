list1 = [1,4,7,'john',True]
colors = ['g','b','w','r']
print(colors[3])
print(colors[-1])
print(colors[1:4])
print(colors[1:-2])
colors[1] = 'y'
print(colors)
colors[0:2] = ['y','o','p']
print(colors)
colors.extend(['o','g'])
colors.append('o')
print(colors)
colors.insert(2,'s')
print(colors)
colors.remove('o')
print(colors)
colors.index('o')
colors.count('y')
colors.sort()
colors2 = sorted(colors)
del colors
colors.reverse()


