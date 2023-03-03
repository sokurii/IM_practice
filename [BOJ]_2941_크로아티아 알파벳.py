'''
크로아티아 알파벳 목록에 없는 한글자 알파벳으로 대체해주었다
'''
alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
cnt = 0

for a in alpha:
    if a in word:
        word = word.replace(a,'a')
print(len(word))