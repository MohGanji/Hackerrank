arr=(`cat /dev/stdin`)
export LC_COLLATE=C
for (( i=0;i<${#arr[@]};i++ ));do
    arr[i]=`echo ${arr[i]} | sed 's/[A-Z]/./'`
done
echo ${arr[@]}
