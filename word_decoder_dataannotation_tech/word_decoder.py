# Generate the numbers of the "pyramid" structure
def pyramid_numbers(max_num: int):
    i, diff = 1, 2
    while i <= max_num:
        yield i
        i += diff
        diff += 1

# Read the file, split the data into lines and build a dictionary
with open("coding_qual_input.txt", "r") as my_file:
    lines = my_file.read().strip().split("\n")

max_num = len(lines)
lines = [line.split() for line in lines]
dic = {int(key): value for key, value in lines}
# Create a list (sentence) by retrieving words from the dictionary based on the generated numbers
sentence = [dic[number] for number in pyramid_numbers(max_num)]

# Concatenate the words into a single string and print it
print(" ".join(sentence))



