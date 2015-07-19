class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        return {
        "north-west": [(self.south + self.width_NS), self.west],
        "north-east": [(self.south + self.width_NS), (self.west + self.width_WE)],
        "south-west": [self.south, self.west],
        "south-east": [self.south, (self.west + self.width_WE)]
        }

    def area(self):
    	return self.width_WE * self.width_NS

    def volume(self):
    	return self.width_NS * self.width_WE * self.height

    def __repr__(self):
    	return "Building(%s, %s, %s, %s, %s)" % (self.south, self.west, self.width_WE, self.width_NS, self.height)

print (Building(1, 2, 2, 2).corners())
print (Building(1, 2.5, 4.2, 1.25).area())
print (Building(1, 2.5, 4.2, 1.25, 101).volume())
print(repr(Building(0, 0, 10.5, 2.546)))