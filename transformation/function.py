# Given code
# code = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
code = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽" 
# Reversing the operations
reversed_flag = ''
for i in range(0, len(code)):
    num = ord(code[i])
    char1 = chr(num >> 8)  # Reverse the left shift operation
    char2 = chr(num & 255)  # Retrieve the second character from the combined code point
    reversed_flag += char1 + char2

print(reversed_flag)

