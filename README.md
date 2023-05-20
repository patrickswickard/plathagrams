# plathagrams
utility files for poems by Latvia Sylph (Sylvia Plath anagrams)

This directory holds files related to my project of generating line-by-line anagrams of poems from Sylvia Plath's book of poems Ariel.

The problem is to generate and verify line-by-line anagrams of Plath poems.  I have been using the Internet Anagram Server as a source of anagrams.  This site takes requests of the form:

https://new.wordsmith.org/anagram/anagram.cgi?anagram=LINE_TO_ANAGRAM&language=english&t=500&d=&include=&exclude=&n=&m=&a=n&l=n&q=n&k=1&source=adv

The site has a character limit of 25 characters per anagram.  Some lines exceed this.  There's also quite a bit of latency, so it is useful to submit requests one after the other and create and verify the chosen anagrams later.

Eventually this may turn into useful tools so the user can generate their own anagrams efficiently.
