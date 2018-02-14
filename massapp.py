import re

#***********
# mzIdentML
#***********

def mzidentml(fil): #This function generates a list of all the peptide identifications from a mzIdentML file 
    from pyteomics import mzid  
    with mzid.read(fil, read_schema=False) as f:  #reads the mzid file 
        sequences = [item['SpectrumIdentificationItem'][0]['PeptideSequence'] for item in f] #for each Spectrum Identification Item gets the
    return sequences									     # peptide sequences.

#***********
# mzTab
#***********

def mztab(fil):  #This function generates a list of all the peptide identifcations from a mzTab file 
    pattern = r"PSM\s([A-Z]+)" #This pattern identifies the identification sections of the mzTab file and save the peptide sequence.
    mz = open(fil,"r") #Read the file.
    lines=mz.readlines() #Read the file line by line. 
    peptides=[]
    for l in lines:
        if "PSM" in l:
            rgx=re.findall(pattern,l) #Gets all the peptide sequences from the section PSM of the mzTab file. 
            if len(rgx)!=0: 
                peptide="".join(rgx)
                peptides.append(peptide) #Saves the peptide sequences in a list. 
    return peptides

