from collections import Counter
import re
from math import log
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce

fname = 'crypto_christmas_2020.txt'

with open(fname) as f:
    data = f.read()

with open('example.txt', encoding='utf-8') as f:
    example = f.read()

example = example.replace('‘', "'").replace('’', "'")
example = example.replace('“', '"').replace('”', '"')
example = example.replace('æ', 'ae')


pta = '''Yoshi's Glitz Pit Championship Fight, a mario fanfic | FanFiction

It's the final round of the Glitz Pit tournament and only two fighters remain. Who will be crowned the grand champion? Disclaimer: The Glitz Pit, Yoshi, and everything else in this story is a registered trademark of Nintendo.

It's a beautiful day at the Glitz Pit Battle Arena where the final match is about to take place. The crowd starts to cheer for these competitors as Jolene makes her way to center stage with her microphone in her hand. She said, "Ladies and gentlemen, welcome to the main event of the day! It's time to find out who will be crowned the champion in … the championship match!"

The crowd cheered as Jolene continues to speak, "That's right folks, one final match will decide who will be crowned the grand champion. We started the competition with 64 amazing combatants and today, we are down to the final two. This is going to be the best fight of the tournament! So without further ado, let's get started. In the blue corner, we have the best opponent you've ever seen and today, he's back for another chance at the title. Please give it up for the Koopa Krusher!"

A blue spotlight shined down towards the arena and in steps the Koopa Krusher, ready to do battle against Yoshi. Jolene walked in and asked him, "So, Koopa Krusher, how does it feel to be back in the arena for another chance?"

The Koopa Krusher replied, "It feels so good to be back in the ring and if I win today, then I'll be crowned the new champion and I'm so glad to have the fans cheer for me throughout the match so, it feels great!"

"I see. Now, do you have some moves for us to show?"

"I do! Here's one, Krusher Shell Spin!"

Then he spun in his shell and the crowd loved it. Koopa Krusher came out and said, "Ta-da!"

The crowd cheered as Jolene said, "Wow, that was amazing! Now, are you ready for the challenger?"

"YES!" the crowd cheered.

"Alright then. Let's meet today's challenger! Our challenger is everyone's favorite fighter in the Glitz Pit. He's known for his eggs, his ground pounds, and his tongue. He's been fighting all the way to today's final match and now, he's here in the red corner. And now, making his way to the arena in the red corner is the challenger. Please give it up for the Dino Fighter… YOSHI!"

A red spotlight shined down on the arena and the fog machine started up. The doors open up and in steps the egg. When the egg hatched, Yoshi has appeared from the egg and received the biggest applause from the crowd. The crowd said, "Yoshi, Yoshi, Yoshi!"

Jolene walked in to him and said, "Yoshi, welcome to the championship match and you still have your trademark green and white battle suit for this match. How does it feel?"

Yoshi replied, "It feels great! I'm so very happy to be here for the final round and I can't wait for the gong to sound. This is going to be the best fight I'll ever have and I'm ready to go with my trademark Yoshi Egg Cannon!"

"Now, according to your profile card, it said that you used your tongue to eat enemies. Is that true?" Jolene asked.

"Yes! My tongue can eat anything and I still have my Yoshi Egg Cannon. Ready to see it?"

"Go ahead, fire away!"

"Alright! Yoshi Egg Cannon... Attack!"

Then, the cannon fired an egg and it hit the target. The crowd cheered as Yoshi said, "Direct hit!"

"Wow, that was amazing! Yoshi, good luck out there and thanks for showing me your trademark Egg Cannon."

"Anytime, Jolene!" Yoshi replied as the crowd cheered.

"OK, now that we met our two amazing fighters, it's time for the rules of this amazing bout and here to tell the rules of the fight is our referee, Shy Guy!"

Shy Guy came in and replied, "Thanks, Jolene. Now this is going to be a special one-round match with no time limit. You may use your special attacks at anytime during the match and of course, you can attack your opponent with your super attack. We will keep going until we have a winner. Whoever gets knocked out first, loses the match and your opponent will be declared the grand champion! Those are the rules of the championship. Jolene?"

"Thank you, ref. And now, it's the moment you've all been waiting for. It is time to fight! Yoshi, are you ready?"

"That's a yes, Jolene." Yoshi replied with a thumbs up, "I'm ready to go!"

"Koopa Krusher, are you ready?" Jolene asked.

"I'm all set!" Koopa Krusher replied.

"Alright then, the battle begins when you hear the gong. So, hold on to your hats folks because this is going to be a great match! One of these two fighters will go home the grand champion. Who will be crowned the winner? Will it be the Koopa Krusher or the Dino Fighter? Well, we're about to find out who it is... right now! Are you ready?"

"YES!" the crowd cheered.

"Then let's get this match started! Shy Guy, take it away!"

Shy Guy agreed as the match is about to start. The crowd grew silent as Shy Guy said, "Alright you two, this is it! Once you hear this gong, the match will officially start. Yoshi and Koopa Krusher, good luck to the both of you and may the best fighter win. Now, before we get started with this match, let me tell you what's at stake here. The winner of this match will become the Glitz Pit's Grand Champion and in addition to the title of grand champion, the winner will also receive this championship trophy!"

The crowd cheered for Shy Guy when they saw the trophy. Then Shy Guy said, "And now, it's the moment that everyone's been waiting for! It's time to start the final match. It's Yoshi vs. Koopa Krusher! Are you ready?"

"Yes." The crowd said.

"I can't hear you. I said, are you ready?"

"YES!" the crowd cheered.

"Now that's more like it! All right then, here we go!"

Then Shy Guy took out his hammer and said these famous words that will start the match, "Ready…"

Yoshi and the Koopa Krusher took their fighting positions as the battle is about to begin.

"Set..."

The stadium grew very silent as they await for the sound of the gong.

And then…

And then…

It's time to start the match. Shy Guy held his breath, raised his hammer, and said the only word that will hit the gong and start the match but... the fighters aren't fighting. Shy Guy sighed and said, "Guys, wake up. The match hasn't started. Why aren't you fighting?"

"Because, you forgot to hit the gong." Yoshi said, "You can't start the match without the gong."

"Oh, I forgot the gong. Of course. I left it there when I got here but, there's no gong for me to hit. Yoshi, could you do me a favor and use your tongue to fetch me the gong?" Shy Guy asked.

"You got it! One gong to start the match for Shy Guy, coming up!" Yoshi replied as he used his tongue.

Then using his tongue, Yoshi has found the gong. Yoshi smiled and said, "Shy Guy, I found the gong! It was at the major-league locker room. Now we can start the match!"

"That's great, Yoshi. Bring it in so we can battle!"

"With pleasure! Tongue, back to the arena!"

Then, using his tongue, Yoshi has brought the gong to the arena. Yoshi smiled and said, "Here it is, Shy Guy! One official Glitz Pit gong, ready to be hit at anytime!"

"Thanks, Yoshi!" Shy Guy replied, "I'm so glad that you found it. Well, now that the gong has been found, I think we could start the match but, something's missing. I think I forgot the only word that will start the match. Now, which word is it?"

Koopa Krusher thought for a moment and said, "Is it fit?"

"No."

Yoshi smiled to Shy Guy and said, "Fight?"

"Of course! I forgot to say fight. Thanks, Yoshi! You're the best fighter the arena has ever seen. Now then, may I do the honors by hitting the gong?" Shy Guy asked them.

Yoshi and Koopa Krusher took their fighting positions and said these words at the same time, "Shy Guy, hit the... GONG!"

Shy Guy smiled at them back and said, "Alright then, here it comes. And Yoshi?"

"Yes, Shy Guy." Yoshi replied.

"Thank you for finding the gong."

"Anytime!"

"Ladies and gentlemen, the gong has been found thanks to Yoshi! Let's give it up for the Dino Fighter!" Shy Guy announced.

The crowd cheered for Yoshi as Shy Guy hugged him for his good deed. Then he said, "Now then, are you ready to do battle Yoshi?"

"Am I ready? That's a great question. Let me answer that question with one single word."

"And that single word is..."

"YES!"

"Alright then. If you're ready, 3, 2, 1..."

Shy Guy took out his hammer, raised it up, and then, he said the word...

"Fight."

But, the fighters aren't moving. Shy Guy shrugged and said, "Guys, I said fight. The match has started. Why aren't you fighting?"

"Because, the crowd is silent." Yoshi replied.

"But how?"

"Your voice is not loud enough for the crowd."

"Oh! So you want me to say the word louder so the crowd can hear me?"

"YEAH! If you say it louder, then everyone can hear you! Even us!"

"You know, this idea just might work and I'm feeling better than ever now! Thanks, Yoshi!"

"Anytime, ref. Anytime! Well, what are you waiting for? I can't stay in my battle position for another few seconds! Hurry, Shy Guy! The crowd is getting restless here and we are still waiting for your call! Now, Shy Guy. Say the word and let's get started!" Yoshi said to the referee.

Shy Guy agreed with his idea and took out his hammer. Then he said, "Alright then, here it comes! 3, 2, 1... FIGHT!"

And then, the gong has sounded and the fighters rushed in to each other with the crowd cheering.

When Shy Guy was finished with the gong, he said to Yoshi, "There! Happy?"

"YEAH! You're back to your own self now because you said the word louder! Thanks!"

"Anytime! Well, what are you waiting for? I've already hit the gong so that means that you should go and attack the Koopa Krusher right now." Shy Guy said to him, "Remember, the fighter who gets knocked out loses and the championship trophy is still at stake. So, go get 'em!"

"Now, Shy Guy?" Yoshi asked.

"Yes, Yoshi! FIGHT!" Shy Guy agreed and gave him a thumbs up.

"Oh, right! And with that from you, I'm off! Yoshi Opening... RUSH!"

And with that, the championship match has officially begun!

Yoshi started the match with his trademark eggs while the Koopa Krusher spun in his shell to block his attack. Then he attacked Yoshi with his shell and said, "You're having a shell of a time! Shell Smash!"

Yoshi smiled and replied, "Egg Shield!"

Then Yoshi shielded in his egg as the Shell Smash attack was backfired. The crowd saw the egg and cheered for Yoshi as the battle heats up. Even Jolene was impressed with Yoshi's Egg Shield and said, "Wow, Yoshi's Egg Shield has blocked the Shell Smash! This is going to be a great match!"

As the battle continues, Yoshi and the Koopa Krusher are giving everything they got. Eggs, punches, shells, you name it!

When the battle is about to end, the Koopa Krusher said, "Well, it looks like this battle has reached its end, Yoshi! Farewell! Finishing Attack: Final Koopa Krusher Spin!"

Then he spun in his shell and sped his way towards Yoshi. This was it, the attack to end the match.

"Oh, no! Koopa Krusher is aiming at Yoshi with his final attack, the Final Koopa Krusher Spin! If this attack collides with Yoshi, then it's all over, unless Yoshi has something to do to save the match! He saved the match seven times in this tournament. Can he make a big comeback and win the title? Only time will tell!" Jolene announced.

Yoshi closed his eyes and waited for the chance to strike. He took out his Egg Cannon and called out the super attack, "Signature Attack! Yoshi Final Egg Cannon!"

The crowd watched and waited for the battle to come to an end as Yoshi charged up his egg cannon. Then he counted, "3, 2, 1..."

And then…

And then…

The cannon reached full power. Yoshi held the cannon steady, took aim at the Koopa Krusher and pulled the trigger as he shouts out the signature attack…

"FULL BLAST!"

And then, the Egg Cannon fired a very big egg and sped its way towards the Koopa Krusher's final attack. When it got there, it stopped the attack and hit the Koopa Krusher, dead on! The crowd saw the egg and cheered for Yoshi as the egg grows bigger!

"There it is! The Yoshi Final Egg Cannon, Yoshi's super attack! Looks like Yoshi has saved the match once again, folks! If this egg explodes on the Koopa Krusher, then this match will come to an end. Here it comes..." Jolene announced as the egg engulfs the Koopa Krusher.

Yoshi covered his ears and said, "Well, Koopa Krusher, you were a great opponent but now, it's time for you to be scrambled with this closing attack. Enjoy the fireworks because this attack ends the match right here, right now! Farewell! Yoshi Final Egg Cannon... FINAL EXPLOSION!"

And with one final blast from the cannon, the egg exploded on the Koopa Krusher!

The blast sends him up to the ceiling and then, he fell down on the arena floor. The crowd grew silent as Koopa Krusher stood up. He said his final words, "That's the best attack I've ever seen. I can't take it anymore! And with that final attack from you, I'm now... DEFEATED!"

And with his last word, he took his last breath and fell down unconscious. Koopa Krusher was knocked out and the match has ended.

Shy Guy took out his hammer, hits the gong and said, "Whoa! That was an impressive finale! I've never seen this finishing attack from Yoshi and the Koopa Krusher is now defeated! This is unbelievable, folks! One final attack finishes the job! So, that means... FINISH!"

Jolene looked at the battle and said, "Well, that was truly an impressive display of action in the arena. Power vs. power, speed vs. strength, technique vs. technique. This was truly the most impressive battle of the tournament and the crowd loved it! But, there can only be one grand champion in this final battle and that someone is… YOSHI!"

Yoshi ran to Jolene and hugged her as confetti fell on the winner. With the crowd cheering, Jolene smiled to Yoshi and said, "You did it, Yoshi! Congratulations! I can't believe what just happened here but your final attack makes you the Glitz Pit's Grand Champion! Let's hear some noise for our grand champion!"

The crowd cheered even louder as Yoshi jumped for joy when Jolene heard the announcement. Jolene smiled and said, "So, you've done it, buddy! Well done, champ! So, how does it feel to be crowned the grand champion?"

"It feels amazing!" Yoshi replied, "I thought I was a goner but when I fired my Egg Cannon, I turned the battle around and then… BOOM! The Koopa Krusher was defeated and now, I'm the champion!"

"Of course you did, Yoshi! The stadium loves your big victory and we are so glad to have you as our grand champion and not only that, you've also saved the match. Great performance, champ! Now, let's see that final attack again in our instant replay before we give you the championship trophy, shall we?"

"We shall do that, Jolene!"

"OK, as soon as you fired the cannon, it sped its way to the Koopa Krusher. Then, the egg got bigger and stronger as you watch the attack comes in full force. And finally, BOOM! The egg exploded on him and he fell down on the arena floor, finishing the match." Jolene said as the duo saw it on an instant replay.

The crowd saw it all and cheered for Yoshi's big performance.

Then Jolene said, "Ladies and gentlemen, I present to you the grand champion of the Glitz Pit. The Dino Fighter himself... YOSHI!"

The crowd cheered very loudly as Yoshi waved to the crowd. Even Shy Guy cheered for Yoshi as confetti keeps on falling.

"Now, here to present this championship trophy is our referee. Shy Guy, do the honors by presenting this trophy to our winner." Jolene said.

Shy Guy came to the arena with the trophy and said, "Yoshi, on behalf of the Glitz Pit, it gives me great pleasure to present to you with this championship trophy! This trophy proves to you that becoming the champion requires skill, strength, stamina, and courage. You have made the stadium very proud with your strong attacks, your quick speed, and most of all, you have made this final match the most impressive match the stadium has ever seen and most of all, you've found the gong to start the match. And now, it is time for you to claim your trophy. Yoshi, step on forward to collect your prize!"

Yoshi agreed as he gets the trophy. Shy Guy came to him and said with a hug, "Congratulations, Yoshi! You deserve it!"

"Thank you, Shy Guy!" Yoshi replied as he held the trophy up high and while he was doing that, more confetti fell on the arena with the crowd cheering. Yoshi smiled to Jolene and Shy Guy and said, "Well, I guess there can only be one champion and I want everyone in the arena to say my name. Ready? One, two, three…"

Everyone said his name at the same time: "YOSHI!"

Then Yoshi said with a wink, "That's me, the grand champion!"'''.replace('…', '...')

print('read input')

def IC(data, alph=None):
    if not isinstance(data, Counter):
        data = Counter(data)
    if alph is None:
        alph = len(data)
    denom = sum(v for v in data.values())
    return sum(v*(v-1) for v in data.values())*alph/denom/(denom+1)


def dbIC(data, n):
    total = 0
    for i in range(n):
        total += IC(data[i::n], 26)
    return total / n

print('data:')
for d in range(1, 20):
        val = dbIC(data, d)
        print(f'd = {d}: {val}')

def invmod(a, n):
    a, b = _gcd_inv(a, n)
    # at this point a is the gcd of the original inputs
    if a == 1:
        return b
    raise ValueError("Not invertible")

def _gcd_inv(a, n):
    b, c = 1, 0
    while n:
        q, r = divmod(a, n)
        a, b, c, n = n, c, b - q*c, r
    return a, b

def gcd(a, n):
    return _gcd_inv(a, n)[0]

def lcm(a, b):
    return a*b//gcd(a,b)

##example = ''.join(v.lower() for v in example if v.lower() in 'abcdefghijklmnopqrstuvwxyz')

ebigramsc = Counter(example[i:i+2] for i in range(len(example)-1))
ebigrams = sorted(((k, v) for k, v in ebigramsc.items()), key=lambda x:-x[1])
logbigrams = {k:100*log(v) for k, v in ebigrams}

ectr = Counter(example)
ecommon = sorted(ectr.items(), key = lambda x:-x[1])
ecommon2 = [k for k, v in ecommon]
echarset = sorted(ectr)

ep = {k:v/len(example) for k, v in ectr.items()}
sep = sorted(ep.items(), key=lambda x:-x[1])

def ICforD(data, d, charset):
    i = 0
    out = ''
    for c in data:
        out += charset[(charset.index(c)+i)%len(charset)]
        i += 1
        i %= d
    return IC(out, len(charset))

'''for d in range(1, 11):
    val = ICforD(example, d, echarset)
    print(f'd = {d:2}: {val}')'''

##ebigrams = [example[i:i+2] for i in range(len(example)-1)]
##print(f'IC for example = {IC(ectr, 26)}')
##print(f'IC for example bigrams = {IC(Counter(ebigrams))}')


ctr = Counter(data)
nospace = list(set(ctr)-{' '})
charset = sorted(ctr)
#print(f'IC = {IC(ctr, 26)}')

#print(f'data is {len(data)} characters long.')

ecommonf = [(k, v) for k, v in ecommon if k in charset]
ecommonf1 = [k for k, v in ecommonf]


def kasiski(data, l):
    chunks = [data[i:i+l] for i in range(len(data)-l)]
    ctr = Counter(chunks)
    diffs = set()
    indexes = []
    for k, v in ctr.items():
        if v > 1:
            ni = data.find(k)
            inds = [ni]
            while True:
                nn = data.find(k, ni+l)
                if nn == -1:
                    break
                inds.append(nn)
                d = nn - ni
                diffs.add(d)
                ni = nn
            indexes.append(inds)
    return diffs, reduce(lambda x,y:gcd(x,y), diffs), indexes

##bigramsc = Counter((data[i:i+2]) for i in range(len(data)-2))
##bigrams = sorted(((k, v) for k, v in bigramsc.items()), key=lambda x:x[1])

##print(f'bigrams in data up to {len(significant)}')
##print(significant)
##
##es = ebigrams[-70:]
##print(f'ordinary bigrams up to {len(es)}')
##print(es)
##
##print('letter freq (data):')
##print(ctr)
##
##print('letter freq (english):')
##print(ectr)

n = 39

chunks = [data[i:i+n] for i in range(0, len(data), n)]

def splitchunk(chunk):
    return ' '.join(repr(chunk[i:i+13]) for i in range(0,n,13))

def dec(chunks, key):
    newchunks = []
    for chunk in chunks:
        newchunk = ''
        for c, tab in zip(chunk, key):
            try:
                newchunk += tab[c]
            except KeyError:
                newchunk += '='
        newchunks.append(newchunk)
    return newchunks

def getpairs(data, d, i):
    for j in range(0, len(data)-i-2, d):
        yield data[j+i:j+i+2]

def getSig(data, d, i):
    pairs = Counter(getpairs(data, d, i))
    sigPairs = [(k, v) for k, v in pairs.items() if v > 9]
    return sorted(sigPairs, key=lambda x:-x[1])


pc = [Counter(getpairs(data, n, i)) for i in range(n)]

commonC = [Counter(data[i::n]) for i in range(n)]
common = [sorted(c.items(), key=lambda x:-x[1]) for c in commonC]
common2 = [[k for k, v in entry] for entry in common]

#ctrn = [sorted((Counter(data[i::n]) for i in range(n)), key=lambda x:-x[1])]

kb = [sorted(Counter((data[i:i+2] for i in range(j,len(data)-1,n))).items(), key=lambda x:-x[1]) for j in range(n)]



'''max = 0
for d in range(1, 500):
        v = dbIC(data, d)
        if v > max:
                max = v
                dd = d

print(dd, max)
'''

##for chunk in chunks:
##    print(repr(chunk))

#dec(data, {'h':'e'})

##print(IC(ebigramsc, len(ebigramsc)))
##print(IC(bigramsc, len(bigramsc)))

def updatekey(candiatekey):
    global memo1, memo2
    for i in range(n):
        m1i = memo1[i]
        m2i = memo2[i]
        #memc = Counter(v for k, v in candidatekey[i])
        for j in range(1, len(candidatekey[i])):
            characters = set(v for k, v in candidatekey[i])
            ptchar, oldkc = candidatekey[i][j]
            i1 = (i-1) % n
            i3 = (i+1) % n
            key1 = dict(candidatekey[i1])
            key3 = dict(candidatekey[i3])
            if ptchar not in m1i:
                m1i[ptchar] = [(a, v) for (a, b), v in kb[i1] if b == ptchar]
            if ptchar not in m2i:
                m2i[ptchar] = [(b, v) for (a, b), v in kb[i] if a == ptchar]
            m1c = [(key1[a], v) for a, v in m1i[ptchar]]
            m2c = [(key3[b], v) for b, v in m2i[ptchar]]
            oldCS = 0
            for a, v in m1c:
                try:
                    oldCS += logbigrams[a+oldkc]
                except KeyError:
                    pass
            for b, v in m2c:
                try:
                    oldCS += logbigrams[oldkc+b]
                except KeyError:
                    pass
            for char in nospace:
                if char in characters:
                    continue
                newCS = 0
                for a, v in m1c:
                    try:
                        newCS += logbigrams[a+char]*v
                    except KeyError:
                        pass
                for b, v in m2c:
                    try:
                        newCS += logbigrams[char+b]*v
                    except KeyError:
                        pass
                if newCS > oldCS:
                    oldCS = newCS
                    #print(i, j, char)
                    candidatekey[i][j] = (ptchar, char)
                    changed = True
    return changed


#candidatekey = [[(j[0], k) for j, k in zip(common[i], ecommonf1)] for i in range(n)]


#key = [{} for i in range(n)]
key = [{j[0]:k[0] for j, k in zip(common[i], ecommonf[:1])} for i in range(n)]

#for i in range(n):
#    candidatekey[i][0] = (candidatekey[i][0][0], ' ')

#memo1 = [[None]*len(c) for c in candidatekey[i] for i in range(n)]
#memo2 = [[None]*len(c) for c in candidatekey[i] for i in range(n)]
memo1 = [{} for i in range(n)]
memo2 = [{} for i in range(n)]

key[4]['t'] = 'h'
key[34]['G'] = 'h'
key[37]['2'] = 'h'
key[31]['p'] = 'o'
##key[5]['1'] = 'T'

#print(*(candidatekey[i][0] for i in range(n)))

#key = [dict(row) for row in candidatekey]

# unkown endings: 11631, 1022, 16429
# suspect: 9602:the, 5833:the
# unsure: (3582, 'time'), (4208, 'time')
'''cribs = [
    (-2, '/'), (-5, '/'), (4738, 'e'), (5625, 'e'), (-5632, 'ee'),
    (588, 'the'), (657, 'the'), (1570, 'the'), (-2440, 'the'), (-5181, 'the'), (-9602, 'the'),
    (16026, 'the'), (3857, 'the'), (5884, 'the'), (955, 'the'), (820, 'the'), (973, 'the'),
    (10569, 'the'), (6798, 'the'), (4580, 'the'), (-605, '==e'), (1035, 'the'), (-2250, 'the'),
    (230, 'The'), (9051, 'The'),
    (6119, 'that'), (1863, 'that'), (8287, 'that'),
    (-3540, 'that we met'),
    (2958, 'with'),
    (2413, 'doors'),
    (13641, 'tournament'),
    (-935, 'chin'), (4167, 'moment'),
    (-498, 'center stage'), (3075, 'enemies.'), #rewrite with so
    (505, 'stage with her microphone in her hand. She said, "Ladies and gentlemen,'),
    (625, 'to'), (1465, 'to'), (2610, 'to'), (3754, 'to'), (4479, 'to'), (4520, 'to'), 
    (4878, 'to'), (16258, 'to'),
    (5069, 'and'), (9354, 'and'), (-1755, 'and'),
    (9389, 'other'),
    (14461, 'defeated'), (459, 'competit'), (-1199, 'moonlight sonata'), (-1199, 'moonlight'),
    (2643, 'to the'), (1983, 'challenger!'),
    (1357, 'how does'),
    (2413, 'doors open'),
    (-3740, 'this in'),
    (2537, 'from'),
    (2683, 'have'), (14583, 'have'), (-7831, 'have'), (17194, 'have'), (1055, 'have'), (-3159, 'have'),
    (-2490, 'from the'),
    (2138, 'all the'),
    (3663, 'is'),
    (1361, 'does'), (577, 'welcome to the'),
    (-1805, 'over'),
    (-1085, 'over seen'), #(1085, 'over'),
    (-516, 'sea'),#*
    (620, 'time'),
    (-3313, 'target'),
    (-2842, 'round'),
    (190, 'crowned the '), (1521, 'crowned'), (812, 'crowned the'), 
    (104, 'the final round of the'),
    (148, 'and only two fighters'),
    (620, 'time to find out who will be crowned the champion in'),
    (-3075, 'premier'), (29, 'fanfiction'), (5256, 'addition'),
    (2528, 'applause from the'), (-4554, 'two =i=ete=n'), (4554, 'two'),
    (4400, 'replied.'),
    (4443, 'when'),
    (-3870, ' of '), (5061, ' of '), (-15960, ' of '),
    (-2740, 'gladly'), (-4534, 'gladly'),
    (-5898, 'lurid'), (-16612, 'me'), (-5053, 'the time of day'), (-4738, 'e her'),
    (-15569, 'choose'), (-5131, 'that'), (-7173, 'this'), (-12555, 'this'),
    (-7719, 'these'), (-87, 'Tuesday'), (-1024, 'th'), (-1027, 'th'),
    (-585, 'so'), (-741, 'so'), (-5265, 'so'), (-5499, 'so'), (-9516, 'so'),
    (8108, 'him'), (-14350, 'his'), (-1764, 'hired'),
    (-2938, 'day'),
    (-16253, 'face'),
    (-13611, 'font'),
    (-10054, 'catch him'),
    (15478, 'present'),
    (-272, 'on'), (-16510, '-'),
    (9195, 'referee'), (15712, 'pleasure'),
    (449, 'for these competitors'),
    (16215, 'agreed'),
    (148, 'and only'),
    (1827, 'crowd cheered'), (1933, 'crowd cheered'),
    (-1398, 'for another'),
    (-9831, 'an'), (-883, 'important'), (-1239, 'and in stead'),
    (-1128, 'change'), (6077, 'raised'), (4209, 'time'), (1402, 'another'),
    (11466, 'super'),
    (3698, 'came'), (3819, 'our'), (9001, 'position'),
    (-302, 'trademark of'), (16839, 'because horses'),
    (286, 'is a registered trademark of Nintendo.\n'),
    (7488, 'course'), (14503, 'course'),
    (178, 'Who will be crowned the grand champion?'), (800, 'who will be crowned the grand champion'),
    (14073, 'champion'), (855, 'competition'), (15749, 'championship'), (1537, 'champion'),
    (14605, 'champion'), (13709, 'champion'), (16563, 'champion'), (-5240, 'champion'),
    (5331, 'championship'), (15491, 'championship'), (5287, 'champion'),
    (14772, 'championship'), (74, 'Championship'), (2650, 'championship'),
    (-681, 'championship'), (-10041, 'championship'),
    (15436, 'confetti'),
    (137, 'tournament'),
    (7939, 'Ladies and gentlemen,'),
    (15230, 'Ladies and gentlemen,'),
    (2471, 'Yoshi'), (5530, 'Yoshi'), (6650, 'Yoshi'), (6494, 'Yoshi'), (7875, 'Yoshi'),
    (11499, 'Yoshi'), (2570, 'Yoshi'), (2767, 'Yoshi'), (3238, 'Yoshi'), (3167, 'Yoshi'),
    (3393, 'Yoshi'), (3494, 'Yoshi'), (7440, 'Yoshi'), (8183, 'Yoshi'), (9895, 'Yoshi'),
    (10291, 'Yoshi'), (11056, 'Yoshi'), (-4114, 'Yoshi'), (13771, 'Yoshi'), (13909, 'Yoshi'),
    (5025, 'Koopa'), (5837, 'Koopa'), (12726, 'Koopa'), (4325, 'Koopa'), (11029, 'Koopa'),
    (1424, 'Koopa'), (1780, 'Koopa'), (9697, 'Koopa'), (10141, 'Koopa'), (11095, 'Koopa'),
    (12009, 'Koopa'), (13097, 'Koopa'), (14895, 'Koopa'), (1175, 'Koopa'), (10662, 'Koopa'),
    (12417, 'Koopa'), (4647, 'Koopa'),
    (10526, 'said, "'), (10796, 'said, "'), (14193, 'said, "'),
    (1780, 'Koopa Krusher'), (9697, 'Koopa Krusher'), (11029, 'Koopa Krusher'), (11926, 'Koopa Krusher'),
    (10662, 'Koopa Krusher'), (12417, 'Koopa Krusher'), (1424, 'Koopa Krusher'), (11095, 'Koopa Krusher'),
    (5025, 'Koopa Krusher'), (12009, 'Koopa Krusher'), (14895, 'Koopa Krusher'), (7374, 'Koopa Krusher'),
    (11029, 'Koopa Krusher'), (11926, 'Koopa Krusher'),
    (252, 'and everything else in this story'), (977, 'tournament! So without further ado, let\'s'),
    (371, 'Arena where the'), (218, 'Disclaimer:'),
    (1199, 'spotlight shined down towards'),
    (333, 'beautiful day at the'),
    (14910, 'The'), (3321, 'The'), (14085, 'The'),
    (1262, 'Krusher'), (12367, 'Krusher'),
    (377, 'where the final match is about to take place.'),
    (12033, 'The crowd'), (3321, 'The crowd'), (14085, 'The crowd'), (703, 'The crowd'),
    (5354, 'The crowd'), (1823, 'The crowd'), (10404, 'The crowd'), (2553, 'The crowd'),
    (8062, 'The crowd'), (15148, 'The crowd'), (15343, 'The crowd'), (15343, 'The crowd'),
    (-12823, 'The crowd'), (9051, 'The crowd'),
    (2542, 'the crowd'), (8675, 'the crowd'), (15391, 'the crowd'), (422, ' The crowd'), (481, 'makes her way to'),
    (11562, 'battle'), (13732, 'battle'), (1283, 'battle'), (8176, 'battle'),
    (10828, 'battle'), (10455, 'battle'), (10754, 'battle'), (13445, 'battle'),
    (2719, 'battle'), (5888, 'battle'), (6902, 'battle'),
    (423, 'The crowd starts to cheer'),
    (-681, 'championship'), (-10041, 'championship'),
]'''
cribs = [
    (-9, 'source: https://www.fanfiction.net/s/'),
    (9, 'source: https://www.fanfiction.net/s/6267887/1/Yoshi-s-Glitz-Pit-Championship-Fight'),
    (99, pta[67:]),
    (-16763, '''----

If you have solved this puzzle then message me with "Yoshi is a horse because horses lay eggs". Thanks for solving Cariad's 2020 Crypto Puzzle!

I haven't done one of these in a few years namely due to medical issues and just overall needing to take a step back from things. However, I am super happy to see someone has solved this and I plan to make one again next year. I hope you are well and please do let me know if you have solved it!
'''),    
]
#(9, 'holiday'), (824, 'merry christmas')]#, (16484, 'christmas')]
##

seen = {}
for i, string in cribs:
    if i < 0:
        continue
    for j, elem in enumerate(string):
        ij = i+j
        ki = ij%n
        ctc = data[ij]
        letters = {v for k, v in key[ki].items()}
        lmap = {v:k for k, v in key[ki].items()}
        pair = (ctc, ki)
        old = None
        try:
            old = key[ki][ctc]
        except KeyError:
            pass
        if elem == ' ' and old is not None and old != ' ':
            print(f'crib: ({i}, "{string[:15]}") has overwritten {old} with a space at {ij}')
        if pair in seen and seen[pair][0] != elem:
            print(f'crib: ({i}, "{string[:15]}"):{elem} conflicts with previous crib {seen[pair][1]}:{seen[pair][0]}')
        if old == ' ' and elem != ' ':
            print(f'space at {ki}:{ctc} overwritten with {elem} by ({i}, {string[:15]})')
        if elem in letters and elem != old:
            octc = lmap[elem]
            otherPair = (octc, ki)
            try:
                r1, (r2, r3) = seen[otherPair]
                rule = r1, (r2, r3[:15])
            except KeyError:
                rule = f'{ki}:{octc}'
            print(f'crib: ({i}, "{string[:15]}" is writing letter {elem} again at {ki}:{ctc} from {rule})')
        seen[pair] = (elem, (i, string[:15]))
        key[ki][ctc] = elem
        
key[14] = {c:c for c in charset}

equivalent_keys = [[0, 3], [1, 7, 16, 26, 34], [2, 38], [4, 36], [5, 11], [6, 12, 24], [8, 23, 32], [17, 19, 29], 
[18, 21, 25, 28, 31, 33], [30, 37]]

for group in equivalent_keys:
    for i, i1 in enumerate(group[:-1]):
        for j, i2 in enumerate(group[i+1:]):
            k1 = key[i1]
            k2 = key[i2]
            for k, v in k1.items():
                try:
                    if k2[k] != v:
                        print (f'conflicting pair {i1}, {i2}, for {k}')
                except KeyError:
                    pass
                k2[k] = v
            for k, v in k2.items():
                try:
                    if k1[k] != v:
                        print (f'conflicting pair {i1}, {i2}, for {k}')
                except KeyError:
                    pass
                k1[k] = v

reverseKey = [{v:k for k, v in i.items()} for i in key]

#val = sum(list(elem.values()).count(' ') for elem in key)
#print(f'there are {val} spaces in the key decoder.')

with open('decoded', 'w') as f, open('plaintext.txt', 'w') as g, open('pt-wrap.txt', 'w') as h:
    decoded = dec(chunks, key)
    for i in range(len(chunks)):
        j = i*n
        print(splitchunk(chunks[i]), file=f)
        print(splitchunk(decoded[i])+f'{j} {j+13} {j+26}', file=f)
        print(decoded[i], end='', file=g)
        print(decoded[i], file=h)

print('wrote output')

with open('plaintext.txt', 'r') as f:
    pt = f.read()

'''updatekey(candidatekey)

import cProfile
cProfile.run('updatekey(candidatekey)')

changed = True
loops = 0
while changed:
    #oldCandidateKey = [[item for item in item1] for item1 in candidatekey]
    print(f'loop1: {loops}')
    changed = updatekey(candidatekey)
    #if candidatekey == oldCandidateKey:
    #    break
    key = [dict(v) for v in candidatekey]
    loops += 1

    with open('decoded', 'w') as f:
        decoded = dec(chunks, key)
        if loops % 50 == 0:
            print(''.join(decoded[:5]))
        for i in range(len(chunks)):
            j = i*n
            print(splitchunk(chunks[i]), file=f)
            print(splitchunk(decoded[i])+f'{j} {j+13} {j+26}', file=f)
            
print('finished')'''

def graph(i):
    ##print('example')
    ##plt.figure()
    ##plt.bar([ord(v) for v in ectr.keys()], ectr.values())
    ##plt.show()

    ##if not isinstance(graphs, list):
    ##    graphs = list(graphs)

    ##for i in graphs:
    print(f'data[{i}::n]')

    kc = Counter(data[i::n])
    plt.figure()
    plt.bar([ord(v) for v in kc.keys()], kc.values())
    plt.show()

def searchpt(string, preserveSpace=False):
    options = []
    amount = 0
    for i in range(len(pt)-len(string)+1):
        matches = 0
        for j in range(len(string)):
            if preserveSpace and string[j] == ' ' and pt[i+j] != ' ':
                break
            if string[j] == pt[i+j]:
                matches += 1
        else:
            if matches == len(string):
                continue
            if matches > amount:
                options = []
            if matches >= amount:
                options.append((i, pt[i:i+len(string)]))
                amount = matches
    return options, amount
    
def searchptR(string, preserveSpace=False):
    options, amount = searchpt(string, preserveSpace)
    options = [(i, string) for i, ps in options]
    return options, amount


def scoreChar(ptc, ctci):
    occ = commonC[ctci%n][data[ctci]]
    p = occ/len(data[ctci%n::n])
    try:
        v = ep[ptc]
    except KeyError:
        return 1
    return (p-v)*(p-v)

    
def searchct(string, excluded=None):
    if excluded is None:
        excluded = set()
    sl = len(string)
    bestscore = float('inf')
    bestI = -1
    for i in range(len(data)-sl+1):
        if i in excluded:
            continue
        if pt[i:i+sl] == string:
            continue
        thisScore = 0
        for ptc, ctci in zip(string, range(i, i+sl)):
            #thisScore = max(thisScore, scoreChar(ptc, ctci))
            thisScore += (scoreChar(ptc, ctci))**0.5
        if thisScore < bestscore:
            bestscore = thisScore
            bestI = i
    return (bestI, pt[bestI:bestI+sl], bestscore)
            
def searchctRecurse(string, failures=1):
    pairs = []
    sl = len(string)
    excluded = set()
    while True:
        i, pstring, score = searchct(string, excluded)
        #print(i, string, score)
        excluded.add(i)
        for pc, sc in zip(pstring, string):
            if pc != '=' and sc != pc:
                break
        else:
            pairs.append((i, string))
            continue
        failures -= 1
        if failures > 0:
            continue
        break
    return pairs

#print(list(len(set(data[i::n])) for i in range(n)))


def stats(si, le, ts=None):
    out = []
    for i in range(si, si+le):
        c = data[i]
        ord = common2[i%n].index(c)
        occ = commonC[i%n][c]
        p = occ/len(data[i%n::n])
        pc = pt[i]
        if ts is not None:
            pc = ts[i-si]
        v1 = scoreChar(pc, i)
        out.append(f'{i%n}:{i}:{ord}:{c}:{pc}:{p:.4f}:{v1:.4f}')
    return out
    
def keyFind(string):
    ci = -1
    while True:
        ci = pt.find(string, ci+1)
        if ci == -1:
            break
        for i, c in enumerate(string):
            cti = ci+i
            ki = (cti)%n
            pair = (data[cti], ki)
            if pair in seen:
                print(seen[pair])
    
def statFind(string, test=None):
    ci = -1
    while True:
        ci = pt.find(string, ci+1)
        if ci == -1:
            break
        print(stats(ci, len(string), test))

'''
for i, k in enumerate(key):
    l = repr(''.join(k[v] if v in k else '=' for v in charset))
    print(f'key[{i}]: {l}')
    
for char in charset:
    s = ''
    for k in key:
        if char in k:
            s += k[char]
        else:
            s += '='
    print(repr(char), repr(s))
'''
print('end')
