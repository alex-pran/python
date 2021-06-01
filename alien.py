alien_0 = {'color': 'green', 'points': '5'}
del alien_0['points']
print(alien_0['color'])
print(alien_0)


alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


print("\n\n============= new 1 =================")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")


if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = .3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

print("\n\n============= new 2 =================")

alien_2 = {'x_position': 0, 'y_position': 30, 'speed': 'medium'}
print(f"Origin position: {alien_2['x_position']}.")

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_2['x_position'] = alien_2['x_position'] + x_increment
print(f"New Position: {alien_2['x_position']}")
