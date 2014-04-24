# A way to process input to get the haikus out
import haiku

fin = open("input.txt", 'r')

t = []
for line in fin.read().split('\n'):
    phrases = line.split()
    words = []
    for phrase in phrases:
        words.append(w.translate(string.maketrans("",""), string.punctuation)) for w in phrase.split('-') if w
    t.append(words)

fin.close()

haikus = set([])
for i in range(len(t)/4):
    haikus.add(Haiku(t[i*4+1],t[i*4+2],t[i*4+3],raw_lines = True))
