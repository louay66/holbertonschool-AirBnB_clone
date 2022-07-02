#!/usr/bin/python3
"""Modulee for the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """  HBNBCommand is like console to mange project"""
    prompt = "(hbnb)"

    def do_create(self, line):
        """ Creates a new instance of class"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save
            print(b.id)

    def do_show(self, line):
        """ Prints the string representation of
        an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            word = line.split(' ')
            if len(word) < 2:
                print("** instance id missing **")
            elif word[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                key = f"{word[0]}.{word[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            word = line.split(' ')
            if len(word) < 2:
                print("** instance id missing **")
            elif word[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                key = f"{word[0]}.{word[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """ Prints all string representation of
        all instances based or not on the class name"""
        if line != "":
            word = line.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                repe = [str(obj) for key, obj in storage.all().items()
                        if type(obj).__name__ == words[0]]
                print(repe)
        else:
            repe = [str(obj) for key, obj in storage.all().items()]
            print(repe)

    def do_update(self, line):
        """Updates an instance based on the
        class name and id by adding or updating attribute"""
        if line == "" or line is None:
            print("** class name missing **")
            return
        word = line.split(" ")
        if word[0] not in storage.classes():
            print("** class doesn't exist **")
            if len(word) < 2:
                print("** instance id missing **")
                return
                key = f"{word[0]}.{word[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    ojec_data = storage.all()[key]
                    acess_denied = ["id", "created_at", "updated_at"]
                    if ojec_data:
                        arg = line.split(" ")
                        if len(arg) < 3:
                            print("** attribute name missing **")
                        elif len(arg) < 4:
                            print("** value missing **")
                        elif arg[2] not in acess_denied:
                            ojec_data.__dict__[arg[2]] = arg[3]
                            ojec_data.updated_at = datetime.now()
                            storage.save()
        else:
            print("** class doesn't exist **")

    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        "Doesn't do anythin when press ENTRE"
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
