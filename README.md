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
2. all the command line options - need a list
	- TODOTXT_FORCE
	- TODOTXT_AUTO_ARCHIVE 
	- TODOTXT_VERBOSE - done
1. configuration file
1. add needs verbosity
1. do needs verbosity
1. document due:XXXX-XX-XX and due:XXXX-XX-XX XX:XX
1. add PV add-on  (project view)
1. make for the .exe
2. add due:tomorrow, and the week days
3. del ITEM# is out of range = nice error
4. del ITEM# TERM, just delete the TERM from the item

## notes ##
### Configuration Value Precedence ###
1. Command line.
1. Config file that's name is declared on the command line.
1. Environment vars
1. Local config file (if exists)
1. Global config file (if exists)
1. Defaults set internally to the program.


