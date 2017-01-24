from data import locations

directions = {
    (0, -1): "north",
    (1, 0): "east",
    (0, 1): "south",
    (-1, 0): "west",
}

position = (0, 0)

while True:
    location = locations[position]
    print 'you are at the %s' % location

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)
        if possible_position:
            print 'to the %s is a %s' % (k, possible_location)
            valid_directions[k] = possible_position

    direction = raw_input('Which direction do you want to go?\n')
    position = valid_directions[direction]
