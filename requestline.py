import requests
import re

poem_number = '23'
poemfilename = 'spsidebyside' + str(poem_number) + '.txt'
with open(poemfilename, 'r') as file:
    thisfile = file.read().split('\n')

def standard_split(thisline):
  thisarray = []
  if thisline:
    thisline = re.sub("\W","",thisline)
    thislength = len(thisline)
    half = int(thislength/2)
    if thislength >= 50:
      print('too long!')
    #print(thislength)
    if thislength < 25:
      firsthalf = thisline
      lasthalf = ''
    else:
      firsthalf = thisline[0:half-1]
      lasthalf = thisline[half-1:]
  else:
    firsthalf = ''
    lasthalf = ''
  thisarray.append(firsthalf)
  thisarray.append(lasthalf)
  return thisarray

def common_split(thisline):
  common_word_set = {'a','an','and','the','are','is','there','as','because','of','like','where'}
  thisarray = []
  common_list = []
  uncommon_list = []
  uncommon_string = ''
  thisline_stripped = re.sub(r'[^\w\s]','',thisline.lower())
  thisline_words = thisline_stripped.split(' ')
  common_word_list = []
  uncommon_word_list = []
  for thisword in thisline_words:
    if thisword in common_word_set:
      #print('************************')
      #print(thisword + ' is a common word!')
      #print('************************')
      common_word_list.append(thisword)
    else:
      #print('************************')
      #print(thisword + ' is an uncommon word!')
      #print('************************')
      uncommon_word_list.append(thisword)
  print('LISTON****************')
  print(common_word_list)
  common_word_string = ' '.join(common_word_list).lower()
  print(common_word_string)
  uncommon_word_string = ''.join(uncommon_word_list).lower()
  print(uncommon_word_list)
  print(uncommon_word_string)
  print('LISTOFF****************')
  thisline_rejoined = ' '.join(thisline_words).lower()
  #print(thisline_rejoined)
  #common_split = standard_split(uncommon_string)
  common_split = standard_split(uncommon_word_string)
  common_final = ''
  #uncommon_list_final = ''
  common_firsthalf_final = common_split[0]
  common_lasthalf_final = common_split[1]
  #thisarray.append(uncommon_list_final)
  thisarray.append(common_word_string)
  thisarray.append(common_firsthalf_final)
  thisarray.append(common_lasthalf_final)
  return thisarray

def get_all_anagrams(thisline):
  thisarray = []
  standard_array = standard_split(thisline)
  common_array = common_split(thisline)
  for this_standard_array in standard_array:
    thisarray.append(this_standard_array)
  for this_common_array in common_array:
    thisarray.append(this_common_array)
  return thisarray


lineno = 10
bigarray = []
for thisline in thisfile:
  lineno += 1
  print(lineno)
  #thisarray = standard_split(thisline)
  thisarray = get_all_anagrams(thisline)
  bigarray.append(thisarray)

print(bigarray)     

def request_anagram_from_site(section):
  if section:
    request_url = 'https://new.wordsmith.org/anagram/anagram.cgi?anagram=' + section + '&language=english&t=500&d=&include=&exclude=&n=&m=&a=n&l=n&q=n&k=1&source=adv'
    print(section)
    print(request_url)
    try:
      result = requests.get(request_url).text
      anagram_blob = re.search("(?sm)</script>\s*<b>[^<]*\sfound\.\s+Displaying[^<]*?</b>\s*<br>\s*(.*?)\s*<br>\s*<script>", result).group(1)
      anagram_list = anagram_blob.split('<br>\n')
      return anagram_list
    except:
      return [section]
  else:
    return []

linecount = 9
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

