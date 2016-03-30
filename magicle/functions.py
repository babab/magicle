# Copyright (c) 2016 Benjamin Althues <benjamin@babab.nl>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import collections
import datetime
import textwrap


class MagicleFunctions:
    '''Function (base) object, all methods in here are magicle functions'''

    functions = (
        ('bumpCopyrightYear', {
            'regexp': r'Copyright\s+\D*\d{4,4}-?\d*\s*\w+',
        }),
        ('reStructuredTextHeader', {
            'regexp': r'^::h[1-6]+\s\w+',
            'settings': {
                'order': ['#', '*', '=', '-', '^', '"'],
                'overlined_order': [True, True, False, False, False, False],
            },
        }),
        ('textwrap', {
            'regexp': r'^\s*\W*\s*\w+',
            'settings': {
                'width': 78,
            },
        }),
    )
    '''Magicle functions mapping'''

    def __init__(self):
        '''Initialize functions and transform it to an OrderedDict'''
        self.functions = collections.OrderedDict(self.functions)

    def bumpCopyrightYear(self, line):
        '''Bump copyright year'''
        curr_year = str(datetime.datetime.now().year)
        prev_year = str(int(curr_year) - 1)

        if curr_year in line:
            # copyright is already up to date
            return line

        if '-' + prev_year in line:
            return line.replace(prev_year, curr_year)
        elif prev_year in line:
            return line.replace(
                prev_year, '{}-{}'.format(prev_year, curr_year)
            )
        return line

    def reStructuredTextHeader(self, line):
        '''Create reStructuredText header'''
        level = int(line.split(' ')[0][3])
        text = ' '.join(line.split(' ')[1:])

        try:
            settings = self.functions['reStructuredTextHeader']['settings']
            overlined = settings['overlined_order'][level - 1]
            decoration = settings['order'][level - 1] * len(text)
        except (TypeError, IndexError):
            return line

        if level:
            if overlined:
                return '{d}\n{t}\n{d}'.format(t=text, d=decoration)
            return '{t}\n{d}'.format(t=text, d=decoration)
        return line

    def textwrap(self, line):
        '''Wrap text to a maximum line width'''
        commentchr = ''
        startchars = line.lstrip()[:2]

        try:
            settings = self.functions['textwrap']['settings']
            width = settings['width']
        except (TypeError, IndexError):
            return line

        if startchars in ('# ', '* ', '//', '" '):
            if startchars == '* ':
                commentchr = ' * '
                width -= 3
            elif startchars == '//':
                commentchr = '// '
                width -= 3
            else:
                commentchr = startchars
                width -= 2

        return '\n{}'.format(commentchr).join(textwrap.wrap(line, width=width))
