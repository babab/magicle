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

from nose.tools import eq_

from magicle import magicle, functions


def test_base_functions():
    '''core: Check if base functions are found in functions'''
    a = functions.MagicleFunctions()
    assert 'bumpCopyrightYear' in a.functions.keys()
    assert 'reStructuredTextHeader' in a.functions.keys()
    assert 'textwrap' in a.functions.keys()


def test_interface_match():
    '''core: Check if match function can match base functions correctly'''
    a = magicle.MagicleInterface(functions.MagicleFunctions())
    matches = a.match('Copyright (C) 2016 Name').keys()
    assert 'Bump copyright year' in matches
    assert 'Wrap text to a maximum line width' in matches

    matches = a.match('::h1 rst header').keys()
    assert 'Create reStructuredText header' in matches
    assert 'Wrap text to a maximum line width' in matches


def test_function_bumpCopyrightYear():
    '''bumpCopyrightYear: expands last year correctly'''
    a = magicle.MagicleInterface(functions.MagicleFunctions())
    lines = a.rewrite(['Copyright (c) 2015 Author Name'])
    eq_(lines[0], 'Copyright (c) 2015-2016 Author Name')


def test_function_reStructuredTextHeader():
    '''reStructuredTextHeader: expands headers correctly'''
    a = magicle.MagicleInterface(functions.MagicleFunctions())
    lines = a.rewrite(['::h3 header 1', '::h4 header2'])
    eq_(lines, ['header 1\n========', 'header2\n-------'])
