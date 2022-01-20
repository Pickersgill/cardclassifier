try:
    from . import mm
    from . import nmm
except:
    import mm
    import nmm

MM = mm.MM
NMM = nmm.TwoMM
