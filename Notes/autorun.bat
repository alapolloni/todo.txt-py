@echo off
REM This now links the alias 't' to 'todo.exe".  You should make sure that the path to todo.exe is the same as where you saved it.
@doskey t="%HOME%\todo.exe" $*
REM this links the alias 'tb' to todo.exe -@ .  This shows you all items without a context assigned to them.
@doskey tb="%HOME%\todo.exe "  ls -@
REM Via the environment variable, this sets the location of your todo files. 
set TODOTXT_DIR=%HOME%/Documents
REM this adds today's date to the item when you 1st add it.
set TODOTXT_DATE_ON_ADD=1
set TODOTXT_PLAIN=1
