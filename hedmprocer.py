#!/usr/env/bin python

"""
hedmprocer
    prep:  pre-processing data
    cali:  perform automated calibration
    recon: perform reconstruction based on prior calibration results
    post:  perform selected post-processing on reconstruction results
    viz:   generate selected predefined plots

Usage:
    hedmprocer.py prep     <CONFIGFILE>
    hedmprocer.py recon    <CONFIGFILE>
    hedmprocer.py post     <CONFIGFILE>
    hedmprocer.py -h | --help
    hedmprocer.py --version
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt

if __name__ == "__main__":
    argvs = docopt(__doc__, argv=None, help=True, version="tomoprocer v0.0.1")
    print(argvs)

    if argvs['prep']:
        pass
    elif argvs['recon']:
        pass
    elif argvs['post']:
        pass
    else:
        raise ValueError("Please use --help to check available optoins")
