#!/bin/bash
str=$1
split1=(${str//// })
dir=${split1[1]}
file=${split1[2]}

split2=(${file//./ })
filename=${split2[0]}

mkdir -p Result/$dir/
python main.py $1 > Result/$dir/$filename.csv
