print("-" * 50)
print("Caesar Cipher Encryptor / Decryptor ")
print("-" * 50)

mode = input("encrypt or decrypt? ('e' or 'd'): ")
text = input("Enter your msg: ")
shift = int(input("Enter the key : "))


if mode == 'd':
    shift = -shift

result = ""

for char in text:
    
    
    if char.isalpha():
        
        
        if char.isupper():
            ascii_offset = 65  
        else:
            ascii_offset = 97  
            
        new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        result += new_char
        
    else:
        result += char

print(result)