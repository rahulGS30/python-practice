def check(text,key):
    new_text =""
    for char in text:
        if char.islower():
            new_text+=chr(((ord(char)-ord('a')+key)%26)+ord('a'))
        elif char.isupper():
            new_text+=chr(((ord(char)-ord('A')+key)%26)+ord('A'))
        else:
            new_text+=char
    return new_text




text = "All the best"
key = 1
result = check(text,key)
print(result)