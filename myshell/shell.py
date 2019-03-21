#!/usr/bin/env python
import os,sys,subprocess
from cmd import Cmd

class MyShell(Cmd):

	#initialise the CWD and PWD.
	def __init__(self):
		super(MyShell,self).__init__()
		self.currentDir = str(os.getcwd())
		self.envVar = {"shell": self.currentDir, "PWD": str(os.getcwd())}
		os.environ.clear()
		os.environ.update(self.envVar)

	#large formatted help file that prints out information.
	def do_help(self,args):
		if len(args) == 0:
			print("")
			print("-----------------")
			print("-Consider the accompanying manual for more information.")
			print("-For specific help, type 'help [command]'.")
			print("-----------------")
			print("List of Commands:")
			print("-cd [directory] - change the current default directory to [directory].")
			print("-clr - clear the shell screen.")
			print("-dir [directory] - list the contents of directory [directory].")
			print("-environ - list all the environment strings.")
			print("-echo [argument] - displays [arguments] on the display.")
			print("-pause - pauses operation in the shell until 'Enter' is pressed.")
			print("-quit - quits the shell.")
			print("-myshell [filename] - file will be read and then the shell will exit.")
			print("Other:")
			print("-All other commands entered into this shell will be treated as")
			print("-executable files/commands")
			print("-----------------")
			print("")
		else:
			try:
				func = getattr(self, 'help_' + args)
				func()
			except:
				print("The command *" + args + "* is invalid or does not exist.")

	def help_cd(self):
		print("")
		print("-cd [directory] - change the current default directory to [directory].")
		print("-if the [directory] argument is not given, the CWD is reported.")
		print("-This command will also change the PWD environment variable.")
		print("-Example: 'cd /home/ubuntu'")
		print("")

	def help_clr(self):
		print("")
		print("-clr - clear the shell screen.")
		print("-if clr has additional arguments, they are ignored.")
		print("")	

	def help_dir(self):
		print("")
		print("-dir [directory] - list the contents of directory [directory].")
		print("-if the [directory] argument is not given, the CWD contents are listed.")
		print("-Example: 'dir /home/ubuntu/Documents'")
		print("")

	def help_environ(self):
		print("")
		print("-environ - list all the environment strings.")
		print("-the CWD is listed, followed by the PWD.")
		print("-if environ has additional arguments, they are ignored.")
		print("")

	def help_echo(self):
		print("")
		print("-echo [argument] - displays [argument] on the display.")
		print("-if echo has no additional arguments, the following message is printed:")
		print("-'error: the echo command was given no arguments.'")
		print("")

	def help_pause(self):
		print("")
		print("-pause - pauses operation in the shell until 'Enter' is pressed.")
		print("-if pause has additional arguments, they are ignored.")
		print("")

	def help_quit(self):
		print("")
		print("-quit - quits the shell.")
		print("-if quit has additional arguments, they are ignored.")
		print("-On quitting, a message is printed:")
		print("-'Thanks for using MyShell. Come back soon!'")
		print("")

	def help_myshell(self):
		print("")
		print("-myshell [filename] - file will be read and then the shell will exit.")
		print("-the file is assumed to contain a set of command lines for the shell to process.")
		print("-if myshell is not given additional arguments, the following prompt appears:")
		print("-'Enter the file name: '")
		print("")

	# Changes the current directory and updates the PWD environment variable
	def do_cd(self,newDir=""):			
		if len(newDir) == 0:
			print("-----------------")
			print(os.getenv("PWD")) #if empty, then return the current dir
			print("-----------------")
			return
		try:
			os.chdir(newDir)
			os.environ["PWD"] = newDir
			self.currentDir = os.getenv("PWD")
		except:
			print("The directory path *" + newDir + "* is invalid or does not exist.")

	#clear the whole terminal screen.		
	def do_clr(self,clr):
		print("\033c")
		shell.cmdloop('Welcome. Type help (or ?) to list commands. Enter a command to begin.')
		return

	#lists the contents of the directory 	
	def do_dir(self,path):	
		try:
			print("-----------------")
			if len(path) < 1: #if no directory given, current directory is used
				path = "."
			for content in os.listdir(path):
				print(content)
			print("-----------------")
		except:
			print("The directory *" + path + "* is invalid or does not exist")

	#prints the CWD and PWD		
	def do_environ(self,env):		
		environ = os.environ
		print("-----------------")
		for each in environ:
			print(each + ": " + environ[each])
		print("-----------------")

	#prints the string out if args are given.
	def do_echo(self,args):
		print("-----------------")
		if len(args) == 0:
			print("error: the echo command was given no arguments.")			
		else:
			print(args.rstrip())
		print("-----------------")

	#pauses the program until Enter is pressed.
	def do_pause(self,pause):		
		try:
			input("Shell paused..Press Enter to continue")
		except:
			pass

	#quits the program.
	def do_quit(self, quit):
		print("")
		print("Thanks for using MyShell. Come back soon!")
		print("")
		raise SystemExit

	#read commmands from a file e.g myshell instructions.txt
	def do_myshell(self,fileIn):		
		if len(fileIn) == 0: 									#if filename not given, ask user for the filename.
			fileIn = input("Enter the file name: ")

		with open(fileIn, "r") as file:
			try:
				i = 1
				for line in file:
					print("Line {} contains: ".format(i) + line)
					if len(line) > 1:							#E.g if the line had dir [directory] it needs to be splitted.
						line = line.split()
						func = getattr(self, 'do_' + line[0])
						func(" ".join(line[1:]))
					else:
						func = getattr(self, 'do_' + line)		#Else is used when only one arg, e.g clr or environ
						func(line)
					i+=1
			except:
				print("File input error")
		return

if __name__ == '__main__':
	shell = MyShell()
	shell.prompt = str(os.getcwd()) + ' >>> '
	shell.cmdloop('Welcome. Type help (or ?) to list commands. Enter a command to begin.\n')
