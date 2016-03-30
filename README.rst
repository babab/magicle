#######
Magicle
#######

Magicle is the Magic Line Editor and it is here to provide in a somewhat
magical approach of editing text (in your favorite text-editor).

You can automatically edit certain lines based on context. The editing actions
are defined in *functions* and the action to perform is selected by matching
with a prioritized list of *regexp* rules, one for each function. Magicle can
perform various tasks, but is only executed with a single (key)command.

**Press Enter to edit**

Because you can easily define your own rules and functions (in any programming
language (coming soon)), magicle allows you to do many cool things, like:

- Running any of the default build-in tasks:
   * Bumping the year in copyright headers
   * Create reStructuredText headers
   * Wrap lines to a miximum length
- Creating powerful macros
- Creating templates
- Creating snippets

*******
Roadmap
*******

Magicle is in very early stages of development right now.
These are the things that most probably will be added soon.

Initial release:

- Add documentation
- Add more build-in functions

Later releases:

- Add a "plugin" system where a Magicle function can be defined as any
  (prefixed) executable (script) in the PATH as long as it can return exit
  codes. This allows for a user to extend the functions list very comfortably.
- Add a configfile to define the functions regexp match list


*******
License
*******

Magicle is released under an ISC license, which is functionally
equivalent to the simplified BSD and MIT/Expat licenses, with language
that was deemed unnecessary by the Berne convention removed.

::

   Copyright (c) 2016  Benjamin Althues <benjamin@althu.es>

   Permission to use, copy, modify, and distribute this software for any
   purpose with or without fee is hereby granted, provided that the above
   copyright notice and this permission notice appear in all copies.

   THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
   WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
   MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
   ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
   WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
   ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
   OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

This file has been edited with Magicle.
