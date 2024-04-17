#!/usr/bin/python3
"""Script that defines a command line interface for the HBNB application"""

import cmd
import sys
from models import storage
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class: manages the command line interface for the HBNB application"""

    # Determine the prompt string based on whether the input is from a TTY device
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    # Map class names to their respective classes for object instantiation
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    # List of commands that support dot syntax
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    # Data type mapping for attribute values
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """Method called before entering the command loop; checks if input is non-interactive"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """
        Method called before executing any command;
        It reformats advanced command syntax into a standard form
        """
        _cmd = _cls = _id = _args = ''  # Initialize line elements

        # Check for the presence of '.', '(', and ')' indicating advanced syntax
        if '.' not in line or '(' not in line or ')' not in line:
            return line

        try:
            pline = line[:]  # Create a copy of the input line

            # Extract the class name
            _cls = pline[:pline.find('.')]

            # Extract the command
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in self.dot_cmds:
                raise Exception

            # Extract and process arguments between parentheses
            pline = pline[pline.find('(') + 1:pline.find(')')]

            if pline:
                # Split the arguments into id and the rest
                pline = pline.partition(', ')

                # Remove quotes from id and handle args
                _id = pline[0].replace('\"', '')
                pline = pline[2].strip()

                if pline:
                    if pline[0] == '{' and pline[-1] == '}':
                        _args = pline

                    else:
                        _args = pline.replace(',', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass

        finally:
            return line

    def postcmd(self, stop, line):
        """Method called after executing each command, that checks if input is non-interactive"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """Exit the HBNB console"""
        exit()

    def help_quit(self):
        """Display help information for the 'quit' command"""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """Handle the EOF signal to exit the program"""
        print()
        exit()

    def help_EOF(self):
        """Display help information for the EOF command"""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Override the emptyline method of CMD to prevent action on empty input"""
        pass

    def do_create(self, args):
        """Create an object of the specified class"""
        new = args.split(" ")

        if not new:
            print("** class name missing **")
            return

        elif new[0] not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[new[0]]()

        for i in range(1, len(new)):
            first = new[i].split("=")

            try:
                if first[1][0] == "\"":
                    first[1] = first[1].replace("\"", "")
                    first[1] = first[1].replace("_", " ")

                elif "." in first[1]:
                    first[1] = float(first[1])

                else:
                    first[1] = int(first[1])
                setattr(new_instance, first[0], first[1])

            except Exception:
                continue

    def help_create(self):
        """Display help information for the 'create' command"""
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Display the attributes of a specified object"""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in self.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            print(storage._FileStorage__objects[key])

        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """Display help information for the 'show' command"""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Destroy a specified object"""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in self.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del (storage.all(args)[key])
            storage.save()

        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Display help information for the 'destroy' command"""
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """Display all objects or all objects of a specified class"""
        print_list = []

        if args:
            args = args.split(' ')[0]

            if args not in self.classes:
                print("** class doesn't exist **")
                return

            for k, v in storage.all().items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """Display help information for the 'all' command"""
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count the current number of instances of a specified class"""
        count = 0

        for k, v in storage.all().items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """Display help information for the 'count' command"""
        print("Usage: count <class_name>")

    def do_update(self, args):
        """Update an existing object with new information"""
        c_name = c_id = att_name = att_val = kwargs = ''

        # Parse the input to isolate class name, ID, and arguments
        args = args.partition(" ")

        if args[0]:
            c_name = args[0]

        else:
            print("** class name missing **")
            return

        if c_name not in self.classes:
            print("** class doesn't exist **")
            return

        # Continue parsing to isolate the object ID and attributes
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:
            print("** instance id missing **")
            return

        # Create a unique key from the class name and ID
        key = c_name + "." + c_id

        # Verify the existence of the object using the key
        if key not in storage.all():
            print("** no instance found **")
            return

        # Determine whether input contains keyword arguments or positional arguments
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:
            args = args[2]
            if args and args[0] == '\"':
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            if not att_name and args[0] != ' ':
                att_name = args[0]

            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # Retrieve the object's current attributes
        new_dict = storage.all()[key]

        # Update attributes with the provided values
        for i, att_name in enumerate(args):
            if i % 2 == 0:
                att_val = args[i + 1]

                if not att_name:
                    print("** attribute name missing **")
                    return

                if not att_val:
                    print("** value missing **")
                    return

                if att_name in self.types:
                    att_val = self.types[att_name](att_val)

                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # Save updates to storage

    def help_update(self):
        """Display help information for the 'update' command"""
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()  # Start the command loop
