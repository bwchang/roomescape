class Place:

	rooms = []

	def __init__(self, name, number, description, furniture=[]):
		self.name = name
		self.number = number
		self.description = description
		self.furniture = furniture
		self.location = self
		if self not in Place.rooms:
			Place.rooms.append(self)

	def add(self, item):
		if item not in self.furniture:
			self.furniture.append(item)


living_room = Place('living room', 1, \
				'You are in the living room. Looking around, you see a plain COUCH paired with a \
wooden COFFEE TABLE. There is also a television on top of a TV STAND. A POTTED PLANT sits in a corner. \
The only exits are a DOOR and an entryway to another room - maybe an OFFICE?')


office = Place('office', 2, \
				'You are in the office. Looking around, you see a big heavy DESK and CHAIR at the \
center of the room. There is a BOOKSHELF behind the desk and a CABINET across from it. You also \
spot a small SAFE built into the wall at a corner of the office. The only exit is to the LIVING ROOM.')