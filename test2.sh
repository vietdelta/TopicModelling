#!/bin/bash
input="/home/vietphan/linkfb2.json"
counter=50
while IFS= read -r line
do
  echo "$line"
  echo $counter
  scrapy crawl fb -a email="hoangvietntrobo@gmail.com" -a password="daicarom" -a page="$line" -a date="2019-11-01" -a lang="it" -o $counter.csv
  ((counter++))
done < "$input"
