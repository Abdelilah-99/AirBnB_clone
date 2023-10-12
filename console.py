#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command HBNB class"""
    prompt = "(hbnb) "
    classes_list = ("BaseModel", "User", "State",
                    "City", "Amenity", "Place", "Review")

    @classmethod
    def print_id(self, class_name):
        """Call the class, then print its id"""
        my_model = class_name()
        my_model.save()
        print(my_model.id)

    def do_create(self, args):
        """Creates a new instance"""
        list = args.split(" ")
        if (list[0] == ''):
            print("** class name missing **")
        elif list[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
        else:
            if (list[0] == "BaseModel"):
                HBNBCommand.print_id(BaseModel)
            elif (list[0] == "User"):
                HBNBCommand.print_id(User)
            elif (list[0] == "State"):
                HBNBCommand.print_id(State)
            elif (list[0] == "City"):
                HBNBCommand.print_id(City)
            elif (list[0] == "Amenity"):
                HBNBCommand.print_id(Amenity)
            elif (list[0] == "Place"):
                HBNBCommand.print_id(State)
            else:
                HBNBCommand.print_id(Review)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        list = args.split(" ")

        if (list[0] == ""):
            print("** class name missing **")
        elif list[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
        elif len(list) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            is_found = False
            for obj_id in all_objs.keys():
                current_class, id = list[0], list[1]
                class_name, class_id = obj_id.split(".")
                if (current_class == class_name and id == class_id):
                    is_found = True
                    obj = all_objs[obj_id]
                    print(obj)
            if (not is_found):
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name"""
        list = args.split(" ")
        if (list[0] == ''):
            print("** class name missing **")
            return
        elif list[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return
        elif len(list) < 2:
            print("** instance id missing **")
            return

        key = list[0] + '.' + list[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        # Delete the instance
        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        list = args.split(" ")
        test_var = 0

        if (list[0] == '' and len(list) == 1):
            test_var = 1
            list_of_dics = []  # create empty dictionary
            all_objs = storage.all()  # get the storage
            for obj_id in all_objs.keys():  # loop through the storage
                list_of_dics.append(str(all_objs[obj_id]))

            print(list_of_dics)
        if len(list) > 0 and list[0] in HBNBCommand.classes_list:
            list_of_dics = []  # create empty dictionary
            all_objs = storage.all()  # get the storage
            for obj_id in all_objs.keys():  # loop through the storage
                class_name, class_id = obj_id.split(
                    ".")  # split the obj [basemodel].id
                if (class_name == list[0]):
                    list_of_dics.append(str(all_objs[obj_id]))
            print(list_of_dics)
        elif (len(list) > 0 and list[0] not in HBNBCommand.classes_list and test_var == 0):
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        list = args.split(" ")
        if (list[0] == ''):
            print("** class name missing **")
            return
        if list[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return
        if len(list) < 2:
            print("** instance id missing **")
            return

        if len(list) < 3:
            print("** attribute name missing **")
            return
        if len(list) < 4:
            print("** value missing **")
            return

        key = list[0] + '.' + list[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if (len(list) == 4):
            all_objs = storage.all()
            for key in all_objs:
                if (list[0] in HBNBCommand.classes_list):
                    class_name, class_id = key.split(".")
                    if list[0] == class_name and list[1] == class_id:
                        setattr(all_objs[key], list[2], list[3])

    def help_update(self, args):
        """Help page for the update"""
        print("update <class name> <id> <attribute name> '<attribute value>'")

    def do_quit(self, arg):
        """Quit the CLI"""
        return True

    def do_EOF(self, arg):
        """Quit the CLI"""
        return True

    def help_quit(self):
        """Quit the CLI"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Quit the CLI"""
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
