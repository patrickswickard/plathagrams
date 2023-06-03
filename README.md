# plathagrams
utility files for poems by Latvia Sylph (Sylvia Plath anagrams)

This directory holds files related to my project of generating line-by-line anagrams of poems from Sylvia Plath's book of poems Ariel.

The problem is to generate and verify line-by-line anagrams of Plath poems.  I have been using the Internet Anagram Server as a source of anagrams.  This site takes requests of the form:

https://new.wordsmith.org/anagram/anagram.cgi?anagram=LINE_TO_ANAGRAM&language=english&t=500&d=&include=&exclude=&n=&m=&a=n&l=n&q=n&k=1&source=adv

The site has a character limit of 25 characters per anagram.  Some lines exceed this.  There's also quite a bit of latency, so it is useful to submit requests one after the other and create and verify the chosen anagrams later.

Eventually this may turn into useful tools so the user can generate their own anagrams efficiently.

UPDATE

So far we have two utility scripts

isanagram.rb  was previously written to take a file as input.  Each pair of lines in the file are expected to be anagrams of each other (odd-even lines).  This script tests and reports deficiencies.  Should port this to python.

requestline.py takes a file line-by-line, expecting each line to be <= 50 characters.  The Internet Anagram Server as stated above has a limit of 25 characters.  This program submits lines that are <= 25 characters directly to the anagram server and splits roughly in half lines of 26-50 characters.  The anagrams are gathered and spit out to files so that anagrams of the first and last halves can be combined into an anagram for the entire line.  This quickly overcomes the limitation above and makes the work of anagrammizing poems more efficient.

As a further improvement on this, we make two runs of anagrams.  The first run naively splits the line roughly in the middle as described.  Unfortunately the frequent use of common words has a tendency to "clutter up" the anagrams, often with the same repetitive words.  As an attempt to avoid this, the second strips common words ("a", "and", "the", etc) and submits only uncommon words to the anagram server for rearrangement.  The common words are preserved in a separate list (with any anagrams of their own) and presented alongside the anagrams of common words.  This allows for imposing roughly the "same structure" on the line if desired, which can lead to a Mad-Lib type effect.  The code for this is a work in progress, but early use indicates that this is greatly speeding up the process of choosing appropriate anagrams.
