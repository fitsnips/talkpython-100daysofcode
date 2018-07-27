from collections import Counter, OrderedDict


# https://writing.colostate.edu/guides/teaching/fys/act3exparagraphs.cfm
sentence = "When I first brought my cat home from the Humane Society she was a mangy, pitiful animal. She " \
           "was so thin thatyou could count her vertebrae just by looking at her. Apparently she was " \
           "declawed by her previous owners, then abandoned or lost. Since she couldn't hunt, she nearly " \
           "starved. Not only that, but she had an abscess on one hip. The vets at the Humane Society had " \
           "drained it, but it was still scabby and without fur. She had a terrible cold, too. She was sneezing " \
           "and sniffling and her meow was just a hoarse squeak. And she'd lost half her tail somewhere. Instead " \
           "of tapering gracefully, it had a bony knob at the end."


my_list = sorted(sentence.split())

count =  Counter(my_list)

print(type(count))
print(count)


