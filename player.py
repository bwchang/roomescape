from items import *
from places import *

class Player():

	inventory = []
	victory = False
	quit = False

	def __init__(self):
		self.location = living_room

	def use_furniture(self, obj1, obj2):
		if obj1 not in self.inventory:
			print("\nYou don't have the {}".format(obj1.name))
		elif self.location is not obj2 and self.location.location is not obj2.location:
			print("\nThe {} isn't here!".format(obj2.name))
		else:
			self.use_helper(obj1, obj2)
			self.location = obj2

	def use_collectible(self, obj1, obj2):
		if obj1 not in self.inventory or obj2 not in self.inventory:
			print("\nYou don't have both items!")
		else:
			self.use_helper(obj1, obj2)

	def use_helper(self, obj1, obj2):
		if obj1.name in pairings and pairings[obj1.name] == obj2.name:
			if not obj1.used:
				print('\n' + obj1.result)
				obj1.used = True
				self.inventory.remove(obj1)
				if obj2.locked:
					obj2.unlock(self)
			else:
				print('\nYou already used the {} on the {}!'.format(obj1.name, obj2.name))
		else:
			print("\nYou can't use the {} on the {}!".format(obj1.name, obj2.name))

	def use(self, obj1, obj2):
		if isinstance(obj2, Furniture):
			self.use_furniture(obj1, obj2)
		elif isinstance(obj2, Collectible):
			self.use_collectible(obj1, obj2)
		else:
			print("You can't use {} on the {}!".format(obj1.name, obj2.name))

	def take(self, item):
		if self.location is item.location:
			if item.can_take:
				item.location.remove(item)
				self.inventory.append(item)
				item.location = self
				print("\nYou take the {}.".format(item.name.upper()))
			else:
				print("\nYou can't take the {}!".format(item.name.upper()))
		elif item in self.inventory:
			print("\nYou already took this item!")
		else:
			print("\nThere is no {} here!".format(item.name.upper()))

	def move(self, place):
		if self.location.location is place:
			print("\nYou are already in the {}.".format(place.name.upper()))
		else:
			self.location = place
			print("\nYou are in the {}.".format(place.name.upper()))

	def look(self):
		print('\n' + self.location.location.description)
		self.location = self.location.location

	def examine(self, item):
		if item.name == 'door' and not item.locked:
			print("\nIt seems to be looking for a 4-digit password.")
			self.endgame(item)
		elif isinstance(item, Furniture):
			if self.location.location is item.location:
				self.location = item
				item.examine()
			else:
				print("\nThere is no {} here!".format(item.name.upper()))
		elif isinstance(item, Collectible) or isinstance(item, Decoration):
			if item.location is self or item.location is self.location:
				item.examine()
			else:
				print("\nThere is no {} here!".format(item.name.upper()))
		else:
			print("\nYou can't examine this item.")

	def check_inventory(self):
		if not self.inventory:
			print("\nYour inventory is empty.")
		else:
			print("\nYou have in your inventory: ")
			for item in self.inventory:
				print('a ' + item.name)

	def endgame(self, door):
		entering_password = True
		while entering_password:
			password = input("Enter password: ")
			if password == "6666":
				entering_password = False
				self.victory = True
				print("\nYou hear a silent click as the screen flashes green. You push open the door...")
			else:
				print("\nThe screen flashes red. You try the door and it remains closed. Wrong password.")
				retry_password = input("To try again, enter 'yes': ")
				if retry_password not in ['yes', 'y', 'ye', 'Yes', 'YES', 'Y', 'Ye', 'ok', 'Ok', 'OK']:
					entering_password = False
					print("\nYou are in the living room.")




