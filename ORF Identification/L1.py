#************
# FUNCTIONS
#************

def opener(seq):
""" This function opens the Fasta file and separates the headers 
	from the sequences for a better manipulation """
    FASTA=open(seq, "r")
    lines=FASTA.readlines()
    headers=[]
    seqs=[]
    header=""
    seq=""
    for l in range(0,len(lines)-1):
        if ">" in lines[l]:
            header=lines[l]
            header=header.replace("\n","")
            for m in range(l+1,len(lines)):
                if ">" not in lines[m]:
                    seq+=lines[m].rstrip()
                else:
                    break
            headers.append(header)
            seqs.append(seq)
            header=""
            seq=""
    return headers,seqs

def reversecom(proteine):
""" This functions generates the reverse complementary of the DNA sequence 
	of each of the retrotransposon in the FASTA file """
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A','N': 'N'} 
    bases = list(proteine) 
    bases = [complement[base] for base in bases] 
    proteiner=''.join(bases)
    proteiner=proteiner[::-1]
    return proteiner

def translation(protein):
""" Biopython has a function to translate DNA to Amino Acid Sequences, but since 
	we are looking for specific ORFs, we decided to come out with our own translation
	function """
    seq=""
    seqr=""
    rframes=[protein,reversecom(protein)]
    seqs=[]
    for proteine in rframes: #This loop allows to look for ORFs in the original sequence and its reverse complementary.
        for m in range(0,len(proteine)):
            if proteine[m:m + 3]=='ATG': #Identify the Start Codon
                protein=proteine[m:]
                for l in range(0,len(protein)):
                    if protein[l*3:l*3 + 3]=='ATG':
                        seq+="M".rstrip()
                    elif protein[l*3:l*3 + 3]=='AAA':
                        seq+="K".rstrip()
                    elif protein[l*3:l*3 + 3]=='AAG':
                        seq+="K".rstrip()
                    elif protein[l*3:l*3 + 3]=='ATA':
                        seq+="I".rstrip()
                    elif protein[l*3:l*3 + 3]=='AAC':
                        seq+="N".rstrip()    
                    elif protein[l*3:l*3 + 3]=='AAT':
                        seq+="N".rstrip()
                    elif protein[l*3:l*3 + 3]=='GAA':
                        seq+="E".rstrip()
                    elif protein[l*3:l*3 + 3]=='GAG':
                        seq+="E".rstrip()
                    elif protein[l*3:l*3 + 3]=='GAC':
                        seq+="D".rstrip()
                    elif protein[l*3:l*3 + 3]=='GAT':
                        seq+="D".rstrip()
                    elif protein[l*3:l*3 + 3]=='CAA':
                        seq+="Q".rstrip()
                    elif protein[l*3:l*3 + 3]=='CAG':
                        seq+="Q".rstrip()
                    elif protein[l*3:l*3 + 3]=='CAC':
                        seq+="H".rstrip()
                    elif protein[l*3:l*3 + 3]=='CAT':
                        seq+="H".rstrip()
                    elif protein[l*3:l*3 + 3]=='TAC':
                        seq+="Y".rstrip()
                    elif protein[l*3:l*3 + 3]=='TAT':
                        seq+="Y".rstrip()
                    elif protein[l*3:l*3 + 3]=='AGC':
                        seq+="S".rstrip()
                    elif protein[l*3:l*3 + 3]=='AGT':
                        seq+="S".rstrip()
                    elif protein[l*3:l*3 + 3]=='GGA':
                        seq+="G".rstrip()
                    elif protein[l*3:l*3 + 3]=='GGG':
                        seq+="G".rstrip()
                    elif protein[l*3:l*3 + 3]=='GGC':
                        seq+="G".rstrip()
                    elif protein[l*3:l*3 + 3]=='GGT':
                        seq+="G".rstrip()
                    elif protein[l*3:l*3 + 3]=='AGG':
                        seq+="R".rstrip()
                    elif protein[l*3:l*3 + 3]=='AGA':
                        seq+="R".rstrip()    
                    elif protein[l*3:l*3 + 3]=='CGA':
                        seq+="R".rstrip()
                    elif protein[l*3:l*3 + 3]=='CGG':
                        seq+="R".rstrip()
                    elif protein[l*3:l*3 + 3]=='CGC':
                        seq+="R".rstrip()
                    elif protein[l*3:l*3 + 3]=='CGT':
                        seq+="R".rstrip()
                    elif protein[l*3:l*3 + 3]=='TGG':
                        seq+="W".rstrip()
                    elif protein[l*3:l*3 + 3]=='TGC':
                        seq+="C".rstrip()
                    elif protein[l*3:l*3 + 3]=='TGT':
                        seq+="C".rstrip()
                    elif protein[l*3:l*3 + 3]=='ACA':
                        seq+="T".rstrip()
                    elif protein[l*3:l*3 + 3]=='ACG':
                        seq+="T".rstrip()
                    elif protein[l*3:l*3 + 3]=='ACC':
                        seq+="T".rstrip()
                    elif protein[l*3:l*3 + 3]=='ACT':
                        seq+="T".rstrip()
                    elif protein[l*3:l*3 + 3]=='GCA':
                        seq+="A".rstrip()
                    elif protein[l*3:l*3 + 3]=='GCG':
                        seq+="A".rstrip() 
                    elif protein[l*3:l*3 + 3]=='GCC':
                        seq+="A".rstrip()
                    elif protein[l*3:l*3 + 3]=='GCT':
                        seq+="A".rstrip()
                    elif protein[l*3:l*3 + 3]=='CCA':
                        seq+="P".rstrip()
                    elif protein[l*3:l*3 + 3]=='CCG':
                        seq+="P".rstrip()
                    elif protein[l*3:l*3 + 3]=='CCC':
                        seq+="P".rstrip()
                    elif protein[l*3:l*3 + 3]=='CCT':
                        seq+="P".rstrip()
                    elif protein[l*3:l*3 + 3]=='TCA':
                        seq+="S".rstrip()
                    elif protein[l*3:l*3 + 3]=='TCG':
                        seq+="S".rstrip()
                    elif protein[l*3:l*3 + 3]=='TCC':
                        seq+="S".rstrip()
                    elif protein[l*3:l*3 + 3]=='TCT':
                        seq+="S".rstrip()
                    elif protein[l*3:l*3 + 3]=='ATC':
                        seq+="I".rstrip()
                    elif protein[l*3:l*3 + 3]=='ATT':
                        seq+="I".rstrip()
                    elif protein[l*3:l*3 + 3]=='GTA':
                        seq+="V".rstrip()
                    elif protein[l*3:l*3 + 3]=='GTG':
                        seq+="V".rstrip()
                    elif protein[l*3:l*3 + 3]=='GTC':
                        seq+="V".rstrip()
                    elif protein[l*3:l*3 + 3]=='GTT':
                        seq+="V".rstrip()
                    elif protein[l*3:l*3 + 3]=='CTA':
                        seq+="L".rstrip()
                    elif protein[l*3:l*3 + 3]=='CTG':
                        seq+="L".rstrip()
                    elif protein[l*3:l*3 + 3]=='CTC':
                        seq+="L".rstrip()
                    elif protein[l*3:l*3 + 3]=='CTT':
                        seq+="L".rstrip()
                    elif protein[l*3:l*3 + 3]=='TTA':
                        seq+="L".rstrip()
                    elif protein[l*3:l*3 + 3]=='TTG':
                        seq+="L".rstrip()
                    elif protein[l*3:l*3 + 3]=='TTC':
                        seq+="F".rstrip()
                    elif protein[l*3:l*3 + 3]=='TTT':
                        seq+="F".rstrip()
                    elif protein[l*3:l*3 + 3]=='TGA':
                        break # If the program identify a Stop Codon, it breaks the loop and continues with the next one.
                    elif protein[l*3:l*3 + 3]=='TAA':
                        break
                    elif protein[l*3:l*3 + 3]=='TAG':
                        break
                    else:
                        seq+="X".rstrip() #There are some unidentified nucleotides in the sequences. Instead of leaving null, put an X. 
                le=m+(len(seq)*3)+3 #This part makes sure that the ORF has a Stop Codon. If the length of the amino acid sequence * 3 (for each codon) plus 3 
                if le<=len(proteine): #(for the Stop Codon) + the position of its first amino acid is longer than the whole DNA sequence, that means that the
                    if len(seq)>=300: #amino acid sequence stop because it got to the end of the DNA sequence instead of finding an Stop Codon.
                        seqs.append(seq)  #Finally, it only calls the sequences that are longer thant 300 amino acids since we know the size of the ORFs.
            seq=""
    return seqs

def listMax(a):
""" This function calls for the biggest ORF since it's possible to find the Start Codon
	inside of an ORF, which can generate small amino acids sequences of a bigger peptide """
    large=a[0]
    for i in range(1,len(a)):
        if len(large)>len(a[i]):
            large=large
        else:
            large=a[i]
    return large

#************
# APPLICATION
#************
	
import csv
import re
sequence="L1s.fasta" 
headers,proteome=opener(sequence)
orf1=""
orf2=""
orf0=""
orf1l=[]
orf2l=[]
orf0l=[]
ORF1s=[]
ORF2s=[]
ORF0s=[]
ORF1=r"RREWGPIFN[IT]L"  #Pattern for the search of Regular Expressions. See the Documentation to understand its origin. 
ORF2=r"CWRGCG"			#Pattern for the search of Regular Expressions. See the Documentation to understand its origin.
ORF2b=r"LKI[KT]GWRK[IS]YQ[AV]N" #Pattern for the search of Regular Expressions. See the Documentation to understand its origin.
ORF0=r"M[AV][GD][ATY]"  #Pattern for the search of Regular Expressions. See the Documentation to understand its origin.


for i in proteome:
    protein=translation(i)
    for l in protein:  #Loop to find the patterns.
        fORF1=re.findall(ORF1,l)
        fORF2=re.findall(ORF2,l)
        fORF2b=re.findall(ORF2b,l)
        fORF0=re.findall(ORF0,l)
        if len(fORF1)!=0:
            orf1l.append(l)
        elif len(fORF2)!=0 or len(fORF2b)!=0:
            orf2l.append(l)
        elif len(fORF0)!=0:
            orf0l.append(l)
    if len(orf1l)>0: 	#This "if" identify if the program found active ORFs and saves the biggest one. 
        orf1=listMax(orf1l)
    else:				#If the program identifies nothing, print "Not ORF"
        orf1="Not ORF"
    if len(orf2l)>0:
        orf2=listMax(orf2l)
    else:
        orf2="Not ORF"
    if len(orf0l)>0:
        orf0=listMax(orf0l)
    else:
        orf0="Not ORF"
    ORF1s.append(orf1)
    ORF2s.append(orf2)
    ORF0s.append(orf0)
    orf1l=[]
    orf2l=[]
    orf0l=[]
 

data=zip(headers,proteome,ORF1s,ORF2s,ORF0s)  #Creates a tuple with the collected information. 

myFile = open('L1sf.csv', 'w')   #Finally, creates a "CSV" file with all the information. 
with myFile:    
    writer = csv.writer(myFile)
    writer.writerows(data)
