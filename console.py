#!/usr/bin/env python3
"""
The console module.

Contains the entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class.

    Implements the command interpreter of the AirBNB project.
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the interpreter using the EOF Flag.
        """
        print()
        return True

    def do_quit(self, line):
        """Exit the interpreter using the quit command.
        """
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
