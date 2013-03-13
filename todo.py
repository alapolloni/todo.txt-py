#!/usr/bin/python -tt

#format rules
#https://github.com/ginatrapani/todo.txt-cli/wiki/The-Todo.txt-Format 


#local libs
import todolib.readfile

#standard libs
import argparse
#from argparse import RawTextHelpFormatter
import sys
import os
import re

print os.environ['HOME']
TODO_DIR=os.environ['HOME']+r'\Documents\python-class\todotxt'
TODO_FILE=TODO_DIR+"/todo.txt"
DONE_FILE=TODO_DIR+"/done.txt"
REPORT_FILE=TODO_DIR+"/report.txt"
TMP_FILE= TODO_DIR+"/todo.tmp"

TODOTXT_PRESERVE_LINE_NUMBERS = 1


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

def main():
  parser = argparse.ArgumentParser(description='Process some todos.',
                                   formatter_class=argparse.RawTextHelpFormatter) 
  list_of_choices=['list','ls','add','a','addto','append','app','archive','do',
                   'del','rm','pri','p']
  parser.add_argument(dest='actions',metavar='action', 
                      choices=list_of_choices,
                      help= "list|ls\n"
                      "add|a\n"
                      "addto\n"
                      'append|app  ITEM# "TEXT TO APPEND" \n'
                      'archive\n'
                      "do\n"
                      "del|rm\n"
                      'pri|p         ITEM#  PRIORITY'  )
  parser.add_argument(dest='remainingArguments',metavar='task number or description', 
                      nargs=argparse.REMAINDER,
                      help="remaining args help")
  args=parser.parse_args()
  print "actions:",args.actions
  print "args_remaintintAarguments",args.remainingArguments

  #action={args.actions:None}
  #print "action ",action

  #sys.exit("bye")

  for case in switch(args.actions):
    if case('list') or case ('ls'):
        print "list"
        todolib.readfile._list(TODO_FILE,args.remainingArguments)
        #todolib.readfile.printx()
        break
    if case('add') or case ('a'):
        print "add"
        todolib.readfile._add(TODO_FILE,args.remainingArguments)
        break
    if case('addto'):
        print "addto"
        destfile=args.remainingArguments.pop(0)  #pop the 1st item off the list as the file
        print "destfile:",destfile
        print "args_remaintintAarguments",args.remainingArguments

        if os.path.isfile(destfile):
          todolib.readfile._addto(destfile,args.remainingArguments)
        else:
          msg =  "TODO: Destination file " + destfile + " does not exist"
          sys.exit(msg)
        break
    if case('addm'):
        #TODO : figure this out on a unix box i guess
        print "addm not supported in windows"
    if case('archive'):
        todolib.readfile._archive(TODO_FILE,DONE_FILE)
        break
    if case('do'):
        print "do"
        for itemNum in args.remainingArguments:
          print "item:"+itemNum
          itemNum.replace(',','')  #if comma separated remove the comma,
          itemNum=int(itemNum)
          with open(TODO_FILE, "r") as source:
              lines = source.readlines()
          with open(TODO_FILE, "w") as source:
              lineCount=0
              for line in lines:
                  lineCount += 1
                  print lineCount," ",line,
                  if lineCount != itemNum: 
                    print "not it, write the line"
                    source.write(line)
                  elif re.match('^X',line, re.IGNORECASE):
                    print itemNum," is already marked as done"
                    source.write(line)
                  else:
                    #source.write(re.sub(r'^# deb', 'deb', line))
                    print "do the line"
                    line="X "+line
                    line=re.sub(r'\(.\)','',line)
                    print "line ",line
                    source.write(line)
                    #TODO archive if set as default
        break

    if case('del','rm'):
        #print "delete"
        #print "TODO_FILE:",TODO_FILE
        linesDeleted=0
        for itemNum in args.remainingArguments:
          #print "item:"+itemNum
          itemNum.replace(',','')  #if comma separated remove the comma,
          itemNum=int(itemNum)
          with open(TODO_FILE, "r") as source:
            lines = source.readlines()
          source.close()
          #print "lines:",lines
          with open(TODO_FILE, "wb") as source:
            lineCount=0
            #print "lineCount",lineCount
            for line in lines:
              lineCount += 1
              #print lineCount," ",line,
              if lineCount != itemNum: 
                #print "not it, write the line"
                source.write(line)
              else:
                question = "\nDelete '"+line+"'? (Y/n)"
                var = raw_input(question)
                if var == 'Y': 
                  linesDeleted  += 1
                  print "You entered ", var, " deleted."
                  if  TODOTXT_PRESERVE_LINE_NUMBERS == 1:                 
                    line="\n"
                  else:
                    line=""
                else: 
                  print "You entered ",var," OK, not deleting."
                source.write(line)
        print "TODO: ",linesDeleted,"task(s) deleted"
        break
    if case('append','app'): 
      item = int(args.remainingArguments.pop(0))
      print item
      todolib.readfile._append(TODO_FILE,item,args.remainingArguments)
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
      break
    if case(): # default, could also just omit condition or 'if True'
      print "something else!"
      # No need to break here, it'll stop anyway

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()





