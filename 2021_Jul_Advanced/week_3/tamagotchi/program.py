#! 42 min 53 sec
#! #1 passed all tests

# Import required modules
from tamagotchi import Tamagotchi
from utils import print_sorted_dict
import database as db

def mainline():
  """ Mainline """
  # Get input
  command = input('Command: ')
  # Loop until empty command is encountered
  while command:
    # Subroutine to handle commands
    process_command(command)
    command = input('Command: ')

def process_command(command):
  """
  Processes a command. Valids commands are as follows:
  - `create <name>`
  - `feed <name>`
  - `play <name>`
  - `wait`

  An invalid command will result in an error message "Invalid command." being
  printed to the console; Tamagotchi's that have not been created will cause
  error message "No Tamagotchi with that name." being printed to the console;
  using the `create` command with the name of an existing Tamagotchi will cause
  error message "You already have a Tamagotchi called that." being printed to
  the console.

  :param command: The command to process. Note that this command must be a
                  valid command as specified above. Non-valid commands will
                  result in a variety of error messages being printed.
  :type command: string
  """
  # Start by splitting command into words
  command = command.split()
  # Parse command => identify first word in command
  if command[0] == 'create' and len(command) == 2:
    # If command is create, check if a Tamagotchi with that name already exists
    if command[1] in db.pets.keys():
      # If it exists, check if it is still alive
      if not db.pets[command[1]].is_dead():
        # If not dead, print error message and exit (do nothing)
        print('You already have a Tamagotchi called that.')
        return
    
    # If it doesn't already exist or is dead, create a new one
    db.pets[command[1]] = Tamagotchi(command[1])
  
  elif command[0] == 'feed' and len(command) == 2:
    # If command is feed, check if Tamagotchi with that name already exists
    if command[1] not in db.pets.keys():
      # If it doesn't exist, print error message and exit (do nothing)
      print('No Tamagotchi with that name.')
      return
    
    # If it exists, call feed method
    db.pets[command[1]].feed()
  
  elif command[0] == 'play' and len(command) == 2:
    # If command is play, check if Tamagotchi with that name already exists
    if command[1] not in db.pets.keys():
      # If it doesn't exist, print error message and exit (do nothing)
      print('No Tamagotchi with that name.')
      return
    
    # If it exits, call play method
    db.pets[command[1]].play()

  elif command[0] == 'wait' and len(command) == 1:
    # If command is wait, do nothing and pass time
    pass

  else:
    # Print error message and exit (do nothing)
    print('Invalid command.')
    return

  # After the command has been processed, display current state of all
  # Tamagotchi's in NAME SORTED ORDER and increment time
  
  # Start by printing the pets sorted by alphabetical order
  print_sorted_dict(db.pets)

  # Call increment time method on all Tamagotchi's
  increment_time()

def increment_time():
  """
  Call :func:`increment_time` method on all Tamagotchi's.
  """

  for pet in db.pets:
    db.pets[pet].increment_time()


if __name__ == '__main__':
  mainline()