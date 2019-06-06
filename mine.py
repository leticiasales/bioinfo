# coding=utf-8

import networkx as nx
import difflib
import matplotlib.pyplot as plt

min_val = 0

def frag(seq):
	#faz uma quebra aleatória do DNA
	#resultando em várias cópias quebradas 
	#em posições aleatórias de suas sequências
	# file = open('in.txt')
	# frags = []
	# for line in file:
	# 	for n in line.split("\n"):
	# 		frags.append(n)
	frags = ["abc", "gbf", "cefg"]
	return frags

def sym_val_2(a, b):
	#procurar pela existência de casamento 
	#entre o sufixo de a e o prefixo de b
	sym = []
	for i in range(len(b)):
		aux = a.find(b[i:])
		size = len(b[i:])
		if aux != -1 and (aux == 0 or aux == len(a) - size):
			sym.append(-1 * size)
		aux = a.find(b[:i])
		size = len(b[:i])
		if aux != -1 and (aux == 0 or aux == len(a) - size):
			sym.append(size)
	return(max(sym, key=abs) if len(sym) else 0)

# tamanho da substring encontrada é
	# adicionar pra ignorar quando estiver
	# mais longe da borda do que é o tamanho

def sym_val_full(a, b):
	#escolhe máximo entra sym_val_2 para
	#a e b e sym_val_2 para b e a
	return sym_val_2(a, b)

def find_relevant(frags):
	#para todo par (a, b) chama sym_val_full(a, b)
	#se o retorno for maior que min_val
	#e diferente de 100%
	#adiciona a e b no valor de retorno
	sym=[];orig=[];dest=[];ign=[];
	for x in range(len(frags) - 1):
		for y in range(len(frags) - 1):
			if x != (y + 1): 
				aux = sym_val_full(frags[x], frags[y + 1])
				if aux >= len(frags[x]):
					ign.append(frags[x])
				if aux >= len(frags[y + 1]):
					ign.append(frags[y + 1])
				if abs(aux) > min_val:
					sym.append(aux)
					orig.append(frags[x])
					dest.append(frags[y + 1])
	for item in ign:
		try: 
			while(orig.index(item)):
				# print(orig)
				index = orig.index(item)
				del orig[index]
				del dest[index]
				del sym[index]
				# print(orig)
		except: pass
		try:
			while(dest.index(item)):
				# print(dest)
				index = dest.index(item)
				del orig[index]
				del dest[index]
				del sym[index]
				# print(dest)
		except: pass
	return(sym, orig, dest)

def main():
	#lê sequencia
	seq = 'abcdefghi'

	#fragmenta sequencia
	frags = frag(seq)
	
	#encontra relevantes
	sym, orig, dest = find_relevant(frags)

	# print(sym)
	# print(orig)
	# print(dest)

	# create graph g
	G = nx.MultiDiGraph()

	for i in range(len(sym)):
		if(sym[i] < 0):
			G.add_weighted_edges_from([(dest[i], orig[i], abs(sym[i]))])
		else:
			G.add_weighted_edges_from([(orig[i], dest[i], abs(sym[i]))])
		#g_o = find_or_create(graph g, orig[i])
		#g_d = find_or_create(graph g, dest[i])
		#create_edge(from: g_o, to: g_d, peso: sym[i])

	for (u, v, wt) in G.edges.data('weight'):
		print('(%s, %s, %d)' % (u, v, wt))

	plt.subplot(121)
	nx.draw(G, with_labels=True, font_weight='bold')
	plt.show()

	print(nx.dag_longest_path(G))

	#para todos os contigs
		#add contigs no grafo G como vértice 
		#orientação das arestas é dada pela ordem do casamento
		#peso da aresta é dado pelo sym_val

	# return find_longest_path(g)
main()