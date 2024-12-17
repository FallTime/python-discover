# Question 2.6:
# Write a program that prints a box, an oval, an arrow and a diamond, as shown:
box = ('* ' * 9 + '\n' + ('*' + ' ' * 15 + '*\n') * 6 + '* ' * 9 + '\n')

oval_top = (' ' * 6 + '* ' * 3 + '\n')
oval_connect = (' ' * 4 + '* ' + ' ' * 6 + '* ' + '\n')
oval_border = (' ' * 2 + '* ' + ' ' * 10 + '* ' + '\n')
oval = (oval_top + oval_connect + oval_border * 5 + oval_connect + oval_top)

line = (' ' * 8 + '* ' + '\n')
arrow = (line + oval_top + ' ' * 4 + '* ' * 5 + '\n' + line * 6)

diamond_layer1 = (' ' * 6 + '*' + ' ' * 3 + '*' + '\n')
diamond_layer2 = (' ' * 4 + '*' + ' ' * 7 + '*' + '\n')
diamond_layer3 = (' ' * 2 + '*' + ' ' * 11 + '*' + '\n')
top_layer = diamond_layer1 + diamond_layer2 + diamond_layer3
bottom_layer = diamond_layer3 + diamond_layer2 + diamond_layer1
diamond = (line + top_layer + ('*' + ' ' * 15 + '*\n') + bottom_layer + line)

print(box)
print(oval)
print(arrow)
print(diamond)
