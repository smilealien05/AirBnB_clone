#!/usr/bin/python3
"""Defines a HBNBCommand class with console"""
import cmd
import shlex
import models
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class"""
    prompt = '(hbnb) '
    Cls = [
        'BaseModel', 'User', 'Amenity',
        'City', 'Place', 'Review', 'State']

    def do_create(self, line):
        """To create a new instance"""
        cls_name = self.parseline(line)[0]
        if not cls_name:
            print('** class name missing **')
        elif cls_name not in self.Cls:
            print("** class doesn't exist **")
        else:
            new_o = eval(cls_name)()
            new_o.save()
            print(new_o.id)

    def do_show(self, line):
        """Show the string representation of an instance"""
        args = shlex.split(line)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.Cls:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.Cls:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            clee = "{}.{}".format(commands[0], commands[1])
            if clee in objs:
                del objs[clee]; models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """show all instances based on obj name or not"""
        cls_name = self.parseline(line)[0]
        storage_engine = models.storage.all()
        if not cls_name:
            print([str(val) for val in storage_engine.values()])
        elif cls_name not in self.Cls:
            print("** class doesn't exist **")
        elif cls_name in self.Cls:
            str_list_obj = []
            for key, obj in storage_engine.items():
                if cls_name == key.split('.')[0]:
                    str_list_obj.append(str(obj))
            print(str_list_obj)

    def default(self, line):
        """method to handel commands"""
        if '.' in line:
            args = line.split('.')
            cls_name = args[0]
            com = args[1].split('(')
            mtd = com[0]
            id_att_val = com[1].split(')')[0]
            sep_all = id_att_val.split(',')
            avl = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
            }
            if mtd in avl.keys():
                if mtd != 'update':
                    return avl[mtd](f'{cls_name} {id_att_val}')
                else:
                    cls_id = sep_all[0]
                    cls_atr = sep_all[1]
                    atr_val = sep_all[2]
                    return avl[mtd](f'{cls_name} {cls_id} {cls_atr} {atr_val}')
            print("*** Unknown syntax: {}".format(line))
            return False
        print("*** Unknown syntax: {}".format(line))
        return False

    def do_count(self, line):
        """retrieve the number of instances of a class"""
        cls_name = self.parseline(line)[0]
        storage_engine = models.storage.all()
        counter = 0
        if not cls_name:
            print('** class name missing **')
        else:
            if cls_name in self.Cls:
                for obj in storage_engine.values():
                    if obj.__class__.__name__ == cls_name:
                        counter += 1
                print(counter)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = shlex.split(line)
        ArgsNum = len(args)
        if ArgsNum == 0:
            print('** class name missing **')
        elif args[0] not in self.Cls:
            print("** class doesn't exist **")
        elif ArgsNum == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            obj = models.storage.all().get(key)
            if obj is None:
                print('** no instance found **')
            elif ArgsNum == 2:
                print('** attribute name missing **')
            elif ArgsNum == 3:
                print('** value missing **')
            else:
                args[3] = self.cast_attr_type(args[3])
                setattr(obj, args[2], args[3])
                setattr(obj, 'updated_at', datetime.now())
                models.storage.save()

    def cast_attr_type(self, value):
        """Analyzes a parameter value for an update."""
        try:
            return float(value) if '.' in value else int(value)
        except ValueError:
            return value

    def emptyline(self):
        """Called when empty line + ENTER
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """To quit a program when 'EOF'"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

