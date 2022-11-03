#!/bin/bash
ERROR_FOUND=0
# SECOND=0

echo $*
for i in $* ; do
  ./pngtest "$i".png
done



last_line=$( gcov *.c | tail -1 )
echo last_line

if [ $? ==  1 ]; then ERROR_FOUND=1 ; fi 


if [ $ERROR_FOUND -eq 1 ] ; then 
    cat wireworld-backup.c > wireworld-original.c
    exit 1 # interesting
fi
cat wireworld-backup.c > wireworld-original.c
exit 0
