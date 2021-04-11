# Copy test codes here

https://www.geeksforgeeks.org/python-string-strip/
Python string | strip()

**strip()** is an inbuilt function in Python programming language that returns a copy of the string with both leading and trailing characters removed (based on the string argument passed).

Syntax:
string.strip([chars])

Parameter: 
There is only one optional parameter in it:
1)chars - a string specifying the set of characters to be removed. 

***If the optional chars parameter is not given, all leading 
and trailing whitespaces are removed from the string.*** 

Return Value:
Returns a copy of the string with both leading and trailing characters removed.

\-\-\-  

# Q what is stdin and stdout stand for.  

https://stackoverflow.com/questions/8980520/can-anyone-give-me-a-quick-tutorial-in-stdin-and-stdout-in-python-3#:~:text=When%20you%20run%20your%20Python,for%20standard%20error%20(STDERR).&text=After%20these%20two%20lines%20the,now%20in%20the%20str%20data%20.

 * When you run your Python program, **sys.stdin** is the file object connected to ***standard input (STDIN)***, **sys.stdout** is the file object for ***standard output (STDOUT)***, and **sys.stderr** is the file object for ***standard error (STDERR)***. ... After these two lines the input for your program is now in the **str data** .

\-  

 * stdin and stdout are file-like objects provided by the OS. In general, when a program is run in an interactive session, stdin is keyboard input and stdout is the user's tty, but the shell can be used to redirect them from normal files or piped output from and input to other programs.

 * **input()** is used to prompt the user for typed input. In the case of something like a programming puzzle, it's normally assumed that stdin is redirected from a data file, and when the input format is given it's usually best to use sys.stdin.read() rather than prompting for input with input(). input() is intended for interactive user input, it can display a prompt (on sys.stdout) and use the GNU readline library (if present) to allow line editing, etc.

 * **print()** is, indeed, the most common way of writing to stdout. There's no need to do anything special to specify the output stream. print() writes to sys.stdout if no alternate file is given to it as a file= parameter. 



