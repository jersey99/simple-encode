def getPrefixOcc(c, S, i):
    count = 0
    while i < len(S) and c == S[i]:
        i+=1
        count += 1
    return count
    
def encode (S):
    nS = ""
    i = 0
    while i < len(S):
        count = getPrefixOcc(S[i],S,i+1)
        if count == 0:
            nS += S[i]
        else:
            nS += str(count+1) + 'x' + S[i]
        i += count + 1
    return nS

for s in ['abbbbcccd', 'bb', 'a']:
    print s, " -> ", encode(s)
