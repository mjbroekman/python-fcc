'''Generate content from the available graph data

based on:
    - https://github.com/kying18/graph-composer.git

inspired by:
    - https://www.freecodecamp.org/news/python-projects-for-beginners/#markov-chain-text-composer-python-project

additions / modifications:
    - debugging / length arguments to main()
    - no need to generate the edge/weight lists
'''
import string
import random

from graph import Graph, Vertex

def get_words(data_path):
    with open(data_path,'r') as data_source:
        data = data_source.read()
        data = ' '.join(data.split())
        data = data.lower()
        data = data.translate(str.maketrans('','',string.punctuation))

    return data.split()


def make_graph(labels):
    graph = Graph()
    prev_label = None

    for label in labels:
        node = graph.get_vertex(label)

        if prev_label:
            graph.connect_to(prev_label,node)
        
        prev_label = label
    
    return graph

def compose(graph,words,length=100):
    composition = []
    word = graph.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.label)
        word = graph.get_next_node(word)
    
    return composition

def main(length=100,debug=False):
    data = get_words('../LICENSE')
    graph = make_graph(data)
    composition = compose(graph,data,length)
    if debug:
        print(graph)
    return ' '.join(composition)

if __name__ == '__main__':
    print(main(length=25))
