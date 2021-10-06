word='abcefdsakoasssclpl'
letters={}
pocitadlo=0
max=0

for c in word:
    if c in letters:
        letters[c]=(letters[c])+1
    else:
        letters[c]=1
    pocitadlo=pocitadlo+1

# for a,b in letters.items():
#     print(a, b)       
#     if b>max:     
#         max=b                                                       

# print(max)