class Solution:
    def hIndex(self, citations: list[int]) -> int:
        candidates = [0]
        for num in citations:
            counter = 0
            for num2 in citations:
                if num2 >= num and counter <= num:
                    counter += 1
                if counter <= num:
                    candidates.append(counter)
        h_index = max(candidates)

        return h_index
    
## Time Complexity = O(n²)