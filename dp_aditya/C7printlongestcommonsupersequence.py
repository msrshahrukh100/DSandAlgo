# in printing longest common subsequence, (the lcs obtained in C1) we
#  see the matrix of dp(cache) and decrement i and j if both are equal and
# include the same character or
# decrement the one whose value is more in matrix i.e.
# if a[i] != b[j] and if cache[i-1][j] > cache[i][j-1]: i = i - 1


# in printing the longest common supersequence do similar but include the
# lcs part once and rest of both the string as is. see this
# https://www.youtube.com/watch?v=VDhRg-ZJTuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=29


def print_lcsupersequence():
    '''
        Prints the longest common subsequence
    '''
    i = n
    j = m
    longest_common_subsequence = ""
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            longest_common_subsequence += s2[i-1]
            i -= 1
            j -= 1
        else:
            if cache[i-1][j] > cache[i][j-1]:
                longest_common_subsequence += s2[i-1]
                i -= 1
            else:
                longest_common_subsequence += s1[j-1]
                j -= 1

    print(longest_common_subsequence[::-1])


print_lcs()
