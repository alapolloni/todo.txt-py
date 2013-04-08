# ya(yet another) todotxt python implementation   #
## WHAT and WHY ##
- Doesn't rely on any gnu programs 
- There's a windows .exe included for windows users who are interested but don't want or cannot installing/configure Cygwin.
- I wanted to learn python.
- Mostly a copy of todo.sh.

## Windows Installation ##
- Copy [todo.exe](todo.exe) your home directory (C:\Users\\{your login id\}\
- Follow these [instructions](/Notes/WindowsAliases.md)

## TODO/ISSUES ##
-  review the --help
-  add version info -V, -version
-  added sanity checks like in todo.sh
-  write a configuration file from current options
	-. this is a bigger pain that I assumed
-  go through todo.sh config file and add missing.
-  add e for edit todo.txt in editor
-  add instructions for doskey for aliases in windows
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
	- TODOTXT_DEFAULT_ACTION=""       run this when called with no arguments  
	- TODOTXT_SORT_COMMAND="sort ..." customize list output                   
	- TODOTXT_FINAL_FILTER="sed ..."  customize list after color, P@+ hiding  

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

## notes ##
### Configuration Value Precedence ###
1. Command line.
1. Config file that's name is declared on the command line.
1. Environment vars
1. Local config file (if exists)
1. Global config file (if exists)
1. Defaults set internally to the program.
