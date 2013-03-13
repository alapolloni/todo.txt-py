
import os
import sys
import re

def readfile():
  f=open(r'C:\Users\aapollon\Documents\My Dropbox\TaskPaper\todo.txt','r')
  #x=f.read()
  #print "x"+x
  return f.read()

def printx():
  print readfile()
  return

def _list(FILE,TERMS):
  print "def _list"
  print "FILE:",FILE
  print "TERMS:",TERMS
  if os.path.isfile(FILE): src=FILE
  elif os.path.isfile(FILE): src=FILE
  else: sys.exit("TODO: File"+FILE+"does not exit")
    
  ## Get our search arguments, if any
  #TODO: 

  ## Prefix the filter_command with the pre_filter_command
  #TODO: filter_command="${pre_filter_command:-}"
 
  #f=open(r'C:\Users\aapollon\Documents\My Dropbox\TaskPaper\todo.txt','r')
  f=open(FILE,'r')
  SRC=f.readlines()

  ## Figure out how much padding we need to use
  ## We need one level of padding for each power of 10 $LINES uses
  LINES=len(SRC)
  PADDING=len(str(LINES))

  for x in range(len(SRC)):
    #SRC[x]=str(x+1)+" "*PADDING+SRC[x]
    SRC[x]=str(x+1).zfill(PADDING)+" "+SRC[x]

  print SRC

  for TERM in TERMS:
    if re.match('-',TERM): 
      TERM=TERM[1:]
      print "return all without TERM:"+TERM
      SRC = filter (lambda a: not re.search(TERM,a), SRC)
    else:
      print "return all with TERM:"+TERM
      SRC = filter (lambda a: re.search(TERM,a), SRC)
  
  #print SRC

  for x in SRC:
    print x,

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
        completedLines.append(re.sub('^[Xx]','',line))
      else:
        todoLines.append(line)
  fTODO=open(TODO,'wb')
  for item in todoLines:
    fTODO.write("%s\n" % item)
  fDONE=open(DONE,'ab')
  if len(completedLines):#yes, there are completed lines so append to the done.txt"
    for item in completedLines:
     fDONE.write("%s\n" % item)

  
