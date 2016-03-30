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
import re
import sys

import pycommand

from magicle import functions

__docformat__ = 'restructuredtext'
__author__ = "Benjamin Althues"
__copyright__ = "Copyright (C) 2016  Benjamin Althues"
__version_info__ = (0, 1, 0, 'final', 0)
__version__ = '0.1.0'
versionStr = 'Magicle ' + __version__


class MagicleInterface:
    '''Interface methods'''

    def __init__(self, functions):
        '''Initialize functions'''
        self.functions = functions

    def match(self, line):
        '''match line with functions and return matches'''
        matches = collections.OrderedDict()
        for action, settings in self.functions.functions.items():
            result = re.search(settings['regexp'], line)
            if result:
                function = getattr(self.functions, action)
                matches.update({function.__doc__: function(line)})
        return matches

    def rewrite(self, lines):
        '''Rewrite input lines to output lines'''
        output_lines = []
        for line in lines:
            matches = self.match(line.rstrip('\n'))
            if matches:
                for k, v in matches.items():
                    output_lines.append(v)
                    break
            else:
                output_lines.append(line.rstrip('\n'))
        return output_lines


class Command(pycommand.CommandBase):
    '''Magicle shell command handler, based on pycommand'''

    usagestr = 'usage: echo "somestring" | magicle [options]'
    description = 'Magicle {}'.format(__version__)
    optionList = (
        ('help', ('h', False, 'show this help information')),
    )

    def run(self):
        if self.flags.help:
            print(self.usage)
            return 0

        magicle = MagicleInterface(functions.MagicleFunctions())
        lines = magicle.rewrite(sys.stdin)
        for line in lines:
            print(line)
        return 0

if __name__ == '__main__':
    pycommand.run_and_exit(Command)
