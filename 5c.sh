#!/bin/bash
ERROR_FOUND=0
# SECOND=0

echo $*
for i in $* ; do
  ./pngtest "$i".png
done



last_line=$( gcov *.c | tail -1 )
echo last_line

IFS='\v' read -r var1 var2 var3 <<< last_line

coverage=$(echo $var3 | cut -d'%' -f 1)

echo coverage

if [ coverage >=  29.13 ]; then ERROR_FOUND=1 ; fi 


if [ $ERROR_FOUND -eq 1 ] ; then 
    rm *.gcda pngout.png
    exit 1 # interesting
fi
rm *.gcda pngout.png
exit 0
