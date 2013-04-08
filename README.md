# ya todotxt python implementation   #
## WHAT and WHY ##
- As a bone to windows users who are interested but don't want to waste time installing and configuring Cygwin:
- This one doesn't rely on any gnu programs 
- There's a windows .exe included. 
- I wanted to learn python.

## TODO ##
- <del>fix _list 
	- 	DONE Added -A for sort Alphabetically
	- 	DONE ignores date and case 
	- 	DONE-(sorta)fix listpri (needs _list to be fixed)</del>
-  <del>document due:XXXX-XX-XX and due:XXXX-XX-XX XX:XX</del>
-  <del>make for the .exe</del>
-  <del>add due:tomorrow, and the week days</del>
-  <del>put due:day in a def so that it can be called from anywhere, specifically append.</del>

-  <del>del ITEM# is out of range = nice error</del>
-  <del>del ITEM# TERM, just delete the TERM from the item : this was already done</del>
-  <del>append: check ITEM# is an integer and within range.</del>
-  <del>test for tododir,etc and set home and default location/files</del>
-  <del>look for the config file in a default TODO.sh-ish location.</del>
-  added sanity checks
-  write a configuration file from current options
	-. this is a bigger pain that I assumed
-  go through todo.sh config file and add missing.
-  add e for edit todo.txt in editor
-  add instructions for doskey for aliases in windows
-  add PV add-on (project view) 
-  add birdseye and stuff 
-  stuff I might do later
	- -P ( hide priority (x) labels.
	- -@
	- -+
	- -vv
	- -V
	- -x
	- TODOTXT_DEFAULT_ACTION=""       run this when called with no arguments  
	- TODOTXT_SORT_COMMAND="sort ..." customize list output                   
	- TODOTXT_FINAL_FILTER="sed ..."  customize list after color, P@+ hiding  

## notes ##
### Configuration Value Precedence ###
1. Command line.
1. Config file that's name is declared on the command line.
1. Environment vars
1. Local config file (if exists)
1. Global config file (if exists)
1. Defaults set internally to the program.



## DONE ##
1. DONE: <del>add one command line option (not action)</del>
1. DONE: add one configuration file
2. DONE: add one environment variables
2. DONE: all the command line options - need a list
	- -f TODOTXT_FORCE - done
	- -a TODOTXT_AUTO_ARCHIVE 
	- -v TODOTXT_VERBOSE - done
	- -d TODOTXT_CFG_FILE -done 
	- -p TODOTXT_PLAIN -done
	- -n PRESERVE_LINE_NUMBERS -done
	- -t TODOTXT_DATE_ON_ADD=1 -done 
