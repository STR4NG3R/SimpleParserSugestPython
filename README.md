# SimpleParserSugestPython
An 3 hour application that parse an input of a simple CFG of english with auto completion

this is the CFG  <br>
S -> NOUN_PHRASE VERB_PHRASE DOT S <br>
S -> lambda <br>
VERB_PHRASE -> singular_verb adverb <br>
NOUN_PHRASE -> adjective NOUN_PHRASE2 <br>
NOUN_PHRASE2 -> NOUN_PHRASE <br>
NOUN_PHRASE2 -> singular_noun <br>
DOT -> . <br>
