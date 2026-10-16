class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        """
        for each char in searchword:
            prefix += char
            find top 3 products with common prefix of searchWord and lexicographically minimum

        all products unique

        
 products = ["mobile","mouse","moneypot","monitor","mousepad"]
    => sorted ["mobile","moneypot","monitor","mouse","mousepad"]
                    l
                                      m
                                                        r
searchWord = "mouse"

    m [mobile, moneypot, monitor]
    mo [mobile, moneypot,  monitor]
    mou, mous, mouse ["mouse","mousepad"]


    brute force: O(n^2)
    sort products
    for each char:
        prefix += char
        find up to 3 products from left to right with common prefix of char

    better: O(slog(p*n) + pnlogp)
    binary search on products that share current typed prefix to find minimum valid and then find next 3 after

["mobile","moneypot","monitor","mouse","mousepad"] searchWord = "mouse"
Current prefix: m
left 0
right 4
mid 2
Status match
we found a match monitor
left 0
right 1
mid 0
Status match
we found a match mobile
min_valid_index 0
Current prefix: mo
left 0
right 4
mid 2
Status match
we found a match monitor
left 0
right 1
mid 0
Status match
we found a match mobile
min_valid_index 0
Current prefix: mou
left 0
right 4
mid 2
Status right
left 3
right 4
mid 3
Status match
we found a match mouse
min_valid_index 3
search prefix mou
search prefix mou
search prefix mou
matching words ['mouse', 'mousepad']
Current prefix: mous
left 0
right 4
mid 2
Status right
left 3
right 4
mid 3
Status match
we found a match mouse
min_valid_index 3
search prefix mous
search prefix mous
search prefix mous
matching words ['mouse', 'mousepad']
Current prefix: mouse
left 0
right 4
mid 2
Status right
left 3
right 4
mid 3
Status match
we found a match mouse
min_valid_index 3
search prefix mouse
search prefix mouse
search prefix mouse
matching words ['mouse', 'mousepad']
        """
        def is_match(mid, prefix):
            product = products[mid]
            if product.startswith(prefix):
                return "match"
            elif product > prefix:
                return "left"
            return "right"
        sol=[]
        prefix = ""
        products.sort()
        for c in searchWord:
            prefix += c
            l=0
            r=len(products)-1
            min_valid_index = None
            while l <= r:
                mid = (l + r)//2
                status = is_match(mid, prefix)
                if status == "match":
                    r = mid -1
                    min_valid_index = mid
                elif status == "left":
                    r = mid -1
                else:
                    l = mid + 1
            group = []
            if min_valid_index != None:
                for i in range(3):
                    if min_valid_index + i < len(products) and products[min_valid_index + i].startswith(prefix):
                        group.append(products[min_valid_index + i])
            sol.append(group)
        return sol