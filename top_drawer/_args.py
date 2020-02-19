from precept import Argument

from top_drawer import _thesaurus

WORD = Argument(
    'word',
    help='The word to search.'
)
CASING = Argument(
    '-c', '--casing',
    choices=['snakecase', 'spinalcase'],
    default='spinalcase',
    help='The casing to apply to synonyms.'
)
PYPI = Argument(
    '--pypi',
    help='Disable validation on pypi',
    action='store_false'
)
NPM = Argument(
    '--npm',
    help='Disable validation on npm',
    action='store_false'
)
FULL = Argument(
    '-f', '--full',
    help='Include the invalids in the output',
    action='store_true'
)
ANTONYMS = Argument(
    '--antonyms',
    action='store_true',
    help='Include antonyms in the output.'
)
USR = Argument(
    '--usr',
    action='store_true',
    help='Include `usr` results in the output.'
)
WORD_TYPE = Argument(
    '--word-type',
    choices=_thesaurus.WORD_TYPES,
    default=_thesaurus.ALL,
    help='Type of words to use, `all` for every types.'
)
