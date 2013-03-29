3/25/2013 11:47:55 AM tec# ya todotxt python implementation   #
## WHAT and WHY ##
- As a bone to windows users who are interested but don't want to waste time installing and configuring Cygwin:
- This one doesn't rely on any gnu programs 
- There's a windows .exe included. 
- I wanted to learn python.

## TODO ##
1. DONE: add one command line option (not action) 
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
1. fix _list 
	2. needs sort (ignore case)
	3. sort ignore date
	2. DONE-(sorta)- fix listpri (needs _list to be fixed)
1. document due:XXXX-XX-XX and due:XXXX-XX-XX XX:XX
2. added sanity checks
1. add PV add-on  (project view)
1. make for the .exe
2. add due:tomorrow, and the week days
3. del ITEM# is out of range = nice error
4. del ITEM# TERM, just delete the TERM from the item
1. write a configuration file
2. 5. look for the config file in a default TODO.sh-ish location.
5. stuff I dont care about and will do later
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


