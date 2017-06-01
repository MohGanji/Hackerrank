read n
read -r a
a=$(echo $a|tr ' ' '\n')
echo "$a" | sort | uniq -u

