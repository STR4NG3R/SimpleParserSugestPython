
execution_stack = []

adjective = {
        "bald",
        "attractive",
        "beautiful",
        "chubby",
        "brave",
        "calm",
        "delightful",
        "ckumsy",
        "big",
        "fat",
        "gigantic",
        "great",
        "huge",
        "inmense",
        "large"
}

singular_verb = {
    "is",
    "does",
    "has",
    "can",
    "could",
    "may",
    "might",
    "must",
    "will",
    "should",
    "would"
}

singular_noun = {
    "bed",
    "sister",
    "bike",
    "dog",
    "computer",
    "room",
    "cat",
    "bird",
    "tv",
    "guitar"
}

adverb = {
    "daily",
    "happily",
    "usually",
    "potentially",
    "helpfully",
    "crossly",
    "poorly",
    "solemmly",
    "softly",
    "heavily",
    "quicker"
}


# S -> NOUN_PHRASE VERB_PHRASE DOT S
# S -> lambda 
# VERB_PHRASE -> <singular_verb> <adverb>
# NOUN_PHRASE -> <adjective> NOUN_PHRASE2
# NOUN_PHRASE2 -> NOUN_PHRASE 
# NOUN_PHRASE2 -> <singular_noun>
# DOT -> .

# S = 4
# NOUN_PHRASE = 1
# NOUN_PHRASE2 = 5
# VERB_PHRASE = 2
# DOT = 3
# <singular_verb> = 1000
# <adverb> = 1001
# <singular_noun> = 1003
# <adjective> = 1002
# . = 1004

reverse_sugestion_dict = {
        1000: singular_verb,
        1001: adverb,
        1002: adjective,
        1003: singular_noun,
        1004: {"."}
}

productions = {
        1 : [4 ,3, 2, 1],
        2: [],
        3: [1001, 1000],
        4: [5, 1002],
        5: [1],
        6: [1003],
        7: [1004],
}

predict_table = {
    # First
        (4, 1002) : 1,
        (1, 1002) : 4, 
        (2, 1000) : 3,
        (2, 1002) : 5,
        (3, 1004) : 7,
        (5, 1003) : 6,
        (5, 1002) : 5,
    # Follow
       (1, 1000) : 2,
       (2, 1004) : 2,
       (3, 1003) : 2,
       (3, 1002) : 2,
}


suggestions = {
        1: [1002],
        3: [1004],
        2: [1000],
        4: [1002],
        5: [1002, 1003, 1000]
}




def parser(tokens):
    print(tokens)
    global execution_stack
    execution_stack = [1003, 4]
    for token in tokens:
        while True:
            top = execution_stack.pop()
            if top < 1000: # non terminal symbol
                axis = (top, terminal(token.lower()))
                print(axis)
                if axis in predict_table:
                    row = predict_table[axis]
                    execution_stack += productions[row]
                    print(execution_stack)
                else:
                    print("Error de sintaxis")
            else: # terminal symbol
                if terminal(token.lower()) == top:
                    break
                else: 
                   print("Hubo un error con tu sintaxis") 
                   return
    if execution_stack[-1] == 1003:
        print("Felicidades sabes escribir :D")


def terminal(token):
    if token in adjective:
        return 1002
    if token in singular_verb:
        return 1000
    if token in singular_noun:
        return 1002
    if token in adverb:
        return 1001
    if token == "EOF":
        return 1003
    if token == ".":
        return 1004
    return 1005 # any other phrase


def getSugestions():
    print("Tu autocompletado")
    global execution_stack
    global suggestions
    top = execution_stack[-1]
    if top >= 1000:
        if top in reverse_sugestion_dict:
            target = reverse_sugestion_dict[top]
            for suggestion in target:
                print(suggestion)
    elif top in suggestions:
        targets = suggestions[top]
        for target in targets:
            for sug in reverse_sugestion_dict[target]:
                print(sug)


buffer_text = ""
while True:
    print(f'Texto en el "corta papeles":\n{buffer_text}')
    text = input(f"Ingresa tu oración aqui y presiona enter para el autocompletado\n-> {buffer_text}")
    if text == ":c":
        buffer_text = ""
    else: 
        buffer_text += text
    tokens =  buffer_text.split()
    parser(tokens)
    getSugestions()
