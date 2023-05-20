import requests

poem_number = '2'
poemfilename = 'spsidebyside' + str(poem_number) + '.txt'
with open(poemfilename, 'r') as file:
    thisfile = file.read().split('\n')

lineno = 0
bigarray = []
for thisline in thisfile:
  lineno += 1
  print(lineno)
  thisarray = []
  if thisline:
    thislength = len(thisline)
    if thislength < 50:
      print(thislength)
      if thislength <= 25:
        thisarray.append(thisline)
        print(thisline)
      else:
        half = int(thislength/2)
        firsthalf = thisline[0:half]
        lasthalf = thisline[half:]
        thisarray.append(firsthalf)
        thisarray.append(lasthalf)
        print(firsthalf)
        print(lasthalf)
    else:
      print('too long!')
  bigarray.append(thisarray)

print(bigarray)     

linecount = 0
for thisline in bigarray:
    linecount += 1
    sectioncount = 0
    for thissection in thisline:
        sectioncount += 1
        outfilename = 'poem_' + poem_number + '_' + str(linecount) + '_' + str(sectioncount)
        this_request_url = 'https://new.wordsmith.org/anagram/anagram.cgi?anagram=' + thissection + '&language=english&t=500&d=&include=&exclude=&n=&m=&a=n&l=n&q=n&k=1&source=adv'
        print(outfilename)
        print(thissection)
        print(this_request_url)
        result = requests.get(this_request_url)
        f  = open(outfilename,'w')
        f.write(result.text)
        f.close()


