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
sequence="HERV.fasta"
headers,proteome=opener(sequence)
gag=""
pol=""
env=""
gagl=[]
poll=[]
envl=[]
GAGs=[]
POLs=[]
ENVs=[]
GAG=r"C[A-Z]{2}C[A-Z]{4}H[A-Z]{4}C"  #Pattern for the search of Regular Expressions. See the Documentation to understand its origin. 
POL1=r"[GE]N[A-Z]{3}D"				 #Pattern for the search of Regular Expressions. See the Documentation to understand its origin. 
POL2=r"LPQG"  						 #Pattern for the search of Regular Expressions. See the Documentation to understand its origin. 
POL3=r"Y[A-Z]DD"                     #Pattern for the search of Regular Expressions. See the Documentation to understand its origin. 
ENV1=r"C[A-Z]{6}C[CHRYS]"            #Pattern for the search of Regular Expressions. See the Documentation to understand its origin. 
ENV2=r"C[A-Z]{7}[CY][CS]"            #Pattern for the search of Regular Expressions. See the Documentation to understand its origin. 
ENV3=r"C[A-Z]{6}F"                   #Pattern for the search of Regular Expressions. See the Documentation to understand its origin. 

for i in proteome:
    protein=translation(i)
    for l in protein:     #Loop to find the patterns.
        fGAG=re.findall(GAG,l)
        fPOL1=re.findall(POL1,l)
        fPOL2=re.findall(POL2,l)
        fPOL3=re.findall(POL3,l)
        fENV1=re.findall(ENV1,l)
        fENV2=re.findall(ENV2,l)
        fENV3=re.findall(ENV3,l)
        if len(fGAG)!=0:   
            gagl.append(l)
        elif len(fPOL1)!=0 or len(fPOL2)!=0 or len(fPOL3)!=0:
            poll.append(l)
        elif len(fENV1)!=0 or len(fENV2)!=0 or len(fENV3)!=0:
            envl.append(l)
    if len(gagl)>0:      #This "if" identify if the program found active ORFs and saves the biggest one. 
        gag=listMax(gagl)
    else:                #If the program identifies nothing, print "Not ORF"
        gag="Not ORF"
    if len(poll)>0:
        pol=listMax(poll)
    else:
        pol="Not ORF"
    if len(envl)>0:
        env=listMax(envl)
    else:
        env="Not ORF"
    GAGs.append(gag)
    POLs.append(pol)
    ENVs.append(env)
    gagl=[]
    poll=[]
    envl=[]

data=zip(headers,proteome,GAGs,POLs,ENVs) #Creates a tuple with the collected information. 

myFile = open('ervf.csv', 'w')   #Finally, creates a "CSV" file with all the information.
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(data)
