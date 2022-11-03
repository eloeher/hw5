#!/bin/bash
ERROR_FOUND=0
# SECOND=0

echo $*
for i in $* ; do
  ./pngtest large-png-suite/"$i".png
done



last_line=$( gcov *.c | tail -1 )
echo last_line is: 
echo $last_line

IFS=' '


# coverage=$(echo $last_line | tr -d 'Lines executed:' | tr -d '% of 10606' )

coverage=${last_line:15:2}

echo coverage is
echo $coverage

if [ "$coverage" -ge  30 ]; then ERROR_FOUND=1 ; fi 


if [ $ERROR_FOUND -eq 1 ] ; then 
    rm *.gcda pngout.png
    exit 1 # interesting
fi
rm *.gcda pngout.png

exit 0
