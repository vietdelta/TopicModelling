#!/bin/bash
input="/home/vietphan/linkfb.json"
counter=0
while IFS= read -r line
do
  echo "$line"
  echo $counter
  scrapy crawl fb -a email="mampoclone@gmail.com" -a password="daicarom" -a page="$line" -a date="2019-12-01" -a lang="it" -o $counter.csv
  ((counter++))
done < "$input"
