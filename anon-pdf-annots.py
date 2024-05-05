#!/usr/bin/env python

import argparse
import fitz

parser = argparse.ArgumentParser()

parser.add_argument("infile", help="Input file", type=str)
parser.add_argument("outfile", help="Output file", type=str)
parser.add_argument("-a", "--annot_auth", help="Annotation author name", type=str, default="rev", required=False)

args = parser.parse_args()

pages = fitz.open(args.infile)


for page in pages:
    xrefs = [annot.xref for annot in page.annots()]
    for xref in xrefs:
        annot = page.load_annot(xref)
        info = annot.info # get info dict
        info["title"] = args.annot_auth # set author
        annot.set_info(info) 
        annot.update()
        page = pages.reload_page(page)

if args.outfile == args.infile:
    pages.saveIncr()
else:
    pages.save(args.outfile)

