#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """The class HBNBCommand"""
    prompt = "(hbnb) "

    all_classes = ["BaseModel", "Amenity", "City",
                   "Place", "Review", "State", "User"]

    att_str = ["name", "amenity_id", "city_id", "place_id",
               "state_id", "user_id", "description", "text",
               "email", "password", "first_name", "last_name"]

    att_int = ["number_rooms", "number_bathrooms",
               "max_guest", "price_by_night"]

    att_float = ["longitude", "latitude"]

    def do_quit(self, arg):
        """Quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """Ctrl+D to exit program"""
        return True

    def do_emptyline(self):
        """Empty line + Enter returns nothing"""
        pass

    def validation(self, arg, _id_flag=False, _attr_flag=False):
        """Validation of argument that passes to continue"""
        args = arg.split()
        _lens = len(args)
        if _lens == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return False
        if _id_flag and args[0]+"."+args[1] not in storage.all():
            print("** instance id missing **")
            return False
        if _lens == 2 and _attr_flag:
            print("** attribute name missing **")
            return False
        if _lens == 3 and _attr_flag:
            print("** value missing **")
            return False
        return True

    def do_create(self, arg):
        """Creates a new instance, saves it and prints id"""
        classes = {
            "BaseModel": BaseModel,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }
        if self.validation(arg):
            args = arg.split()
            if args[0] in classes:
                new = classes[args[0]]()
            storage.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if self.validation(arg, True):
            args = arg.split()
            _keys = args[0]+"."+args[1]
            print(storage.all()[_keys])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if self.validation(arg, True):
            args = arg.split()
            _keys = args[0]+"."+args[1]
            del storage.all()[_keys]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        _lens = len(args)
        my_list = []
        if _lens >= 1:
            if args[0] not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if args[0] in key:
                    my_list.append(str(value))
        else:
            for key, value in storage.all().items():
                my_list.append(str(value))
        print(my_list)

    def cast(self, arg):
        """Casts string to float or int"""
        try:
            if "." in arg:
                arg = float(arg)
            else:
                arg = int(arg)
        except ValueError:
            pass
        return arg

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if self.validation(arg, True, True):
            args = arg.split()
            _keys = args[0]+"."+args[1]
            match = args[3]
            if args[2] in HBNBCommand.att_str:
                setattr(storage.all()[_keys], args[2], str(match))
            elif args[2] in HBNBCommand.att_int:
                setattr(storage.all()[_keys], args[2], int(match))
            elif args[2] in HBNBCommand.att_float:
                setattr(storage.all()[_keys], args[2], float(match))
            else:
                setattr(storage.all()[_keys], args[2], self.cast(match))
            storage.save()

    def count(self, arg):
        """Retrieves the number of instances in a class"""
        count = 0
        for key in storage.all():
            if arg[:-1] in key:
                count = count + 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
