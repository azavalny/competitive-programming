class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import Counter

        """
        are there two values equal to each other w/ distance <=k?

        [1, 2, 3, 1, 2, 3] k=2
         [  ]
            [  ]
               [  ]
                   [  ]
                      [  ]
        
        [1, 2, 3, 1, 2, 3] k=3
         [     ]
            [     ]
               [      ]
                   [     ]

        keep track of set of counts at each step and remove the last
        """
        window = set()
        l=0
        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False