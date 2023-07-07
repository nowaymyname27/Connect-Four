

# Set the directory path where the folders should be created
directory="/Users/Galock/Desktop/BU/Fall 2023/CS 112 - Summerpack/Labs"

# Loop through numbers 1 to 10 and create folders named lab1 to lab10
for i in {1..10}
do
  mkdir "$directory/lab$i"
done
