#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd): 

    def do_quit(self, arg):
	return True

    def do_EOF(self, arg):
	return True

    def emptyline():
	return
if __name__ == '__main':
    HBNBCommand().cmdloop
