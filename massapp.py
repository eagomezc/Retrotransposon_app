def mzidentml(fil):
    from pyteomics import mzid
    with mzid.read(fil, read_schema=False) as f:
        sequences = [item['SpectrumIdentificationItem'][0]['PeptideSequence'] for item in f]
    return sequences

