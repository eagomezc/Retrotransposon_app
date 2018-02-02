def opener(seq):
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

