#!/bin/bash
ERROR_FOUND=0
# SECOND=0

echo $*
cat wireworld-original.c > wireworld-backup.c
for i in $* ; do
  cat patch."$i" | patch -p0 -b wireworld-original.c
done

gcc -c wireworld-original.c
if [ $? ==  1 ]; then ERROR_FOUND=1 ; fi 


if [ $ERROR_FOUND -eq 1 ] ; then 
    cat wireworld-backup.c > wireworld-original.c
    exit 1 # interesting
fi
cat wireworld-backup.c > wireworld-original.c
exit 0
