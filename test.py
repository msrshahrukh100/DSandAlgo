class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        found = False
        answer = -1
        i, j = 0, 0
        
        while i < len(haystack) and j < len(needle):
            
            if haystack[i] == needle[j]:
                print(haystack[i], needle[j])
                bi = i
                bj = j
                while bi < len(haystack) and bj < len(needle):
                    if haystack[bi] != needle[bj]:
                        break
                    else:
                        if bj == len(needle) - 1:
                            found = True
                            answer = i
                    bi += 1
                    bj += 1
                
                if found:
                    break
            
            i += 1
            j += 1
        
        return answer
            
            
                
                
        s