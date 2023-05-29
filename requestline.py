import requests
import re

poem_number = '17'
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
    thisline = re.sub("\W","",thisline)
    thislength = len(thisline)
    if thislength < 50:
      print(thislength)
      if thislength < 25:
        thisarray.append(thisline)
        print(thisline)
      else:
        half = int(thislength/2)
        firsthalf = thisline[0:half-1]
        lasthalf = thisline[half-1:]
        thisarray.append(firsthalf)
        thisarray.append(lasthalf)
        print(firsthalf)
        print(lasthalf)
    else:
      print('too long!')
  bigarray.append(thisarray)

print(bigarray)     

def request_anagram_from_site(section):
  request_url = 'https://new.wordsmith.org/anagram/anagram.cgi?anagram=' + section + '&language=english&t=500&d=&include=&exclude=&n=&m=&a=n&l=n&q=n&k=1&source=adv'
  print(section)
  print(request_url)
  result = requests.get(request_url).text
  anagram_blob = re.search("(?sm)</script>\s*<b>[^<]*\sfound\.\s+Displaying[^<]*?</b>\s*<br>\s*(.*?)\s*<br>\s*<script>", result).group(1)
  anagram_list = anagram_blob.split('<br>\n')
  return anagram_list

linecount = 0
for thisline in bigarray[linecount:]:
    linecount += 1
    sectioncount = 0
    for thissection in thisline:
        sectioncount += 1
        outfilename = 'poem_' + poem_number + '_' + str(linecount) + '_' + str(sectioncount)
        print(outfilename)
        f  = open(outfilename,'w')
        f.write('Original section: ' + thissection + '\n')
        anagram_list = request_anagram_from_site(thissection)
        print(anagram_list)
        print('************')
        for thisanagram in anagram_list:
          print('----------------')
          print(thisanagram)
          f.write(thisanagram + '\n')
        print('----------------')
        f.close()

