#!/usr/bin/python3

# https://docs.python.org/3/library/argparse.html
import argparse

import mbdev

parser = argparse.ArgumentParser(
    description='''Generates printable version of beamer slides. When you
 actually print the output file, please select 'US letter' paper size due to
 margin errors on some printers.''',
    epilog='''by Mateusz Bysiek''',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    'filename', metavar='<filename-without-extension>', type=str,
    help='''source filename wihtout .pdf extension''')

args = parser.parse_args()

output_prefix = args.filename + '_print'
output = output_prefix + '.tex'

with open(output, 'w') as f:
		f.write(r'''\documentclass[a4paper]{article}

\usepackage{pdfpages}

\begin{document}

\includepdf[nup=2x2,pages=-,delta=5mm 5mm,frame=true,landscape]{''')
		f.write(args.filename)
		f.write(r'''.pdf}

\end{document}
''')

mbdev.execute(['pdflatex', output], indent=2)

mbdev.execute(['mv', output_prefix + '.pdf', output_prefix + 'able.pdf'])

mbdev.execute(['rm', '-rf', output_prefix + '.*'])
