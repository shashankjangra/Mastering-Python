ransomNote = input("Ransom Note: ")
magazine = input("Magazine: ")

for i in ransomNote:
    for j in magazine:
        if i==j:
            magazine = magazine.replace(j,'',1)
            ransomNote = ransomNote.replace(j,'',1)

if ransomNote == '':
    print('True')

else:
    print('False')