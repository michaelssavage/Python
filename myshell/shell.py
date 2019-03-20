#!/usr/bin/env python
import os,sys,subprocess
from cmd import Cmd



class MyShell(Cmd):

	def __init__(self):
		super(MyShell,self).__init__()
		self.currentDir = str(os.getcwd())
		self.envVar = {"shell": self.currentDir, "PWD": str(os.getcwd())}
		os.environ.clear()
		os.environ.update(self.envVar)

	def do_help(self,args):
		if len(args) == 0:
			print("My Shell Manual")
			print("-----------------")
			print("Usage:")
			print("./myshell.py [File containing commands]")
			print("-----------------")
			print("Commands:")
			print("dir [directory] - list directory content")
			print("clr - clear the current shell screen")
			print("environ - output the current environment variables")
			print("cd [target directory] - change current working directory")
			print("pause - pause execution in the shell until the user hits 'enter'")
			print("quit - quits the shell")
			print("echo [String] - prints the specified string to the shell")
			print("Other:")
			print("All other commands entered into this shell will be treated as")
			print("executable files/commands")
			print("-----------------")
			print("")

	# Changes the current directory and updates the PWD environment variable
	def do_cd(self,newDir=""):
		#if empty then return the current dir	
		if len(newDir) == 0:
			print(os.getenv("PWD"))
			return
		try:
			os.chdir(newDir)
			os.environ["PWD"] = newDir
			self.currentDir = os.getenv("PWD")
		except:
			print("The directory path *" + newDir + "* is invalid or does not exist.")

	def do_clr(self,clr):
		print("\033c")
		shell.cmdloop('Welcome. Type ? (or help) to list commands. Enter a command to begin.')
		return

	def do_dir(self,path):
		"""Lists the directory content"""
		try:
			if len(path) < 1:
				path = "."
			for content in os.listdir(path):
				print(content)
		except:
			print("The directory *" + path + "* is invalid or does not exist")

	def do_environ(self,env):
		"""Prints the CWD and PWD"""
		environ = os.environ
		print("-----------------")
		for each in environ:
			print(each + ": " + environ[each])
		print("-----------------")

	def do_echo(self,args):
		"""Prints the string out"""
		print(args)

	def do_pause(self,pause):
		"""Pauses the program until Enter is pressed."""
		try:
			input("Shell paused..Press Enter to continue")
		except:
			pass

	def do_quit(self, quit):
		"""Quits the program."""
		print("Thanks for using MyShell. Come back soon!")
		raise SystemExit

	def do_myshell(self,fileIn):
		"""Reads from a file"""
		if len(fileIn) == 0:
			fileIn = input("Enter the file name: ")

		with open(fileIn, "r") as file:
			try:
				for line in file:
					print(line.rstrip())
			except NameError as e:
				print("File input error")
		raise SystemExit

if __name__ == '__main__':
	shell = MyShell()
	shell.prompt = str(os.getcwd()) + ' >>> '
	shell.cmdloop('Welcome. Type ? (or help) to list commands. Enter a command to begin.\n')
