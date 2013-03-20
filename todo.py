#!/usr/bin/python -tt

#format rules
#https://github.com/ginatrapani/todo.txt-cli/wiki/The-Todo.txt-Format 


#TODO
#all the options 
#environment variables
#


#standard libs
import argparse
#from argparse import RawTextHelpFormatter
import sys
import os
import re
import datetime

#TODO_DIR=os.environ['HOME']+r'\Documents\My Dropbox\Taskpaper'
TODO_DIR=os.environ['HOME']+r'\Documents\GitHub\todo.txt-py'
TODO_FILE=TODO_DIR+"/todo.txt"
DONE_FILE=TODO_DIR+"/done.txt"
REPORT_FILE=TODO_DIR+"/report.txt"
TMP_FILE= TODO_DIR+"/todo.tmp"

TODOTXT_PRESERVE_LINE_NUMBERS = 1
TODOTXT_VERBOSE = 1
TODOTXT_FORCE = 0 


# ANSI Colors
NONE         = ""
BLACK        = "\033[0;30m"
RED          = "\033[0;31m"
GREEN        = "\033[0;32m"
BROWN        = "\033[0;33m"
BLUE         = "\033[0;34m"
PURPLE       = "\033[0;35m"
CYAN         = "\033[0;36m"
LIGHT_GREY   = "\033[0;37m"
DARK_GREY    = "\033[1;30m"
LIGHT_RED    = "\033[1;31m"
LIGHT_GREEN  = "\033[1;32m"
YELLOW       = "\033[1;33m"
LIGHT_BLUE   = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN   = "\033[1;36m"
WHITE        = "\033[1;37m"
DEFAULT      = "\033[0m"

# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def readfile():
  f=open(r'C:\Users\aapollon\Documents\My Dropbox\TaskPaper\todo.txt','r')
  #x=f.read()
  #print "x"+x
  return f.read()

def printx():
  print readfile()
  return

def highlightPriority(matchobj):
  """color replacement function used when highlighting priorities"""
  """took this from https://github.com/abztrakt/ya-todo-py """

  PRI_A = YELLOW
  PRI_B = LIGHT_GREEN
  PRI_C = LIGHT_PURPLE
  PRI_X = WHITE
  LATE  = LIGHT_RED

  if (matchobj.group(1) == "(A)"):
      return PRI_A + matchobj.group(0) + DEFAULT
  elif (matchobj.group(1) == "(B)"):
      return PRI_B + matchobj.group(0) + DEFAULT
  elif (matchobj.group(1) == "(C)"):
      return PRI_C + matchobj.group(0) + DEFAULT
  else:
      return PRI_X + matchobj.group(0) + DEFAULT

def highlightLate(matchobj):
    """color replacement function used when highlighting overdue items"""
    due = date(int(matchobj.group(2)), int(matchobj.group(3)), int(matchobj.group(4)))
    if due <= date.today():
        return matchobj.group(1) + LATE + "{due: " + matchobj.group(2) + "-" + matchobj.group(3) + "-" \
        	+ matchobj.group(4) + "}" + DEFAULT + matchobj.group(5)
    else:
        return DEFAULT + matchobj.group(0) + DEFAULT

def highlightLate2(matchobj):
    """color replacement function used when highlighting overdue items with time"""
    due = datetime.datetime(int(matchobj.group(2)), int(matchobj.group(3)), int(matchobj.group(4)), \
    	int(matchobj.group(5)), int(matchobj.group(6)))
    if due <= datetime.datetime(*time.localtime()[0:5]):
        return matchobj.group(1) + LATE + "{due: " + matchobj.group(2) + "-" + matchobj.group(3) + "-" \
        	+ matchobj.group(4) + " " + matchobj.group(5) + ":" + matchobj.group(6) + "}" \
        	+ DEFAULT + matchobj.group(7)
    else:
        return DEFAULT + matchobj.group(0) + DEFAULT

def _list(FILE,TERMS):
  if os.path.isfile(FILE): src=FILE
  elif os.path.isfile(FILE): src=FILE
  else: sys.exit("TODO: File"+FILE+"does not exit")
    
  f=open(FILE,'r')
  SRC=f.readlines()

  ## Figure out how much padding we need to use
  ## We need one level of padding for each power of 10 $LINES uses
  LINES=len(SRC)
  PADDING=len(str(LINES))
  ## and add line numbers to the SRC
  for x in range(len(SRC)):
    #SRC[x]=str(x+1)+" "*PADDING+SRC[x]
    SRC[x]=str(x+1).zfill(PADDING)+" "+SRC[x]

  originalSRCLenth=len(SRC) 

  #each time through the FOR loop cuts down SRC
  for TERM in TERMS:
    if re.match('-',TERM): 
      TERM=TERM[1:]
      print "return all without TERM:"+TERM
      SRC = filter (lambda a: not re.search(re.escape(TERM),a), SRC)
    else:
      print "return all with TERM:"+TERM
      SRC = filter (lambda a: re.search(re.escape(TERM),a), SRC)
 
  #add colors 
  re_pri = re.compile(r".*(\([A-Z]\)).*") 
  re_late = re.compile(r"(.*)\{due: (....)-(..)-(..)\}(.*)")
  re_late2 = re.compile(r"(.*)\{due: (....)-(..)-(..) (..):(..)\}(.*)")
  re_anyext = re.compile(r"\{[^\}]*\}")

  #only after done, show the end results
  for item in SRC:
    #print re_pri.sub(highlightPriority,x),
    print re_late2.sub(highlightLate2, 
                       (re_late.sub(highlightLate, 
                                    re_pri.sub(highlightPriority, item)))),  
  print "TODO:", len(SRC), " of ", originalSRCLenth, " tasks shown"

def _add(FILE,TERMS):
  print "FILE:",FILE
  print "TERMS:",TERMS
  _addto(FILE,TERMS)

def _addto(FILE,TERMS):
  #TERMS needs to end up as one string
  print "FILE:",FILE
  print "TERMS:",TERMS
 
  input= " ".join(TERMS)
  input= "\n"+input
  print "input:",input
  with open(FILE, "ab") as fwrite:
    fwrite.write(input)
    fwrite.close()

def _append(FILE,itemNum,TERMS):
  #print "FILE:",FILE
  #print "itemNum:",itemNum
  #print "TERMS:",TERMS
 
  input= " ".join(TERMS)
  #print "input:",input

  with open(FILE, "r") as source:
    lines = source.readlines()
  with open(FILE, "wb") as source:
    lineCount=0
    for line in lines:
        lineCount += 1
        #print lineCount," ",line,
        if lineCount != itemNum: 
          #print "not it, write the line"
          source.write(line)
        else:
          #source.write(re.sub(r'^# deb', 'deb', line))
          #print "append to the line"
          line=line.rstrip('\n')+" "+input+'\n'
          #print "line ",line
          source.write(line)
 
def _archive(TODO,DONE):
  completedLines=[]
  todoLines=[]
  for line in open(TODO,'rb'):
    line=line.rstrip()
    if line: #else, removes empty lines
      if re.match('x',line,re.IGNORECASE):
        completedLines.append(line)
      else:
        todoLines.append(line)
  fTODO=open(TODO,'wb')
  for item in todoLines:
    fTODO.write("%s\n" % item)
  fDONE=open(DONE,'ab')
  if len(completedLines):#yes, there are completed lines so append to the done.txt"
    for item in completedLines:
     fDONE.write("%s\n" % item)

def main():
  parser = argparse.ArgumentParser(description='Process some todos.',
                                   formatter_class=argparse.RawTextHelpFormatter) 
  list_of_choices=['list','ls','add','a','addto','append','app','archive','do',
                   'del','rm','depri','dp','help','listall','lsa','listcon','lsc',
                   'listfile','lsf','listpri','lsp','listproj','lsprj', 
                   'move','mv','prepend','prep','pri','replace','p']
  parser.add_argument(dest='actions',metavar='action', 
                      choices=list_of_choices,
                      help= 
                      'add|a "THING I NEED TO DO +projeect @context"\n'
                      'addto DESTFILE "TEXT TO ADD"\n'
                      'append|app  ITEM# "TEXT TO APPEND" \n'
                      'archive\n'
                      'command [ACTIONS]\n'
                      "del|rm ITEM# [TERM]\n"
                      "dp|depri ITEM#[, ITEM#, ITEM#, ...]\n"
                      "do ITEM#[, ITEM#, ITEM#, ...]\n"
                      "help\n"
                      "list|ls [TERM]\n"
                      "listall|lsa [TERM]\n"
                      "listcon|lsc\n"
                      "listfile|lsf SRC [TERM...]\n"
                      'listpri|lsp [PRIORITY]\n'
                      'listproj|lsprj\n'
                      'move|mv ITEM# DEST [SRC]\n'
                      'prepend|prep ITEM# "TEXT TO PREPEND"\n'
                      'pri|p ITEM#  PRIORITY\n'  
                      'replace ITEM# "TEXT TO REPLACE"\n'
                      )
                      #TODO
                      #help
                      #report
  parser.add_argument(dest='remainingArguments',metavar='task number or description', 
                      nargs=argparse.REMAINDER,
                      help="remaining args help")
  args=parser.parse_args()
  #print "actions:",args.actions
  #print "args_remaintintAarguments",args.remainingArguments

  for case in switch(args.actions):
    if case('list') or case ('ls'):
        _list(TODO_FILE,args.remainingArguments)
        break
    if case('listall','lsa'): 
        _list(TODO_FILE,args.remainingArguments)
        _list(DONE_FILE,args.remainingArguments)
        break
    if case('listcon','lsc'): 
        with open(TODO_FILE, "r") as source:
          lines = source.readlines()
        #find all the contexts and return them.  you get lists of lists
        alist=[re.findall('(\@\w+)[\s|\\n]',l) for l in lines]
        #squash the lists
        blist=[item for sublist in alist for item in sublist]
        #turn in to a set to get uniques and then back into a list
        clist=list(set(blist))
        for x in clist: print x
        break
    if case('listfile','lsf'): 
        SRC=args.remainingArguments.pop(0)  #pop the 1st item off the list as the file
        _list(SRC,args.remainingArguments)
        break    
    if case('listpri','lsp'):
        if len(args.remainingArguments) > 0 :
          PRI= args.remainingArguments.pop(0)
          if re.match('[A-Z|a-z]',PRI):
            PRI= PRI.upper()
            listPRI=[ '('+PRI+')' ]
            _list(TODO_FILE,listPRI)
          else:
            print 'usage: todo.sh listpri ITEM# PRIORITY\nnote: PRIORITY must be anywhere from A to Z.'
            break
        else:
          PRI='.'
          #TODO dont know how to fix this since _list does an escape on the TERM
          #and in this case, we don't want that.  this seems to be the ONLY case.
          #options
          #1, just cycle through the priorities...
          #2, do it yourself this one time
          #3, rething the escape...
          print "error: this doesn't do what you think it should"
          for i in range(ord('a'),ord('z')+1): 
            listPRI=[ '('+chr(i).upper()+')' ]
            _list(TODO_FILE,listPRI)
          break
        break    
    if case('listproj','lsprj'):
      with open(TODO_FILE, "r") as source:
        lines = source.readlines()
      #find all the projects and return them.  you get lists of lists
      alist=[re.findall('(\+\w+)[\s|\\n]',l) for l in lines]
      #squash the lists
      blist=[item for sublist in alist for item in sublist]
      #turn in to a set to get uniques and then back into a list
      clist=list(set(blist))
      for x in clist: print x
      break
    if case('move','mv'):
      # replace moved line with a blank line when TODOTXT_PRESERVE_LINE_NUMBERS is 1
      errmsg="usage: TODO mv ITEM# DEST [SRC]"
      if len(args.remainingArguments) > 0 : 
        itemNum = args.remainingArguments.pop(0)
      else: print errmsg;break
      if len(args.remainingArguments) > 0 : 
        dest=TODO_DIR +"/"+  args.remainingArguments.pop(0)
      else: print errmsg;break
      if len(args.remainingArguments) > 0 : 
        src =TODO_DIR +"/"+  args.remainingArguments.pop(0)
      else: src=TODO_FILE

      if not os.path.isfile(dest): sys.exit("TODO: Destination file "+dest+" does not exist") 
      if not os.path.isfile(src): sys.exit("TODO: Destination file "+src+" does not exist") 

      if re.match('(\d+)',itemNum):
        itemNum=int(itemNum)-1
      else:
        sys.exit(errmsg) 

      with open(src, "r") as source:
        lines = source.readlines()
      if (len(lines)<itemNum): 
        sys.exit( '{0}:No such item in {1}'.format(itemNum+1, src))

      question = 'Move {0} from {1} to {2}? (Y/n)'.format(lines[itemNum],src,dest)
      if TODOTXT_FORCE == 0:
        answer = raw_input(question)
      else:
        answer = 'Y'

      if answer == 'Y': 
        if TODOTXT_PRESERVE_LINE_NUMBERS == 0:
          #delete line numbers
          line=[]
          line.append(lines.pop(itemNum).strip('\n'))
        else:
          #preserve lines numbers
          line=[]
          line.append(lines[itemNum].strip('\n'))
          lines[itemNum]='\n'
        _add(dest,line)
        with open(src, "wb") as file:
          file.writelines(lines)
      break
    if case('prepend','prep','replace'):
      action = args.actions
      itemNum = args.remainingArguments.pop(0)  #pop the 1st item off the list as the file
      if re.match('\d+',itemNum):
        itemNum=int(itemNum)-1 #convert to list index
      else:
        sys.exit ("Error: need ITEM#")
      TEXT = " ".join(args.remainingArguments)
      with open(TODO_FILE, "r") as source:
        lines = source.readlines()
      TODO=lines[itemNum]

      # Retrieve existing priority and prepended date
      mTODO=re.search('(\([A-Z]\) ){0,1}(\d{4}-\d{2}-\d{2}){0,1}(.*)',TODO)
      if mTODO.group(1) is None:
        priority=''
      else:
        priority=mTODO.group(1)
      #prepdate=mTODO.group(2)
      # If the replaced text starts with a date, it will replace the existing
      # date, too.
      nTEXT=re.search('(\d{4}-\d{2}-\d{2}){0,1}(.*)',TEXT)
      if mTODO.group(2) is None or nTEXT.group(1) is not None:
        prepdate=''
      else:
        prepdate=mTODO.group(2)+" "
      if action == 'replace': 
        itemText=TEXT
      else:
        itemText=TEXT+" "+mTODO.group(3)

      newTEXT="{0}{1}{2}\n".format(priority,prepdate,itemText)
      if TODOTXT_VERBOSE == 1:
        print "{0} {1}".format(str(itemNum+1),TODO)
        print "TODO: Replaced task with"
        print "{0} {1}".format(str(itemNum+1),newTEXT)

      lines[itemNum]=newTEXT

      with open(TODO_FILE, "wb") as file:
        file.writelines(lines)

      break
    if case('add','a'):
        print "add"
        _add(TODO_FILE,args.remainingArguments)
        break
    if case('addto'):
        print "addto"
        destfile=args.remainingArguments.pop(0)  #pop the 1st item off the list as the file
        print "destfile:",destfile
        print "args_remaintintAarguments",args.remainingArguments

        if os.path.isfile(destfile):
          _addto(destfile,args.remainingArguments)
        else:
          msg =  "TODO: Destination file " + destfile + " does not exist"
          sys.exit(msg)
        break
    if case('addm'):
        #TODO : figure this out on a unix box i guess
        print "addm not supported in windows"
    if case('archive'):
        _archive(TODO_FILE,DONE_FILE)
        break
    if case('do'):
        with open(TODO_FILE, "r") as source:
          lines = source.readlines()

        for itemNum in args.remainingArguments:
          print "item:"+itemNum
          itemNum.replace(',','')  #if comma separated remove the comma,
          itemNum=(int(itemNum)-1)

          #completed must be a lower case x
          if re.match('^x',lines[itemNum]):
            print itemNum+1," ",lines[itemNum]," is already marked as done"
          elif itemNum <0:
            print itemNum+1," is less then 1"
          else:
            lines[itemNum]="x "+ datetime.date.today().strftime('%Y-%m-%d ') \
                            + lines[itemNum]
            lines[itemNum]=re.sub(r'\(.\)','',lines[itemNum])
            #TODO archive if set as default

        with open(TODO_FILE, "wb") as file:
          file.writelines(lines)
        break
    if case('del','rm'):
        #print "delete"
        #print "TODO_FILE:",TODO_FILE
        linesDeleted=0
        with open(TODO_FILE, "r") as source:
          lines = source.readlines()
        for itemNum in args.remainingArguments:
          #print "item:"+itemNum
          print "lines:",lines
          itemNum.replace(',','')  #if comma separated remove the comma,
          itemNum=int(itemNum)
          itemNum -= 1 #to match list index numbering
          question = "\nDelete '"+lines[itemNum]+"'? (Y/n)"
          var = raw_input(question)
          if var == 'Y': 
            linesDeleted += 1
            lines[itemNum]="\n"
            print "You entered ", var, " deleted."
          else: 
            print "You entered ",var," OK, not deleting."
        if  TODOTXT_PRESERVE_LINE_NUMBERS == 0: #then get rid of empty lines before 
        #writing need to do this afterwards because deleting within the for above 
        #for multiple deletes will mess up the index
          lines = [ line for line in lines if line != "\n"] 
        with open(TODO_FILE, "wb") as file:
          file.writelines(lines)
        print "TODO: ",linesDeleted,"task(s) deleted"
        break
    if case('append','app'): 
      item = int(args.remainingArguments.pop(0))
      print item
      _append(TODO_FILE,item,args.remainingArguments)
      break
    if case('pri','p'): # default, could also just omit condition or 'if True'
      ITEMNUM=int(args.remainingArguments.pop(0))  #pop the 1st item off the list as the file
      ITEMNUM -=1 #decrement to match list index, starts with zero
      PRIORITY=args.remainingArguments.pop(0)  #pop the 1st item off the list as the file
      if not re.match('[A-Z]',PRIORITY):
        print 'usage: todo.sh pri ITEM# PRIORITY\nnote: PRIORITY must be anywhere from A to Z.'
        break
      with open(TODO_FILE, "r") as source:
        lines = source.readlines()
      #get rid of the current Priority
      lines[ITEMNUM]=re.sub('^\(.\)','',lines[ITEMNUM])
      #add the new priority 
      lines[ITEMNUM]="(" + PRIORITY + ") " + lines[ITEMNUM] 
      with open(TODO_FILE, "wb") as file:
        file.writelines(lines)
      break
    if case('depri','dp'):
      with open(TODO_FILE, "r") as source:
        lines = source.readlines()
      tempITEMNUM=','.join(args.remainingArguments)
      ITEMNUMS=[int(x.strip()) for x in tempITEMNUM.split(',') if re.match('\d+',x)]
      print ITEMNUMS
      for ITEMNUM in ITEMNUMS:
        ITEMNUM -= 1 # to match the list index
        print ITEMNUM+1, lines[ITEMNUM]
        lines[ITEMNUM]=re.sub('^\(.\) ','',lines[ITEMNUM])
        print "TODO: ", ITEMNUM+1," deprioritized"
      with open(TODO_FILE, "wb") as file:
        file.writelines(lines)
      break
    if case('help'):
      #TODO oneline_usage 
      print """
		  Usage: $oneline_usage

		  Actions:
		    add "THING I NEED TO DO +project @context"
		    a "THING I NEED TO DO +project @context"
		      Adds THING I NEED TO DO to your todo.txt file on its own line.
		      Project and context notation optional.
		      Quotes optional.

		    addm "FIRST THING I NEED TO DO +project1 @context
		    SECOND THING I NEED TO DO +project2 @context"
		      Adds FIRST THING I NEED TO DO to your todo.txt on its own line and
		      Adds SECOND THING I NEED TO DO to you todo.txt on its own line.
		      Project and context notation optional.
		      Quotes optional.

		    addto DEST "TEXT TO ADD"
		      Adds a line of text to any file located in the todo.txt directory.
		      For example, addto inbox.txt "decide about vacation"

		    append ITEM# "TEXT TO APPEND"
		    app ITEM# "TEXT TO APPEND"
		      Adds TEXT TO APPEND to the end of the task on line ITEM#.
		      Quotes optional.

		    archive
		      Moves all done tasks from todo.txt to done.txt and removes blank lines.

		    command [ACTIONS]
		      Runs the remaining arguments using only todo.sh builtins.
		      Will not call any .todo.actions.d scripts.

		    del ITEM# [TERM]
		    rm ITEM# [TERM]
		      Deletes the task on line ITEM# in todo.txt.
		      If TERM specified, deletes only TERM from the task.

		    depri ITEM#[, ITEM#, ITEM#, ...]
		    dp ITEM#[, ITEM#, ITEM#, ...]
		      Deprioritizes (removes the priority) from the task(s)
		      on line ITEM# in todo.txt.

		    do ITEM#[, ITEM#, ITEM#, ...]
		      Marks task(s) on line ITEM# as done in todo.txt.

		    help
		      Display this help message.

		    list [TERM...]
		    ls [TERM...]
		      Displays all tasks that contain TERM(s) sorted by priority with line
		      numbers.  If no TERM specified, lists entire todo.txt.

		    listall [TERM...]
		    lsa [TERM...]
		      Displays all the lines in todo.txt AND done.txt that contain TERM(s)
		      sorted by priority with line  numbers.  If no TERM specified, lists
		      entire todo.txt AND done.txt concatenated and sorted.

		    listcon
		    lsc
		      Lists all the task contexts that start with the @ sign in todo.txt.

		    listfile SRC [TERM...]
		    lf SRC [TERM...]
		      Displays all the lines in SRC file located in the todo.txt directory,
		      sorted by priority with line  numbers.  If TERM specified, lists
		      all lines that contain TERM in SRC file.

		    listpri [PRIORITY]
		    lsp [PRIORITY]
		      Displays all tasks prioritized PRIORITY.
		      If no PRIORITY specified, lists all prioritized tasks.

		    listproj
		    lsprj
		      Lists all the projects that start with the + sign in todo.txt.

		    move ITEM# DEST [SRC]
		    mv ITEM# DEST [SRC]
		      Moves a line from source text file (SRC) to destination text file (DEST).
		      Both source and destination file must be located in the directory defined
		      in the configuration directory.  When SRC is not defined
		      it's by default todo.txt.

		    prepend ITEM# "TEXT TO PREPEND"
		    prep ITEM# "TEXT TO PREPEND"
		      Adds TEXT TO PREPEND to the beginning of the task on line ITEM#.
		      Quotes optional.

		    pri ITEM# PRIORITY
		    p ITEM# PRIORITY
		      Adds PRIORITY to task on line ITEM#.  If the task is already
		      prioritized, replaces current priority with new PRIORITY.
		      PRIORITY must be an uppercase letter between A and Z.

		    replace ITEM# "UPDATED TODO"
		      Replaces task on line ITEM# with UPDATED TODO.

		    report
		      Adds the number of open tasks and done tasks to report.txt.



		  Options:
		    -@
		        Hide context names in list output. Use twice to show context
		        names (default).
		    -+
		        Hide project names in list output. Use twice to show project
		        names (default).
		    -d CONFIG_FILE
		        Use a configuration file other than the default ~/.todo/config
		    -f
		        Forces actions without confirmation or interactive input
		    -h
		        Display a short help message
		    -p
		        Plain mode turns off colors
		    -P
		        Hide priority labels in list output. Use twice to show
		        priority labels (default).
		    -a
		        Don't auto-archive tasks automatically on completion
		    -n
		        Don't preserve line numbers; automatically remove blank lines
		        on task deletion
		    -t
		        Prepend the current date to a task automatically
		        when it's added.
		    -v
		        Verbose mode turns on confirmation messages
		    -vv
		        Extra verbose mode prints some debugging information
		    -V
		        Displays version, license and credits
		    -x
		        Disables TODOTXT_FINAL_FILTER


		  Environment variables:
		    TODOTXT_AUTO_ARCHIVE=0          is same as option -a
		    TODOTXT_CFG_FILE=CONFIG_FILE    is same as option -d CONFIG_FILE
		    TODOTXT_FORCE=1                 is same as option -f
		    TODOTXT_PRESERVE_LINE_NUMBERS=0 is same as option -n
		    TODOTXT_PLAIN=1                 is same as option -p
		    TODOTXT_DATE_ON_ADD=1           is same as option -t
		    TODOTXT_VERBOSE=1               is same as option -v
		    TODOTXT_DEFAULT_ACTION=""       run this when called with no arguments
		    TODOTXT_SORT_COMMAND="sort ..." customize list output
		    TODOTXT_FINAL_FILTER="sed ..."  customize list after color, P@+ hiding
	EndHelp


      """
      break
    if case(): # default, could also just omit condition or 'if True'
      print "something else!"
      # No need to break here, it'll stop anyway

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()





