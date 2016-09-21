from escape import *

def do_action(player, action_verb, action_obj):
	if action_verb in action_keywords:
		action_dict[action_verb](player, action_obj)
	else:
		print("Invalid action. Please try again.")

def do_move_form(player, action_obj):
	if not action_obj:
		print('Move where?')
	elif action_obj[0] == 'to':
		do_move_form(player, action_obj[1:])
	else:
		action_string = ' '.join(action_obj)
		room = find_room(action_string)
		if room:
			player.move(room)
		else:
			print(action_string.upper() + ' is not a valid room.')

def do_look_form(player, action_obj):
	if not action_obj:
		player.look()
	elif action_obj[0] == 'around':
		do_look_form(player, action_obj[1:])
	elif action_obj[0] == 'at':
		if not action_obj[1:]:
			print("You can either LOOK AROUND the room or EXAMINE an item.")
		else:
			action_string = ' '.join(action_obj)
			item = find_item(action_string)
			if item:
				print("You must EXAMINE the {}.".format(item.name))
			else:
				print("There is no {} to look at.".format(' '.join(action_obj[1:])))
	else:
		look_input = input("Look around the room? ")
		if look_input in ['yes', 'y', 'ye', 'Yes', 'Y', 'Ye', '', 'ok', 'Ok', 'OK']:
			do_look_form(player, [])
		else:
			print("Invalid action. Please try again.")

def do_examine_form(player, action_obj):
	if not action_obj:
		print("You must examine an item.")
	else:
		action_string = ' '.join(action_obj)
		item, room = find_item(action_string), find_room(action_string)
		if item:
			player.examine(item)
		elif room:
			print("You must LOOK AROUND the {}.".format(room.name))
		else:
			print("There is no {} to examine.".format(action_string))

def do_take_form(player, action_obj):
	if not action_obj:
		print("You must take an item.")
	else:
		action_string = ' '.join(action_obj)
		item, room = find_item(action_string), find_room(action_string)
		if item:
			player.take(item)
		elif room:
			print("You cannot take the {}.".format(room.name))
		else:
			print("There is no {} to take.".format(action_string))

def do_use_form(player, action_obj):
	if not action_obj or 'on' not in action_obj:
		print("You must USE an item ON another item.")
	else:
		on_index = 0
		for i in range(len(action_obj)):
			if action_obj[i] == 'on':
				on_index = i
		string1, string2 = ' '.join(action_obj[:on_index]), ' '.join(action_obj[on_index:])
		obj1, obj2 = find_item(string1), find_item(string2)
		if not string1 or not string2:
			do_use_form(player, [])
		elif not obj1:
			print("There is no {} to use.".format(string1))
		elif not obj2:
			print("There is no {} to use the {} on.".format(string2, obj1.name))
		else:
			player.use(obj1, obj2)

def do_check_form(player, action_obj):
	player.check_inventory()

def do_help_form(player, action_obj):
	print(help_text)

def do_quit_form(player, action_obj):
	quit_input = input('Are you sure? Your progress will not be saved: ')
	if quit_input in ['yes', 'y', 'ye', 'Yes', 'YES', 'Y', 'Ye', '', 'ok', 'Ok', 'OK']:
		player.quit = True

def find_item(string):
	for item in Item.all_items:
		if item.name in string:
			return item

def find_room(string):
	for room in Place.rooms:
		if room.name in string:
			return room




############## ACTION KEYWORDS ####################

action_keywords = ['check',
				   'look',
				   'move',
				   'examine',
				   'take',
				   'use',
				   'help',
				   'quit']

action_prompt = "\n---------------------------------------------------------------------\
\nChoose an action: \nMOVE TO | LOOK | EXAMINE | TAKE | USE | CHECK INVENTORY | HELP | QUIT"

action_dict = {'check': do_check_form,
			   'look': do_look_form,
			   'move': do_move_form,
			   'examine': do_examine_form,
			   'take': do_take_form,
			   'use': do_use_form,
			   'help': do_help_form,
			   'quit': do_quit_form}






