# yaya(yet another) todotxt python implementation   #
## WHAT and WHY ##
- Doesn't rely on any gnu programs 
- There's a windows .exe included for windows users who are interested but don't want or cannot installing/configure Cygwin.
- I wanted to learn python.
- Mostly a copy of todo.sh.

## Windows Installation ##
1. SAVE AS [todo.exe](todo.exe) to your home directory ( C:\Users\\{your login id\}\ )
2. Follow these [instructions](/Notes/WindowsAliases.md)
3. Open a new cmd.exe
4. Type: the letter *t*.  This will run the todo command.
5. Then: try *t help*
6. Then: *t add "read todo.txt help text"*
7. And then: *t ls*
4. Look at autorun.bat.  It should be self explanatory how to add more aliases and environment variables

If you are using an ANSI compatible Terminal as a replacement for Window's cmd.exe you should use the --ansi switch or set TODOTXT_ANSI=1 via an environtment variable or a Config file.

## TODO/ISSUES ##
-  review the --help output
-  add version info from -V, -version
-  add sanity checks like in todo.sh
-  add e for edit todo.txt in editor
-  add action add-on ability.  Like PV(project view) add-on. 
-  add birdseye and stuff 
-  multiple line add doesn't seem to work in windows.
-  listpri works but is a bit of a hack
-  stuff I might do later
	- -P ( hide priority (x) labels.
	- -@
	- -+
	- -V
	- -x
	
## DONE ##
- : add one command line option (not action)
- : add one configuration file
- : add one environment variables
- : all the command line options - need a list
	- -f TODOTXT_FORCE - 
	- -a TODOTXT_AUTO_ARCHIVE 
	- -v TODOTXT_VERBOSE - 
	- -d TODOTXT_CFG_FILE - 
	- -p TODOTXT_PLAIN -
	- -n PRESERVE_LINE_NUMBERS -
	- -t TODOTXT_DATE_ON_ADD=1 - 
	- -vv (extra verbose)
- fix _list 
	- 	 Added -A for sort Alphabetically
	- 	 ignores date and case 
	- 	-(sorta)fix listpri (needs _list to be fixed)
-  document due:XXXX-XX-XX and due:XXXX-XX-XX XX:XX
-  make for the .exe
-  add due:tomorrow, and the week days
-  put due:day in a def so that it can be called from anywhere, specifically append.
-  del ITEM# is out of range = nice error
-  del ITEM# TERM, just delete the TERM from the item : this was already 
-  append: check ITEM# is an integer and within range.
-  test for tododir,etc and set home and default location/files
-  look for the config file in a default TODO.sh-ish location.
-  add instructions for doskey for aliases in windows
-  Add Windows color for both ANSI Terminals and default cmd.exe.
	-    TODOTXT_COLOR_THEME & --ansi_theme {light,dark}
	-    TODOTXT_ANSI & --ansi


## notes ##
### Configuration Value Precedence ###
1. Command line.
1. Config file that's name is declared on the command line.
1. Environment vars
1. Local config file (if exists)
1. Global config file (if exists)
1. Defaults set internally to the program.


## Attribution ##
- All the colorization code came from https://github.com/abztrakt/ya-todo-py/blob/master/todo.py .
