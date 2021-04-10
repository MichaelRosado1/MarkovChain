import string
import random
from graph import Graph, Vertex

def getWordsFromText(textPath):
    with open(textPath, 'r') as f:
        text = f.read()

        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation)) #this will remove the punctuation from the text to decrease complexity
    
    words = text.split()
    return words

def makeGraph(words):
    g = Graph()

    previousWord = None

    for word in words:
        wordVertex = g.getVertex(word)

        if previousWord:
            previousWord.incrementEdge(wordVertex)

        previousWord = wordVertex

    g.generateProbMapping()
    return g

def compose(g, words, length=50):
    composition = []
    word = g.getVertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.getNextWord(word)
    return composition

def main():
    words = getWordsFromText('texts/RomeoAndJuliet.txt')
    g = makeGraph(words)
    composition = compose(g, words, 100)
    print(' '.join(composition))

    
main()