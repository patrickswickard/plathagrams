import requests
import re

poem_number = '14'
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

linecount = 17
for thisline in bigarray[linecount:]:
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
        myresult = result.text
        f  = open(outfilename,'w')
        #anagram_blob = re.search("(?m)</script>\s*<b>[^<]*\sfound\.\s+Displaying[^<]*</b>\s*<br>\s*(.*?)\s*<br>\s*<script>", myresult)
        anagram_blob = re.search("(?sm)</script>\s*<b>[^<]*\sfound\.\s+Displaying[^<]*?</b>\s*<br>\s*(.*?)\s*<script>", myresult).group(1)
        #anagram_blob = re.search("(?sm)</script>\s*<b>[^<]*\sfound\.\s+Displaying[^<]*?</b>\s*<br>\s*(.*)", myresult)
        #anagram_blob = re.search("<br>\s*(.*?)\s*<br>", myresult)
        #anagram_blob = re.search("(?m)(.*?)", myresult)
        print("THEBLOB1")
        print(anagram_blob)
        print('************')
        anagram_list = anagram_blob.split('<br>\n')
        for thisanagram in anagram_list:
          print('----------------')
          print(thisanagram)
          f.write(thisanagram + '\n')
          print('----------------')
        print("THEBLOB2")
        f.close()


