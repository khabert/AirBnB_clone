#!/usr/bin/python3
"""
Console for AirBnB clone project
"""


import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]

    def do_create(self, args):
        """Create a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            if args == "BaseModel":
                new = BaseModel()
            elif args == "User":
                new = User()
            elif args == "State":
                new = State()
            elif args == "City":
                new = City()
            elif args == "Amenity":
                new = Amenity()
            elif args == "Place":
                new = Place()
            elif args == "Review":
                new = Review()
            storage.new(new)
            storage.save()
            print(new.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if not args:
            print("** class name missing **")
        elif args.split()[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args.split()) < 2:
            print("** instance id missing **")
        else:
            key = args.split()[0] + '.' + args.split()[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        elif args.split()[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args.split()) < 2:
            print("** instance id missing **")
        else:
            key = args.split()[0] + '.' + args.split()[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        """
        args = line.split()
        result = []
        if len(args) != 0:
            if args[0] not in HBNBCommand.classes:
                print('** class doesn\'t exist **')
                return
            else:
                for key, value in storage.all().items():
                    if type(value).__name__ == args[0]:
                        result.append(value.__str__())
        else:
            for key, value in storage.all().items():
                result.append(value.__str__())
        print(result)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email """
        if not args:
            print("** class name missing **")
        elif args.split()[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args.split()) < 2:
            print("** instance id missing **")
        elif len(args.split()) < 3:
            print("** attribute name missing **")
        elif len(args.split()) < 4:
            print("** value missing **")
        else:
            prop = ['id', 'created_at', 'updated_at']
            key = args.split()[0] + '.' + args.split()[1]
            if args.split()[2] in prop:
                print("** attribute can't be updated  **")
                return
            if key in storage.all():
                setattr(storage.all()[key], args.split()[2], args.split()[3])
                storage.save()
            else:
                print("** no instance found **")


    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program : Ctrl + D"""
        print()
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
