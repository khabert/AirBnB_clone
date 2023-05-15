#!/usr/bin/env python3
"""
this is the console program
"""
import cmd
from models.base_model import BaseModel
from models import storage
import json
import shlex
from models.user import User

Class HBNBCommand(cmd.Cmd):
    """command to access models"""
    prompt = '(hbnb) '
    mydict  = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

    def do_nothing(self, arg):
        """it does nothing"""
        pass
    
    def do_quit(self, arg):
        """close the program amd saves"""
        return True

    def do_EOF(self, arg):
        """closes the program and saves with CTRl+D"""
        print ("")
        return True

    def emptyline(self):
        """does nothing on empty line + enter"""
        pass

    def do_create(self, arg):
        """creates a new istance of basemodel"""
        if not arg:
            print("** class name missing **")
            return
        mydata = shlex.split(arg)
        if mydata[0] not in HBNBCommand.mydict.keys():
            print("**class doesnt exist**")
            return
        newinstance = HBNBCommand.mydict[mydata[0]]()
        newinstance.save()
        print(newinstance.id)

    def do_show(slf, arg):
        """prints the string rep of an instance like [class name] [id]"""
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing**")
            return
        if tokens[0] not in HBNBCommand.mydict.keys():
            print("** class doesnt exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objdict = storage.all()
        key = tokens[0] + " " + tokens[1]
        if key in objdict:
            objinstance = str(objdict[key])
            print(objinstance)
        else:
            print("** no instance found **")


    def do_destroy(self, arg):
        """
        deletes an instance nased on name and id
        saving changes to JSON file
        """
        tokens = shelex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.mydict.keys():
            print("** instance id missing **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objdict = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in objdict[key]:
            del objgict[key]
            storage.save()
        else:
            print("** no instance found**")

    def do_all(self, arg):
        """prints all string reps of all instances with or without class names"""
        #printing the whole file
        storage.reload()
        myjson = []
        objectsdict = storage.all()
        if not arg:
            for key in objectsdict:
                myjson.append(str(objectsdict[key]))
            print(json.dumps(myjson))
            return
        token = shlex.split(arg)
        if token[0] in HBNBCommand.mydict.keys():
            for key in objectsdict:
                if token[0] in key:
                    myjson.append(str(objectsdict[key]))
            print(json.dumps(myjson))
        else:
            print("** class doesnt exist **")

    def do_update(self,arg):
        """
        updates instance based on class name and id
        (by using updating attribute)
        [class name] [id] [arg name] [arg nalue]
        """
        if not arg:
            print("** class name missing **")
            return
        mydata = shelex.split(arg)
        storage.reload()
        objdict = storage.all()
        if mydata[0] not in HBNBCommand.mydict.keys():
            print("** class doesnt exist **")
            return
        try:
            key = mydata[0] + "." + mydata[1]
            objsdict[key]
        except keyError:
            print("** no instance found **")
            return
        if (len(mydata) == 2):
            print("** attribute name missing **")
            return
        if (len(mydata) == 3):
            print("** value missing **")
            return
        myinstance = objsdict[key]
        if hasattr(myinstance, mydata[2]):
            datatype = type(getattr(myinstance, mydata[2]))
            setattr(myinstance, mydata[2], dtattype(mydata[3]))
        else:
            setattr(myinstance, mydata[2], mydata[3])
        storage.save()

    def do_update2(slf,arg):
        """
        updates instances based oc class name and id by add or 
        update attribute [class name] [id] [dict]
        """
        if not arg:
            print("** class name missing **")
            return
        mydict = "{" + arg.split("{")[1]
        mydata = shlex.split(arg)
        storage.reload()
        objsdict = storage.all()

        if mydata[0] not in HBNBCommand.mydict.keys():
            print("** class doesnt exist**")
            return
        if len(mydata) == 1:
            print("** instance id missing **")
            return
        try:
            key = mydata[0] + "." + mydata[1]
            objsdict[ke]
        except KeyError:
            print("** no instance found **")
            return
        if mydict == "{":
            print("** attribute name missing ***")

        mydict = mydict.replace("\'", "\"")
        mydict = json.loads(mydict)
        myinstance = objsdict[key]
        for mykey in mydict:
            if hasattr(myinstance, mykey):
                datatype = type(getattr(myinstance, mykey))
                setattr(myinstance, mykey, mydict[mykey])
            else:
                setattr(myinstance, mykey, mydict[mykey])
        storage.save()

    def do_counter(self, arg):
        """ counts the number of instances of a class"""
        counter = 0
        objectsdict = storage.all()
        for key in objectsdict:
            if (arg in key):
                counter += 1
        print(counter)

    def default(self, arg):
        """handles new inputting of data ways"""
        valdict = {"all": self.do_all, "count": self.do_count, "show": self.do_show, "destroy": self.do_destroy, "update": self.do_update}
        arg = arg.strip()
        values = arg.split(".")
        if len(values) != 2:
            cmd.Cmd.default(self, arg)
            return
        classname = values[0]
        command = values[1].split("(")[0]
        line = ""
        if (command == "update" and values[1].split("(")[1][-2] == "{"):
            inputs = values[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = classname + " " + line
            self.do_update2(line.strip())
            return
        try:
            inputs = values[1].split("(")[1].split(",")
            for num in range(len(input)):
                if (num != len(inputs) -1):
                    line = line + " " + shlex.split(inputs[num])[0]
                else:
                    line = line + " " + shlex.split(inputs[num][0:-1])[0]
        except IndexError:
            inputs = ""
            line = classname + line
            line = classname + line
            if (command in valdict.keys()):
                valdict[command](line.strp())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
