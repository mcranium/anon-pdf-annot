# anon-pdf-annot
**Anonymize or modify PDF annotations**

Have you ever started reviewing a manuscript and noticed way down the process that you forgot toremove your name from the PDF annotations?

This simple command line script, allows you to change the author information of all annotations in a PDF at once.

```
anon-pdf-annots input.pdf output.pdf -a authorname
```

The ´authorname´, can be ommitted and defaults to "rev".


## Dependencies
- Python 3
- [pymupdf](https://pypi.org/project/PyMuPDF/)


## Disclaimer
Only tested on Linux.