#!/usr/bin/python3

"""Generate printable slides (4 slides on one page) from a PDF.

Assuming that the PDF page size is what beamer would generate by default.

On different input page size the page placement might not be optimal.
"""

import argparse
import subprocess


def main(args=None):
    """Commandline interface of the printable slides generator."""

    parser = argparse.ArgumentParser(
        description='''Generates printable version of beamer slides. The resulting
     file will have the name "<filename>_printable.pdf" where <filename> is the sole
     command-line argument. When you actually print the output file, please select
     'US letter' paper size due to margin errors on some printers.''',
        epilog='''by Mateusz Bysiek''',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'filename', metavar='<filename-without-extension>', type=str,
        help='''source filename wihtout .pdf extension - for example, if source file
     is "slides.pdf", the argument here should be "slides"''')

    args = parser.parse_args(args)

    make_printable_slides(args.filename)


def make_printable_slides(filename: str):
    """Generate printable slides (4 slides on one page) from a PDF."""

    output_prefix = filename + '_print'
    output = output_prefix + '.tex'

    with open(output, 'w') as tex_file:
        tex_file.write(r'''\documentclass[a4paper]{article}

\usepackage{pdfpages}

\begin{document}

\includepdf[nup=2x2,pages=-,delta=5mm 5mm,frame=true,landscape]{''' + filename + r'''.pdf}

\end{document}
''')

    subprocess.run(['pdflatex', output], check=True)
    subprocess.run(['mv', output_prefix + '.pdf', output_prefix + 'able.pdf'], check=True)
    subprocess.run(['rm', output_prefix + '.aux', output_prefix + '.log', output_prefix + '.tex'],
                   check=True)


if __name__ == '__main__':
    main()
