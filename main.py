#Aaron McKeown 2/19/17
#STATUS: working
#Answer: 5537376230

#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
fr = open('nums.txt', 'r')
text = fr.read()
text = text.replace('\n','')
a = []

for i in range(100):
    a.append(text[:50])
    text = text.replace(str(text[:50]), '')

summ = 0
for i in a:
     summ += int(i)
summ = str(summ)
print('The first ten digits of the sum are', summ[:10])
