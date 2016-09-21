from player import *
from places import *

class Item():

	locked = False
	can_take = False
	examined = False
	all_items = []

	def __init__(self, name, location, description, result=''):
		self.name = name
		self.location = location
		self.description = description
		self.result = result
		self.contains = []
		if self not in Item.all_items:
			Item.all_items.append(self)

	def examine(self):
		print("\n" + self.description)

	def add(self, item):
		if item not in self.contains:
			self.contains.append(item)

	def remove(self, obj):
		if obj in self.contains:
			self.contains.remove(obj)
		else:
			print('{} not here!'.format(obj))

	def unlock(self, player):
		self.locked = False
		if self.name == "apple":
			for obj in self.contains:
				player.inventory.append(obj)
				obj.location = player
		elif self.name == "door":
			player.endgame(self)
		elif isinstance(self, Furniture):
			self.description = "The {} is unlocked.".format(self.name.upper())
		else:
			self.description = self.result


class Furniture(Item):

	def __init__(self, name, location, description, result=''):
		Item.__init__(self, name, location, description, result)
		self.location.add(self)

	def examine(self):
		Item.examine(self)
		ans = input("\nLook closer? ")
		if ans in ['yes', 'y', 'ye', 'YES', 'Yes', 'Y', 'Ye', '', 'ok', 'Ok', 'OK']:
			if self.locked:
				print("\nThe {} is locked.".format(self.name))
			elif self.examined and not self.contains:
				print("\nNothing new here.")
			elif not self.contains:
				print('\nNothing special about this.')
			else:
				print(self.result)
			self.examined = True
		else:
			print("\nYou are in the {}.".format(self.location.name))


class Collectible(Item):

	can_take = True
	used = False

	def __init__(self, name, location, description, result):
		""" name = name of item
			place = what room the item is located
			location = piece of furniture by which object was found
			description = description of item
			result = what happens when you successfully use item
			contains = list of other items within this item"""
		Item.__init__(self, name, location, description, result)
		self.location.contains.append(self)


class Decoration(Item):
	pass





############# FURNITURE ##################


door = Furniture('door', living_room, \
				"It is a heavy, sturdy-looking wooden DOOR. The door is locked and there is a \
keypad next to it with the numbers 0-9. The key pad seems to require a key card to activate.")
door.locked = True

couch = Furniture('couch', living_room, \
				"It is a cream-colored sectional COUCH plainly decorated with bright green \
pillows. There is a stain on the right cushion.", \
"You find a SILVER KEY underneath one of the couch cushions.")

plant = Furniture('potted plant', living_room, \
				"An ordinary POTTED PLANT about 4 feet tall sits in a corner of the living room.", \
				"You find a HAMMER buried in the dirt. Interesting hiding choice.")

coffee_table = Furniture('coffee table', living_room, \
				"It is a dark, wooden COFFEE TABLE with one wobbly leg. There is a bowl of \
strawberries and a couple of magazines scattered on top.")

tv_stand = Furniture('tv stand', living_room, \
				"A 55-inch TV sits on top of a dark, wooden TV STAND. The stand has four drawers, \
one of which is locked. It will require a key to open")
tv_stand.locked = True

desk = Furniture('desk', office, \
				"It is an expensive-looking mahogany DESK. It's strangely empty, with only a pen \
a blank piece of paper on it.", \
"You find a GOLD KEY taped to the bottom of the desk.")

cabinet = Furniture('cabinet', office, \
				"A CABINET with 5 drawers stands next to the door. There are two picture frames \
sitting on top of it. The lighter-colored wood of the cabinet stands out against the \
rest of the furniture in the room.", \
"You open the top drawer and find only an APPLE inside. Hmm.")

bookshelf = Furniture('bookshelf', office, \
				"It is a tall, fancy BOOKSHELF filled with old, dusty books. You take a quick glance \
at some of the titles. None of them look interesting.")

chair = Furniture('chair', office, \
				"It is a regular black office CHAIR.")

safe = Furniture('safe', office, \
				"A SAFE is tucked discreetly in a corner of the office. It requires a key to open.",)
safe.locked = True



################### DECORATIONS #######################


"""strawberries = Decoration('strawberries', coffee_table, \
				"A bowl filled to the brim with beautiful, perfectly ripe strawberries sits \
atop the coffee table. You take one and take a bite. It reminds you of sunshine and good company \
and picnics on warm May afternoons.")

pictures = Decoration('picture frames', cabinet, \
				"One frame contains only a stock picture of a mother holding her child. The other \
frame contains a faded picture of a girl with curly blonde hair smiling into the camera. \
She's beautiful.")"""




############# COLLECTIBLES ##################


hammer = Collectible('hammer', plant, \
				"A standard HAMMER you would find in a household toolbox.", \
				"You smash the container open with your hammer. \
Inside you find only a piece of paper with the numbers '6666' written on it.")

apple = Collectible('apple', cabinet, \
				"A bright red, fresh APPLE. It feels a little heavier than it should be. Weird.", \
				"The apple is cut open. There is a CERAMIC CONTAINER inside.")
apple.locked = True

container = Collectible('ceramic container', apple, \
				"An egg-shaped CERAMIC CONTAINER is where the apple core is supposed to be. \
You shake the container and hear a faint rustling sound. Double weird.", \
"The container is smashed open to reveal a piece of paper with the numbers '6666' on it.")
container.locked = True

key_card = Collectible('key card', safe, \
				"An official-looking KEY CARD. It has no writing or pictures on it.", \
"You swipe the key card. The screen lights up; it seems to be looking for a 4-digit password.")

silver_key = Collectible('silver key', couch, \
				"A small, plain SILVER KEY.", \
				"The safe opens! Inside you find a KEY CARD.")

knife = Collectible('knife', tv_stand, \
				"A small KNIFE. It's a little dull but it can definitely still do some damage.", \
				"You cut the APPLE open with the KNIFE. Inside you find:\n{}".format(container.description))

gold_key = Collectible('gold key', desk, \
				"A small, plain GOLD KEY.", \
				"The drawer of the TV STAND opens. Inside you find a plain KNIFE.")





############# Pairings ##################


pairings = {"silver key": "safe",
			"gold key": "tv stand",
			"knife": "apple",
			"hammer": "ceramic container",
			"key card": "door"}


