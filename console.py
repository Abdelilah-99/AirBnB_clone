#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    """Command HBNB class"""
    prompt = "(hbnb) "

    
    def do_create(self, args):
            list = args.split(" ")
            if (list[0] == ''):
                print("** class name missing **")
            elif list[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                my_model = BaseModel()
                my_model.save()
                print(my_model.id)
    def do_show(self, args):
        list = args.split(" ")
        
        if (list[0] == ""):
            print("** class name missing **")
        elif list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif list[1] == "":
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
            list = args.split(" ")
            if (len(list) == 0):
                print("** class name missing **")
            elif list[0] != "BaseModel":
                print("** class doesn't exist **")
            elif list[1] == "":
                print("** instance id missing **")
            else:
                my_model = BaseModel()
                my_model.save()
                print(my_model.id)
       
    
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