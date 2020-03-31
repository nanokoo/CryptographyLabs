#!/usr/bin/python3
from itertools import cycle, islice

def encrypt(K, P):
	S = [0, 1, 2, 3, 4, 5, 6, 7]
	T = list(islice(cycle(K), len(S)))
	print(T)
	
	j = 0
	for i in range(0,8):
		j = (j + S[i] + T[i]) % 8
		S[i], S[j] = S[j], S[i]
		print(S)
		
	
	i = 0
	j = 0
	C = []
	for p in P:
		i = (i + 1) % 8
		j = (j + S[i]) % 8
		S[i], S[j] = S[j], S[i]
		t = (S[i] + S[j]) % 8
		k = S[t]
		C.append(k ^ p)
		
	return C

	
	
if __name__ == "__main__":

	K = [1, 2, 3, 6]
	P = [1, 2, 2, 2]
	C = encrypt(K, P)
	print(C)

