#!/usr/bin/python3

# https://docs.python.org/3/library/argparse.html
import argparse

import mbdev

parser = argparse.ArgumentParser(
    description='''generating printable slides.''',
    epilog='''by Mateusz Bysiek''',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    'filename', metavar='<filename-without-extension>', type=str,
    help='''source filename wihtout .pdf extension''')

args = parser.parse_args()

output = '{name}_print.tex'.format(name=args.filename)

with open(output, 'w') as f:
		f.write(r'''\documentclass[a4paper]{article}

\usepackage{geometry}
\geometry{margin=4cm}

\usepackage{pdfpages}

\begin{document}

%,offset=10mm 10mm
\includepdf[nup=2x2,pages=-,delta=5mm 5mm,frame=true,landscape]{''')
		f.write(args.filename)
		f.write(r'''.pdf}

\end{document}
''')

mbdev.execute(['pdflatex', output], indent=2)

mbdev.execute(['rm', '-rf', output + '.*'], indent=2)
