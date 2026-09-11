class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        keys (2-9) map to any # of letters
        each letter must map to one key
        it is not necessary to map letters to every key, but to map all the letters

        find min number of pushes needed to type word
            position within key's list matters
        
        total cost = number of presses * number of characters
        
        make dictionary of unique characters and sort in order of highest frequency
        keypadDist is 1
        loop in order of lowest frequency 
            multiply frequency*keypadDist
            if i is divisible by 8, increment keypadDist

        aabbccddeeffgghhiiiiii

        i = 8%8==0
        keypadDist = 1

        i:6*1 = 6
        a:2*1 = 2
        b:2*1
        c:2*1
        d:2*1
        e:2*1
        f:2*1
        g:2*1
        h:2*2
    
        """
        freqs = {}
        for w in word:
            freqs[w] = freqs.get(w, 0) + 1
        freqArray = list(sorted(freqs.items(), key=lambda x: x[1], reverse=True))
        
        pushes = 0
        i=1
        keyPadDist=1
        for char, freq in freqArray:
            pushes += freq*keyPadDist
            if i%8==0:
                keyPadDist+=1
            i+=1
        return pushes