#!/bin/bash
FIRST=0
SECOND=0
for i in $* ; do
  if [ $i -eq 3 ]; then FIRST=1 ; fi
  if [ $i -eq 6 ]; then SECOND=1 ; fi
done
if [ $FIRST -eq 1 ] ; then
  if [ $SECOND -eq 1 ] ; then
    exit 1 # interesting
  fi
fi
exit 0


# this checks to see if the numbers are 3 and 6; if that's true, then it's interesting. 
# we want to check if the concatenation breaks the compilation; if that's true, it's interesting.