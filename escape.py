from player import *
from actions import *

def play():
	player = Player()
	print(intro_text)
	while not player.victory and not player.quit:
		print(action_prompt)
		action_raw_input = input("\nAction: ")
		if not action_raw_input:
			print("Please enter an action.")
		else:
			action_input = action_raw_input.split()
			action_verb, action_obj = action_input[0].lower(), [word.lower() for word in action_input[1:]]
			do_action(player, action_verb, action_obj)
	if player.victory:
		print(victory_text)
	else:
		print(quit_text)
	replay = input("\nPlay again? ")
	if replay in ['yes', 'y', 'ye', 'Yes', 'YES', 'Y', 'Ye', '']:
		play()
	else:
		print("\nThanks for playing! Wish you the best in trying to find meaning in a senseless world.")





############## TEXTS ####################

intro_text = "\nYou wake up in an unfamiliar room with a throbbing headache. The last thing \
you remember is... you don't even remember the last thing you remember. What in the world is going on?"

victory_text = "\nCongratulations, you have escaped the room! Now you must go out and face the \
real world to try and figure out what the hell happened. So really, did you escape at all? Or did you \
just condemn yourself to a different, yet arguably worse, reality? Are you free now?"

quit_text = "\nYou have given up, resigning yourself to the fate of living out the rest of your \
days in these rooms. Perhaps it is better this way."

help_text = "\nType in one of the available commands, followed by an object/place if necessary. Examples: \
\nMOVE TO OFFICE - move to office \
\nLOOK AROUND - list all items you can see in the room you're in \
\nEXAMINE COUCH - description of couch and possible hidden objects \
\nTAKE APPLE - put apple in your inventory \
\nUSE APPLE ON COUCH - try to apply apple to couch \
\nCHECK INVENTORY - list items in your inventory"






if __name__ == "__main__":
	play()