class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        """
        string b is subset of a = every letter of b occurs in a including multiplicity

        wrr c warrior
              1011
        
        string in words1 is universal if every string in words2 is subset

        O(n)
        make words2 frequency map
            if one char is multiple of another, take larger
            if char > 1, seperate them

        loop over each word in words1:
            each word is at most 10 chars so I can make frequency map
        
            if word has subset of frequencies of words2 add to solution
                subset of frequencies means we loop over each of the characters in words2 frequency
                dictionary and see if at least the words2 count show up in the current word
                Done in O(1) because dictionary size cannot be more than 26
                
                if not, we skip the current word


        e.g.
            facebook = {f:1, a:1, c:1, e:1, b:1, o:2, k:1}
            words2 = {e:1, o:1}
            words2 c facebook

            leetcode = {l:1, e:3, t:1, c:1, o:1, d:1}
            words2 = {l:1, c:1, e:1, o:1}


            words2 = {c:3, b:1}


            
        """
        words2_freq = Counter()
        for w in words2:
            w_freq = Counter(w)
            for c in w_freq:
                words2_freq[c] = max(words2_freq[c], w_freq[c])

        print(words2_freq)
        sol = []
        for word in words1:
            to_add = True
            words1_freq = Counter(word)
            for c in words2_freq:
                if not (c in words1_freq and words2_freq[c] <= words1_freq[c]):
                    to_add = False
                    break
            if to_add:
                sol.append(word)
        return sol