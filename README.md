# cariad's crypto challenge 2020 writeup

## first analysis

The first observation that I made was what the charset of the ciphertext was. The charset is every lowercase and uppercase letter, except "Q", "V", and "Z" and every number, except for "9". This seems to suggest that the occurrences of each letter is somewhat preserved.

## a breakthrough

To contrast this, a simple measure of the index of conincidence has some interesing results.
Taking a couple of books from Project Gutenberg, and cleaning up some of the characters so that they more closely follow the charset (replacing unicode quotes with ascii equivalents, 'æ' with 'ae'),
 something close the expected index of coincidence for general ascii text, 1.71.
The index of coincidence for the raw ciphertext is 0.6034086259384807, and assuming that uncompressed english is present in the plaintext, this means that a polyalphabetic substitution cipher has been used.

Since a polyalphabetic substitution cipher was expected, the first step I took was to determine the key size, i.e. period of the cipher.
Looking at the first 20 values for the delta bar IC (aggregate IC for n periodic alphabets), we get the following results:
d = 1: 0.6034086259384807
d = 2: 0.6031786104021015
d = 3: 0.7000061302158705
d = 4: 0.6031113394754609
d = 5: 0.6032799165967744
d = 6: 0.6994281955779581
d = 7: 0.6024438521068534
d = 8: 0.6026543338984898
d = 9: 0.6977575468839858
d = 10: 0.6022569206252385
d = 11: 0.6026724182495761
d = 12: 0.6998833772426155
d = 13: 0.947239895026965
d = 14: 0.6018011840339702
d = 15: 0.7003270749651656
d = 16: 0.6011219126322209
d = 17: 0.6011217822555345
d = 18: 0.6972876377386807
d = 19: 0.5985660498371375
Every third number is larger than the two before it, and in case 13 it jumps to 0.95, however even 0.95 is too low for the expected value of 1.71. Perhaps the product of 3 and 13 might be of interest.  
And it is of interest!, the delta bar IC for 39 is 1.69, which is close enough to the expected value.  
As a quick check, simple multiples of 39 give smaller values, for example, the delta bar IC for d=3*39=117 is 1.66, which is not any higher than 39, so 39 is perhaps the most likely key size

To be doubly sure, a kasiski analysis confirmed that repeating chunks of the ciphertext were always a multiple of 39 characters apart
(meaning that those sections had the same part of the key encrypting the same characters from the plaintext that repeated).

## unicity distance

The unicity distance is an approximation for how many characters are needed to crack a given cipher (given perfect cryptanalysis or cipher breaking methods) at a minimum. It works best for large values.

Here, I have determined the unicity distance for a general polyalphabetic substitution cipher of length 39 with 68 characters.

Assuming the rate of actual information for english is 1.5 bits per character, the redundancy is log2(68)-1.5 which is approximately 4.59 bits ber character. The entropy of the key length 39, assuming the worst case with all keys equally likely would be log2(factorial(68))*39 ~= 12500 bits of information. The unicity distance is thus 12500/4.59 ~= 2700 characters, and since the ciphertext is 17211 characters long it should not be too hard to crack without any prior knowledge of the key.

## The hard part

Now that I knew what the period of the cipher was, it was time for the hard part, the actual cryptanalysis.
I had a brief look at the frequency distribution, using matplotlib to plot the frequency of each ciphertext letter for each alphabet. One such alphabet is included here:

(IF YOU ARE SEEING THIS I FORGOT TO INCLUDE THE GRAPH)


from the image it is apparent that a simple viginere or beaufort variant was not used. Regardless, prior knowledge of the key is not necessary, given the volume of the ciphertext.

To actually crack a substitution cipher, it helps to start with the most frequenct characters, and try to work out the common short words first. Given that each graph has a single most common letter, I made the assumption that the most common letter is space (and given that they are all close the the fraction 1/6 of all characters that is observed in the example texts, this seems like a safe assumption).

Looking at the ordering of the spaces in the deciphered plaintext, it does seem like the length of individual words is approximately right, save for a long block near the beginning, and perhaps each time two words are seperated by a newline rather than a space

## first words

To make it easier to find words, and to decrypt the ciphertext once those words are found, I made a simple utility function that takes in a pair of a ciphertext index and suspected string that shows up in the plaintext. It takes those pairs, and turns them into elements of the final key. If it ever tries to overwrite part of the key, or re-write the same character in the key, it prints a warning.

To get the first words, I set the most common letters in the key after space to the first couple most common letters in the example text, this allowed me to find some of the common three letter words like "the"

## speeding up

At this point, the trick was to keep finding common words, with longer and less common words as more of the key is determined. At some point, I found that the most common letters in the key made more errors, so I went with the decductions from the words alone.

I made a function that found a specific word in the plaintext based on which matches the spaces, then the most amount of common letters.
Another that I made prints the statistics of a set of letters in the ciphertext, showing how close it is to the expected frequency for each letter in the predicted word that I provided.

These functions made it easier to find and check specific words in the plaintext.

I also eventually made a function that scores each possible place a word could show up in the ciphertext by the aggregate absolute difference between the frequency of each letter from the actual letter. By then I had determined that there were many occurences of the word "competition", so this allowed me to find many more occurrences, and really sped up the cracking.

## finishing off

Around this point, I knew that this text was about fanfiction (from the block of text without spaces at the start), and the occurrence of "Yoshi" and "Koopa Krusher" helped to find a bunch of the words, and I had also started to figure out some of the punctuation, and it looked like a url was at the start of the ciphertext, preceeded by `source: `
After a little more messing around to try and get more content of the url, it still seemed to have a large chunk missing from it, so I instead tried to search google for some of the content of the text, as I had already cracked multiple lengths of the key in certain places
When I looked the plaintext up in google, I wished that I had tried so earlier, since it was quick to find the original text at this url: `https://www.fanfiction.net/s/6267887/1/Yoshi-s-Glitz-Pit-Championship-Fight`  
which of course fits perfectly with what's already crackded.

After copying the text from the webpage, and replacing the ellipsis character with three periods, the automated key finder incorporates the text with no conflicts, and after the story you can read the following text:  

    If you have solved this puzzle then message me with "Yoshi is a horse because horses lay eggs". Thanks for solving =ariad's 2=2= Crypto Puzzle!
    
    = haven't done one of these in a few years namely due to medical issues and just overall needing to take a step back from things. However, I am super happy to see someone has solved this and I plan to make one again ne=t year. I hope you are well and please do let me know if you have solved it!
    8

which of course can be easily filled in to give:

    If you have solved this puzzle then message me with "Yoshi is a horse because horses lay eggs". Thanks for solving Cariad's 2020 Crypto Puzzle!
    
    I haven't done one of these in a few years namely due to medical issues and just overall needing to take a step back from things. However, I am super happy to see someone has solved this and I plan to make one again ne=t year. I hope you are well and please do let me know if you have solved it!
    8

