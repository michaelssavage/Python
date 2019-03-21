## Manual

1. Explain the concepts of i/o redirection, the program environment, and background program execution. 
2. The manual MUST be named readme and must be a simple text document capable of being read by a standard Text Editor.

## Shell
1. All other command line input is interpreted as program invocation.
   which should be done by the shell forking and execing the programs as its own child processes.

2. The shell must support i/o-redirection on either or both stdin and/or stdout. 
   i.e. the command line: 
                        programname arg1 arg2 <inputfile> outputfile 
   
   will execute the program **programname** with arguments arg1 and arg2, the stdin FILE stream
   replaced by inputfile and the stdout FILE stream replaced by outputfile. 

   stdout redirection should also be possible for the internal commands: 
   
                        dir, environ, echo, & help. 
  
   With output redirection, if the redirection character is **>** then the outputfile is
   created if it does not exist and truncated if it does. If the redirection token is **>>** then
   outputfile is created if it does not exist and appended to if it does.

3. The shell must support background execution of programs. An ampersand (&) at the
   end of the command line indicates that the shell should return to the command line
   prompt immediately after launching that program.
