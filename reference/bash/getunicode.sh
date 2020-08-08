#!/usr/local/bin/bash

echo $(/usr/local/bin/bash --version)
# 2000 to 3000
#for i in {2000..3000};
#do
#  echo -e "${i}: \u${i}"
#done

for i in {200..300};
do
  echo -e "${i}: \u${i}0     \u${i}1     \u${i}2     \u${i}3     \u${i}4     \u${i}5     \u${i}6     \u${i}7     \u${i}8     \u${i}9"
done
