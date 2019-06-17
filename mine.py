# coding=utf-8

import networkx as nx
import difflib
import matplotlib.pyplot as plt

min_val = 0

def frag(seq):
	#le arquivo in.txt e considera cada linha um fragmento
	file = open('in.txt')
	frags = []
	for line in file:
		for n in line.split("\n"):
			frags.append(n)
	return frags

def sym_val(a, b):
	# procura pela existência de casamento 
	# entre o sufixo de a e o prefixo de b 
	# e vice versa
	sym = []
	for i in range(len(b)):
		aux = a.find(b[i:])
		size = len(b[i:])
		if aux != -1 and (aux == 0 or aux == len(a) - size):
			# ignora quando estiver
			# mais longe da borda do que é o tamanho 
			# garantindo que não está no meio
			sym.append(-1 * size)
		aux = a.find(b[:i])
		size = len(b[:i])
		if aux != -1 and (aux == 0 or aux == len(a) - size):
			sym.append(size)
	return(max(sym, key=abs) if len(sym) else 0)

def find_relevant(frags):
	#para todo par (a, b) chama sym_val(a, b)
	#se o retorno for maior que min_val
	#e diferente de 100%
	#adiciona a e b no valor de retorno
	sym=[];orig=[];dest=[];ign=[];
	for x in range(len(frags) - 1):
		for y in range(len(frags) - 1):
			if x != (y + 1): 
				aux = sym_val(frags[x], frags[y + 1])
				if aux >= len(frags[x]):
					ign.append(frags[x])
				if aux >= len(frags[y + 1]):
					ign.append(frags[y + 1])
				if abs(aux) > min_val:
					sym.append(aux)
					orig.append(frags[x])
					dest.append(frags[y + 1])
	for item in ign:
		# ignorar substrings contidas
		try: 
			while(orig.index(item)):
				index = orig.index(item)
				del orig[index]
				del dest[index]
				del sym[index]
		except: pass
		try:
			while(dest.index(item)):
				index = dest.index(item)
				del orig[index]
				del dest[index]
				del sym[index]
		except: pass
	return(sym, orig, dest)

def main():
	#lê sequencia a partir de arquivo
	frags = frag(seq)
	
	#encontra relevantes
	sym, orig, dest = find_relevant(frags)

	# print(sym)
	# print(orig)
	# print(dest)

	# create graph g
	G = nx.MultiDiGraph()

	#para todos os contigs
		#add contigs no grafo G como vértice 
		#orientação das arestas é dada pela ordem do casamento
		#peso da aresta é dado pelo sym_val

	for i in range(len(sym)):
		H = G.copy()
		if(sym[i] < 0):
			try:
				H.add_weighted_edges_from([(dest[i], orig[i], abs(sym[i]))])
				nx.find_cycle(H, orientation='original')
				# teste se a adição da aresta cria um ciclo
			except:
				# se não, mantém a aresta
				G = H.copy()
		else:
			# inverte origem e destino se negativo
			try:
				H.add_weighted_edges_from([(orig[i], dest[i], abs(sym[i]))])
				nx.find_cycle(H, orientation='original')
				# teste se a adição da aresta cria um ciclo
			except:
				G = H.copy()
				# se não, mantém a aresta

	path = nx.dag_longest_path(G)

	# print(path)

	gem = ""

	for i in range(len(path) - 2):
		gem += path[i][:sym_val(path[i], path[i+1])]

	gem += path[len(path) - 1]

<<<<<<< HEAD
	print(gem)
=======
	# print(gem)
	file = open('out.txt', "w")
	file.write(str(gem))
	file.close()
	#para todos os contigs
		#add contigs no grafo G como vértice 
		#orientação das arestas é dada pela ordem do casamento
		#peso da aresta é dado pelo sym_val
>>>>>>> abc7567a6249d1f9f2b682675757609ab7dd9867

main()