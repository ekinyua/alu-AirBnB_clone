#!/usr/bin/python3
""" it's all about console """

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    models.__all__ = {"BaseModel": BaseModel, 
                      "User": User, 
                      "State": State,
                      "Place": Place, 
                      "City": City, 
                      "Amenity": Amenity, 
                      "Review": Review}

    # Quit command
    def do_quit(self, line):
        """Quit the program"""
        return True

    # End Of File command
    def do_EOF(self, line):
        """Exit the program"""
        return True

    # Empty line handling
    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        pass

    # Create command
    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return
        words = line.split()
        if words[0] not in models.__all__:
            print("** class doesn't exist **")
            return
        new_model = eval(words[0] + "()")
        new_model.save()
        print(new_model.id)

    # Show command
    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return
        words = line.split()
        if words[0] not in models.__all__:
            print("** class doesn't exist **")
            return
        if len(words) == 1:
            print("** instance id missing **")
            return
        key = words[0] + "." + words[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        print(storage.all()[key])

    # Destroy command
    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return
        words = line.split()
        if words[0] not in models.__all__:
            print("** class doesn't exist **")
            return
        if len(words) == 1:
            print("** instance id missing **")
            return
        key = words[0] + "." + words[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    # All command
    def do_all(self, line):
        if not line:
            print([str(v) for v in storage.all().values()])
            return
        words = line.split()
        if words[0] not in models.__all__:
            print("** class doesn't exist **")
            return
        print([str(v) for v in storage.all().values() if type(v).__name__ == words[0]])

    # Update command
    def do_update(self, line):
        if not line:
            print("** class name missing **")
            return
        words = line.split()
        if words[0] not in models.__all__:
            print("** class doesn't exist **")
            return
        if len(words) == 1:
            print("** instance id missing **")
            return
        key = words[0] + "." + words[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        if len(words) == 2:
            print("** attribute name missing **")
            return
        if len(words) == 3:
            print("** value missing **")
            return
        setattr(storage.all()[key], words[2], words[3].strip('"'))
        storage.save()

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
