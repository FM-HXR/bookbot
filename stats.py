def word_counter(booktext):
    splitText = booktext.split()
    return f"Found {len(splitText)} total words"
    
def charaCounter(text):
    bookWords = text.split()
    bookChara = []
    charaDict = {}
    for word in bookWords:
        bookChara += sorted(word)
        
    for chara in sorted(bookChara):
        if chara.lower() in charaDict:
            charaDict[chara.lower()] += 1
        else:
            charaDict[chara.lower()] = 1
    return charaDict