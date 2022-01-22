#### PATTERN SEARCH ####

# what we want to do is to iterate through length of text, and;
# search each index if them are same as pattern's first index
# if yes; search through patterns second index and so on
#  we can do this with a nested for loop inside our first loop for "length of text" loop.
# if no; no need to iterate on our nested loop since we need to move on to the next index of the text
#  which means we need to break out of our nested loop

# !!!! for if yes;;
#           we need to count if the pattern digits are matching with the digits in text
#     we can store the count as a variable.
#       !!!!
#           count should be zeroed in every iteration since we count matching digits of pattern in
#                 specified part of the list; which mean we can put the count variable as 0 before our
#                       nested loop.

# i will design my loop as not case sensitive
# "i" need to be added to text to compare the next digits when we go back on top in our nested loop.


text = input('write a text: ')
pattern = input('what pattern to search?: ')
pattern_at_index = []

for i in range(len(text)):
    count = 0
    for j in range(len(pattern)):
        if pattern[j].lower() == text[i + j].lower():
            count += 1
        else:
            break
    if count == len(pattern):
        pattern_at_index.append(i)

print('you can find the pattern starting from the indexes; ', pattern_at_index)
