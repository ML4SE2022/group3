for file in `ls *.java`
do
    echo "Processing $file"
    sed -i 's/\t/    /g' $file
done