#!/bin/sh
cd `dirname $0`

dir_path="./parameters/*"
files=`find $dir_path`

for file in $files;
do
	cat $file | 
		python main.py | 
		python plot.py & 
done

