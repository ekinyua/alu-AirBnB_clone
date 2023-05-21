#!/usr/bin/python3
"""model console"""
import cmd
import json
from models.base_model import BaseModel
import models

base = BaseModel()


def errores(x):
    """returns error messages
        - x: as argument identifier for error msg
    """
    errores = {1: "** class name missing **",
               2: "** class doesn't exist **",
               3: "** instance id missing **",
               4: "** no instance found **",
               5: "** name missing **",
               6: "** value missing **",
               7: "** attribute name missing **"
               }
    for key, item in errores.items():
        if key == x:
            print(item)


class HBNBCommand(cmd.Cmd):
    """Command example"""

    prompt = '(hbnb) '

    Class_dict = {'BaseModel'}

    @staticmethod
    def do_EOF(self, arg):
        """EOF signal to interrupt a file"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        if line == '':
            errores(1)
        elif line not in self.Class_dict:
            errores(2)
        else:
            obj = eval(line)()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        new_line = line.split()

        if new_line == '':
            errores(1)
        elif new_line[0] not in self.Class_dict:
            errores(2)
        elif len(new_line) < 2:
            errores(3)
        else:
            data = models.storage.all()
            key = "{}.{}".format(new_line[0], new_line[1])
            if key in data.keys():
                obj = data[key]
                print(obj)
            else:
                errores(4)

    def do_destroy(self, line):
        new_line = line.split()

        if new_line == '':
            errores(1)
        elif new_line[0] not in self.Class_dict:
            errores(2)
        elif len(new_line) < 2:
            errores(3)
        else:
            data = models.storage.all()
            key = "{}.{}".format(new_line[0], new_line[1])
            if key in data.keys():
                del data[key]
                models.storage._FileStorage__objects = data
                models.storage.save()
            else:
                errores(4)

    def do_all(self, line):
        new_line = line.split()
        data = models.storage.all()
        new_list = []
        if line == '':
            for key_ins, val_obj in data.items():
                new_list.append(str(val_obj))
            print(new_list)
        else:
            if new_line[0] not in self.Class_dict:
                errores(2)
            else:
                for key_ins, val_obj in data.items():
                    key_class = val_obj.to_dict()
                    if key_class['__class__'] == new_line[0]:
                        new_list.append(str(val_obj))

                print(new_list)

    def do_update(self, line):
        new_line = line.split()
        data = models.storage.all()

        if line == '':
            errores(1)
        elif new_line[0] not in self.Class_dict:
            errores(2)
        elif len(new_line) < 2:
            errores(3)
        elif len(new_line) < 3:
            errores(7)
        elif len(new_line) < 4:
            errores(6)
        else:
            key = "{}.{}".format(new_line[0], new_line[1])
            if key in data:
                """data_temp = data[key].to_dict()
                data_temp.update({new_line[2]: new_line[3]})
                new_instance = globals()[new_line[0]](**data_temp)
                new_instance.save()"""
                new_instance = data[key]
                setattr(new_instance, new_line[2], new_line[3])
            else:
                errores(4)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
