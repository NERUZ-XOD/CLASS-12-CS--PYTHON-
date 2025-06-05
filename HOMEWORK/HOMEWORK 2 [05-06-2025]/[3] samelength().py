''' [3] Write a function that receives two string arguments and returns True if both strings 
        are of same length, False otherwise.                                                '''

def same_length(a,b):
    len1 = len(a)
    len2 = len(b)
    if len1 == len2:
        return True
    else:
        return False
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = same_length(string1, string2)
print(result)