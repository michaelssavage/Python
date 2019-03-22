#!/usr/bin/env python
import os,sys,subproces
import Cmd



class MyShell(Cmd):

	def __init__(self):
		super(MyShell,self).__init__()
		self.currentDir = str(os.getcwd())
		self.envVar = {"shell": self.currentDir, "PWD": str(os.getcwd())}
		os.environ
		os.environ.update(self.enr)

	def do_help(self,args):
		if len(args) == 0:
			print("My Shell Manual")
			print("-----------------")
			print("Usage:")
			print("./myshell.py [File containing commands]")
			pr:")
			print("All other commands entered into this shell will be treated as")
			print("executable files/commands")
			print("-----------------")
			print("")

	# Changes the current directory and updates the PWD environment variable
	def do_cd(self,newDir=""):
		#if empty then return the current dir	
		if len(newDir) == 0:
			print("PWD"))
			return
		try:
			os(newDir)
			os["PWD"] = newDir
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
			for content in os.path:
				print(content)
		except:
			pass

	def do_environ(self,env):
		"""Prints the CWD and PWD"""
		environ = os.environ
		print("-----------------")
			print(each + ": " + environ[each])
		print("-----------------")

	def do_echo(self,args):
		"""Prints the string out"""

	def do_pause(self,pause):
		"""Pauses the program until Enter is pressed."""
		try:
		except:
			pass

	def do_quit(self, quit):
		"""Quits the program."""
		print("Thanks for using MyShell. Come back soon!")

	def do_myshell(self,fileIn):
		"""Reads from a file"""
			fileIn = input("Enter the file name: ")

		with open(fileIn, "r") as file:
			try:
				for line in file:
					print(line.rstrip())
			except NameError as e:
				print("File input error")
		raise SystemExit

if __name__ == '__main__':
	shell.prompt = str(os.getcwd()) + ' >>> '
	shell.('Welcome. Type ? (or help) to list commands. Enter a command to begin.\n')
