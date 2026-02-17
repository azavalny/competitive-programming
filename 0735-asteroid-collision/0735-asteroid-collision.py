class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        if 2 asteroids collide smaller explodes
        if both same size both will explode

        in a row = 

        two asteroids with same signs wont meet
        >  >   <   >   <  >
        [3, 5, -6, 2, -1, 4]​​​​​​​
        
stack: [-6, 2, 4]
        for each asteroid:
            while crash of two asteroids if left positive right negative:
                pop stack
                add larger of the two values (pop 2nd if equal in absolute value)
            otherwise push to stack
        """
        stack = []

        for a in asteroids:
            ignore = False
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0:
                    if abs(a) < abs(stack[-1]):
                        ignore = True
                        break
                    elif abs(a) == abs(stack[-1]):
                        stack.pop()
                        ignore = True
                        break
                    else:
                        stack.pop()

                if ignore == False:
                    stack.append(a)
        return stack