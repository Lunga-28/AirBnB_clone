#!/usr/bin/python3
"""
A module that has crucial command interpreter
for all AirBnB files related to this project
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models import storage, allclasses
from datetime import datetime

from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex
import re

class HBNBCommand(cmd.Cmd):
    """
    this class inherits from cmd
    """
    prompt = '(hbnb) '
    classes = allclasses

def do_create(self, args):
    """
    Creates and saves an instance of a given class
    """
    if not args:
        print("** class name missing **")
        return
    
    tokens = args.split(" ")
    
    class_mappings = {
        "BaseModel": BaseModel,  # Add other class names and corresponding classes here
        # "OtherClass": OtherClass,
    }
    
    class_name = tokens[0]
    
    try:
        new_instance = class_mappings[class_name]()
        new_instance.save()
        print("{}".format(new_instance.id))
    except KeyError:
        print("** class doesn't exist **")


def do_destroy(self, args):
    """
    Deletes an instance based on class name and id
    """

    if not args:
        print("** class name missing **")
        return

    tokens = args.split(" ")

    if tokens[0] not in self.classes:
        print("** class doesn't exist **")
        return

    if len(tokens) < 2:
        print("** instance id missing **")
        return

    class_name = tokens[0]
    instance_id = tokens[1]
    instance_key = "{}.{}".format(class_name, instance_id)

    objects = storage.all()
    if instance_key not in objects:
        print("** no instance found **")
        return

    del objects[instance_key]
    storage.save()

    def do_all(self, args):
        objects = storage.all()
        instances = []
        if not args:
            for name in objects:
                instances.append(objects[name])
            print(instances)
            return
        tokens = args.split(" ")
        if tokens[0] in self.classes:
            for name in objects:
                if name[0:len(tokens[0])] == tokens[0]:
                    instances.append(objects[name])
            print(instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Make updates based on name and id).
        """
        if not args:
            print("** class name missing **")
            return
        tokens = args.split(" ")
        objects = storage.all()
        if tokens[0] in self.classes:
            if len(tokens) < 2:
                print("** instance id missing **")
                return
              
            name = tokens[0] + "." + tokens[1]
            if name not in objects:
                print("** no instance found **")
            else:
                obj = objects[name]
                untouchable = ["id", "created_at", "updated_at"]
                if obj:
                    token = args.split(" ")
                    if len(token) < 3:
                        print("** attribute name missing **")
                    elif len(token) < 4:
                        print("** value missing **")
                    elif token[2] not in untouchable:
                        obj.__dict__[token[2]] = token[3]
                        obj.updated_at = datetime.now()
                        storage.save()
                      
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        tokens = args.split()
        objects = storage.all()
        try:
            if len(tokens) == 0:
                print("** class name missing **")
                return
            if tokens[0] in self.classes:
                if len(tokens) > 1:
                    key = tokens[0] + "." + tokens[1]
                    if key in objects:
                        obj = objects[key]
                        print(obj)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except AttributeError:
            print("** instance id missing **")

  
    def default(self, args):
        """
        just default methods
        """
        s = (args.replace('.', ' ').replace('(', ' ').replace(')', ' '))
        tok = s.split()
        if len(tok) > 1:
            cmd = tok.pop(1)
        if '{' in s and cmd == 'update':
            s = s.replace('update', '')
            dic = re.split(r"\s(?![^{]*})", s)
            for key, val in eval(dic[3]).items():
                arg = tok[0] + ' ' + tok[1][:-1] + ' ' + key + ' ' + str(val)
                self.do_update(arg)
            return
          
        arg = ' '.join(tok).replace(',', '')
        try:
            eval('self.do_' + cmd + '(arg)')
        except:
            print("** invalid command **")

  
def do_count(self, args):
    """
    Counts the number of instances of a class
    """
    objects = storage.all()

    if args in self.classes:
        count = sum(1 for name in objects if name.startswith(args))
        print(count)
    else:
        print("** class doesn't exist **")

    def do_quit(self, args):
        """
        exits the command interpreter
        """
        quit()

    def do_EOF(self, args):
        quit()

    def do_help(self, args):
        """
        lists all commands and help details
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        return

if __name__ == "__main__":
    HBNBCommand().cmdloop()
