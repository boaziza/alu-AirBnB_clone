#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit the console.

        Usage:
            quit
            q
            exit
        """
        return True

    do_q = do_quit
    do_exit = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()