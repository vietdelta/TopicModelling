#!/bin/bash
input="/home/vietphan/linkfb3.json"
counter=100
while IFS= read -r line
do
  echo "$line"
  echo $counter
  scrapy crawl fb -a email="hoangvietntrobo@gmail.com" -a password="daicarom" -a page="$line" -a date="2019-11-01" -a lang="it" -o $counter.csv
  ((counter++))
done < "$input"
