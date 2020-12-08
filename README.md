# SimpleParserSugestPython
An 3 hour application that parse an input of a simple CFG of english with auto completion

this is the CFG
S -> NOUN_PHRASE VERB_PHRASE DOT S
S -> lambda 
VERB_PHRASE -> <singular_verb> <adverb>
NOUN_PHRASE -> <adjective> NOUN_PHRASE2
NOUN_PHRASE2 -> NOUN_PHRASE 
NOUN_PHRASE2 -> <singular_noun>
DOT -> .
