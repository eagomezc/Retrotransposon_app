import re

def mzidentml(fil):
    from pyteomics import mzid
    with mzid.read(fil, read_schema=False) as f:
        sequences = [item['SpectrumIdentificationItem'][0]['PeptideSequence'] for item in f]
    return sequences

def mzidentml(fil):
    pattern = r"<PeptideSequence>([A-Z]+)"
    mz = open(fil,"r")
    lines=mz.readlines()
    peptides=[]
    for l in lines:
        if "<PeptideSequence>" in l:
            rgx=re.findall(pattern,l)
            if len(rgx)!=0: 
                peptide="".join(rgx)
                peptides.append(peptide)
    return peptides

def mztab(fil):
    pattern = r"PSM\s([A-Z]+)"
    mz = open(fil,"r")
    lines=mz.readlines()
    peptides=[]
    for l in lines:
        if "PSM" in l:
            rgx=re.findall(pattern,l)
            if len(rgx)!=0: 
                peptide="".join(rgx)
                peptides.append(peptide)
    return peptides

