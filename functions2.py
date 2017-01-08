def print_solution(r):
	print '\n'.join(r)

# 1.2.3 Composition
def Composition(k, seq):
	r = []
	for i in range(len(seq)-k+1):
		subseq = seq[i:i+k]
		if subseq not in r:
			r.append(subseq)
	return r


def main():
	print_solution(Composition(100, 'CTCCCCTTTATCCGCCAGGTCTAGTCTAGGCACTTGAAGAGTTATAACGACCCTACGGAGGGCTAAGGGTTGTTGGTCACGCGATAGATATATACTTATACAAATGAAGTCTCGTCAACCTCCTGACCAAACCATCTGGTTGCCTCACGAGTAGGTATGTGTTCGGAGGGCCACTCCCAGTCAGCCAGAATCACACATAGTAAGCAGGTATCGATGCGCTGAGCCCTTGCGAAAAATATGACCGACTAAAGGGACGTCCCGGGCCCGCTTTCGATTACTAAGGTTCTGCGATTGAACCTCACCAATGCAGTCTCACCACTTACCCTTTTGGGTGTGGTTGAACCAAGGAATGAATAAGGAAATAAAATATTGTCGTGGCAAGCTTCAGGGATGTTGTCACAGGCCGGACAGGTGCGTTATTATCGCCAACTCAAAGAACAAATTAGTAATATACTAGGCGCTGGGACACACTCTGGTAACAACCGCAACCTAACAGATTAGCCAGTTACGTATAGTGGGAAGCTCTCAAATATTAGTGCAGATGCCGGGATATCACGTTCACTTAGCCGACGGAATATTTGGAGTGCGCAAAAATGCCGTCCACACCCTCCGGCGTCGTCGGACTGACTACGCTGAGGCTGGGAGACGACGCTTCTCCCCGGTTGTAAAAAACTTAATATCGCGGACGTTCTTACGACGCGAAGAACATAAAAGCGCGGGACGGTGTTAAGTGCTTCGAATACGACTCCAACACACAACACTAAACTACGCCCTGAATCAATCTGCATGTTCTTGTTGGCAATGGACGCCTGCTATATGGAACACGTGCAGGATATTGACGACTAGTGCGATGCAATACCGCAAGACAACCCATAAAGTGTCGATCGAGGTGACAATTTAAAAACTCCGCTTGACTGAAAAGCATTTCTCGTATTGAACGGCCGTGCATAGACTAGAGCGGGCCTAGTACTCTAGGAACGCGACACACTCCGTCTTAGGGACGTAGTGTTAGATATTGCGAATGAGTGTCCGAGAACGAAATCACTCAACGACTATGCAACCAATAATAAGCTGATACGCGCACACCCAGCACCGGTGCAGTCATATGTCGTTGAGTCCGCCGAATGACATCGTTCGCGCCTATTTTGGTAGACATTAATAAACCCGGCGCGCGGGATCAAGGCAAGGGCGCTGCGCTCGGGTACAAGCACCGGTGTTAGACTACCAACATCATCGCTAGCTGATGTAAGGCCTGCTATTATAGAGCTCACATCCCTTGGTCGAAGAGATTGGCTCGAGTACCAACCCACGATTTGCGCAAACATGCCATGTGCCTATTCTCATTTGTTTTGACCGAAACTCCCGAGGTCCGAGTACGCTAATCACCAGGAGCTAACGGATTAATTCTCCGAGCCTAATGCAGATCTTAGGAAAAGTCTCCGCCAAATGGGGGGATGAAATCCTTGCACGTCATAGCAACACAAATTGAAGTCCACTGCGTGGGCTCTTGTACGATCCGCGCAGCGCATACGTGTTTGCGTCTAGGGAGTGAATAGGCCCCAGCAGGCTGATTGCGACGCGGCACTGTTAGAATCCTATGGAACAAGTGGGAACAGTAAATATCAATCTTACAAAGGTGTGTCCAACAAGAGATTGAGGCGGCATGGCTATGATTTTTTTATCGTTTGCCAAAGTGCCGCAGCCGAGCACGCACGCCGCTTTGTCACATGCGAACTGACTCAAACGTGCGGTAGTGCCCAGCGCAACTTGAAGACGTAGAAGTCGAGGGATATCCCGCAATCGCACGGCAAGTAAGAGACCTCAGATCAGCTACGCCACTTTCGGGGGCGCCGGCTTATCCCGCCACCTTGCGAACAAATGGGTACATCTATTTGCTTCAGACCCACGTAAACTCGGATACTGGTACCTGGATGAGCTCGCTTCTACCAATGTCTATCTTGGGATAGCCCGGTATGGGGAGACTCTGGAAAGCAGCGTGGATCACCGATTTTCTTATCCCTGCCACTAAGACTACGGTGCTTGCCGAGCTTCTACAGGTGGAAAACCGATACCGTTGATTATTCAGGCAACAATAAAGCCAGCCGGTTGAATGGTTTCTAATACTGCCTGCGAGCGCCTAATTGGGCCGTAGTTCGTCACACATCCACGGAGGATGCTATCCTGGTACCTCGCGTGAACTATGACCAGTCCTAGAAGTTAAAGGAGGGTTTGCTAAAATAGGGATCTGACGTCACGGCCGGCCGCTTCGCTTTAAACTGCGATTATGGGATTGACGTGTCACTCCTCGGAGTATGAATCTTATATCGTGAGGTTAAACCCCATCGGCATCAACTCTTTGGAAGCTCCCTGTCGCTAGCCCTAGTAAGGTTCACGGACGGTATGTGGATCTGAAAGCTGTGCTGCTCTAGTCGATTCCCAGGGAGCATCACAAGGGAAGCTCTCTATTCCAGAAGTAAGGGGAACTGGTAACGCGAGGTGAATAGTCCGATGACGTATATTCCCCAGACAAGCACATAGATTCGTATTAAGATTCAGGATGTGTATAAACTATTGGTCCCTTAATAGGAGTGATTTCGAACACGTCCCACCTCAGATTTACTCCTCAGGTTACAAAAACAGCAAATAGATCGTACGCAGGGCCCGCCCGCACATAATTGGATAGCCATGGAACACAGTTCGGGCATCTATGCACGCCCCAGACGAAGAAATACAGATAGGTGGAACTTCGAAGTAACACTGACATTCGCCGCGGTCGTGATGTCATGCGACTATCAGCGGCTGCCTGCAACAGCTCCTATGTCTCGGTGTTCACATCAATGAGTAACAGTGAGCTTTGCGCACCCTATGGTTACGCTACTATGCCCAAGAGCAAGCCCACAGTTGACTTCTTGTGGGATTTACTCTGTTAACATATGCGCACTCAATATGGCACGTGAGTCAATCAATAGGGGCTACTACGCTTCTAGCGAGTCTGTATCACGCTTCTTTCCTGGTGACCCTCTCCTTTAGGGGGTCAGAGCACGTTAGCCTTAAACGAGAGCCATTGAACCTGTATATTAGAAGGATATCGCACCCCTGAGTTACTTAACCCGTATCTAGGACTGATTCTACGTCGCTGAAATTCCGGATAATTTCGTCGGGCGTGTAGGCAGAGAGGGTTGGAGACAGCTCCTGTGCCTAGGGTAGCTCTTTTTTGTTAAGTTACCATTCGAGGACGAACTCGAATAGTTATGGTTTGTGTGTACCGCTATAATGCGAACAATGGCCTTACCTGTCCGCGTGCCTTAAACTAGATTCAGTACCCTTATTGCTCTCCTGGGCAAGTACCTTCACCCACGCCAGACCCGACTGTCTCGATTAAAGCCCGGGGACCGGAAGAATGGTAATGACAGCCTTACATTGCCATTACAGATTTGTTATCATCGCGTCATCATTCAATCAAACGGATTGGGTGTGCGCGAAAAGCTCCTTGGATTAGCGACCACGCTTTCAGTTGGGTGCGTACCCACGATTATAATTCCGCCAGCATTCAGGAAGCCTCATCCTGCAGAGCGTAGTTATATGGAAACAGTGAGAGGTCTATCATCCGGACCCGGCGTCGTAGGTCAACTCGAATAATCCCGACATTCTATACATCATTCATGGAAAATGAGAATGCCCAAGATGAGTAAATAATTCCACGGCTCCATGGGACACAGACTAAGCACGGCCCCTGTATTAGCCAGACTCTTCAGGGTGCTTCGCAACCAGTCCACCGCGTAGTGCCATGTGCATAGATCGATATACGTTGTGATTACGACCGATATCCTTTGTTACTCGGACGTTCTGCGGGCCGGGAGATGTTCGTGTTAACCGTTCAAGGACTGTCTCACATATTAACTATTTTTAGCACTACCCCCCCCGGACTGAACGTCGATTTAGGCCGTGGGACATCGAACACATTTCGTGGCCCAGGCCATACAACATCTGAGTTTTCCCTATGACCTGCCGCCCAAATCCACCGCCGAGAGAAGAGGTCCCACGTTCGTTCGAACTCCAAACTAGTTAGCAGGTATTGCTATGCGATGGGTCTATCCTCAGCGCTGCCACTCGCGCTCGTATTGACCGGGTTATGTATATGGTCTATGTACGTCCGTTGGTCAGTGAGGCGTAGCTGACCCATAAAATAACTTGCCATTATAGCCTATAGCAGTGATCTGTGGTTATCATCATTGGCCGGTCTCATTTCCATTAAGTCATGCCGTAACGAGTGCTGAAGGACGGAGGGTTCAGTACACCCGACTGATTGGCTGAGACGGTCCTCGTCTAATTACTAATAGGGGCTTCTTACGGATGTCGACGCATACGTGTTATGTTCCGCAAAAAACCGAGGCAGGAACACTCTCATGGATGCGATAAGGCAGCACATTTACTGCTTGGTGCCGGGCGACATTGCGTGTTTTCTACATAGCTTCCTACAGTGGCGATAAAATACGGGCAAAAGATCACGGACCCAGCGATGTCCATCGGTCAAGGGCTCGGTGTGCCACACATCTCGTCGGGCTGTATAAGCCTGATTTCAACATACGTCCGAAAGAAGAGATTGCCTGCCAACGCTCATAGGGTTTTCTACAACCCGCGTGTGGCTTCAAAATTCTGACCCGAAGTCGGCACGCCACCGGACACATCTACGAGGTGTGGGGTCCATCGGCTTAACGTAGTTTTAGTGCTTTCCTTATCCTAACCCAACCAGGTAATGAAATAGGTCGACGATATAATCAATCATCCTGGCTACCTACGGCTACTGTGGCTTTGGTCTGATGATGTATCCCGAATCCGCGGAGACTTAAACTGTGACGTTCCGCAAATCGACGCGGTCAGAGGTGCGATTACAGCCGAGGGGAGCCGACACACGTTCCTTGTCGAGGGTGCCCGTTGAGATACTGGGCCCGTCGGGCCATCGCTTTTCGGGAGTTTTGGAAATTGCGACATAATGTAGT'))



main()
