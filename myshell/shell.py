#!/usr/bin/env python
import os,sys,subprocess
from cmd import Cmd



class MyShell(Cmd):

	def __init__(self):
		#initialise the CWD and PWD.
		super(MyShell,self).__init__()
		self.currentDir = str(os.getcwd())
		self.envVar = {"shell": self.currentDir, "PWD": str(os.getcwd())}
		os.environ.clear()
		os.environ.update(self.envVar)

	def do_help(self,args):
		#large formatted help file that prints out information.
		print("")
		print("For specific help, type 'help [command]'.")
		print("Consider the accompanying manual for more information.")
		print("-----------------")
		print("List of Commands:")
		print("cd [directory] - change the current default directory to [directory].")
		print("clr - clear the shell screen.")
		print("dir [directory] - list the contents of directory [directory].")
		print("environ - list all the environment strings.")
		print("echo [comment] - display [comment] on the display.")
		print("pause - pause operation in the shell until 'Enter' is pressed.")
		print("quit - quit the shell.")
		print("myshell [filename] - file will be read and the shell will exit.")
		print("Other:")
		print("All other commands entered into this shell will be treated as")
		print("executable files/commands")
		print("-----------------")
		print("")

	# Changes the current directory and updates the PWD environment variable
	def do_cd(self,newDir=""):
			
		if len(newDir) == 0:
			print(os.getenv("PWD")) #if empty, then return the current dir
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
			if len(path) < 1: #if no directory given, current directory is used
				path = "."
			for content in os.listdir(path):
				print(content)
		except:
			print("The directory *" + path + "* is invalid or does not exist")

	#prints the CWD and PWD		
	def do_environ(self,env):
		
		environ = os.environ
		print("-----------------")
		for each in environ:
			print(each + ": " + environ[each])
		print("-----------------")

	#prints the string out followed by a newline character
	def do_echo(self,args):
		
		print(args+"\n")

	#pauses the program until Enter is pressed.
	def do_pause(self,pause):
		
		try:
			input("Shell paused..Press Enter to continue")
		except:
			pass

	#quits the program.
	def do_quit(self, quit):

		print("Thanks for using MyShell. Come back soon!")
		raise SystemExit

	#read commmands from a file e.g myshell instructions.txt
	def do_myshell(self,fileIn):
		
		if len(fileIn) == 0: #if filename not given, ask user for the filename.
			fileIn = input("Enter the file name: ")

		with open(fileIn, "r") as file:
			try:
				for line in file:
					output = os.popen(line).read()
					print(output)
			except:
				print("File input error")
		return

if __name__ == '__main__':
	shell = MyShell()
	shell.prompt = str(os.getcwd()) + ' >>> '
	shell.cmdloop('Welcome. Type help (or ?) to list commands. Enter a command to begin.\n')
