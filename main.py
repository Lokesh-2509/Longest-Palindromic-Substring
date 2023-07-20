def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]
def longest_palindromic_substring(A):
    longest = ""
    for i in range(len(A)):
        pal1 = expand_around_center(A, i, i)
        pal2 = expand_around_center(A, i, i + 1)
        if len(pal1) > len(longest):
            longest = pal1
        if len(pal2) > len(longest):
            longest = pal2
    return longest
if __name__ == "__main__":
    input_str = input("Enter the string: ")
    result = longest_palindromic_substring(input_str)
    print("Longest Palindromic Substring:", result)
