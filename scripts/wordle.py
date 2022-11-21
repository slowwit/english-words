import json

def rtn_words(pat, fw='salet', wrds=None, rules=None):
    if not wrds:
        with open('words_dictionary.json', 'r') as fh:
            words = json.load(fh)
            words = {k for k in words.keys() if len(k) == 5}
    else:
        words = wrds
    
    if not rules:
        rules = set()
    
    # pat: is the first word pattern of on an offs 0,1,2
    # 2 = exact place
    # 1 = in word wrong place
    # 0 = not in word
        
    # Develop a set of letters that should be present and onse that should not be
    # Pre develop a list of possibles just by letter regaurdless of position      
    kw = list(fw)
    near = set()
    exact = set()
    bad = set()
    for i, s in enumerate(list(pat)):
        if s == 1:
            near.add((kw[i], i, s))
            rules.add((kw[i], i, s))
        elif s == 2:
            exact.add((kw[i], i, s))
            rules.add((kw[i], i, s))
        else:
            bad.add((kw[i], i, s))

    good_letters = set([t[0] for t in near]).union([t[0] for t in exact])
    bad_letters = set([t[0] for t in bad ])

    likelies = []
    for w in words:
        if good_letters.issubset(w) and bad_letters.isdisjoint(w) :
            likelies.append(w)
    likelies.sort()
    
    passed_words = []

    for w in likelies:
        add = 0
        for l, p, t in rules:
            if t == 2 and w[p] == l:
                add += 1
            elif t == 1 and w[p] != l:
                add += 1 
        if add == len(rules):
            passed_words.append(w)

    return passed_words, rules


if __name__ == '__main__':

    w,l = rtn_words(fw='salet', pat=[0,1,0,1,0])
    print(w)
    w,l = rtn_words(fw='renal', pat=[1,1,0,1,0], wrds=w,rules=l)
    print(w)
    w,l = rtn_words(fw='cream', pat=[0,2,1,1,0], wrds=w,rules=l)
    print(w)
    w,l = rtn_words(fw='argue', pat=[1,2,0,0,2], wrds=w,rules=l)
    print(w)
    w,l = rtn_words(fw='brake', pat=[2,2,2,0,2], wrds=w,rules=l)
    print(w)
    
    

