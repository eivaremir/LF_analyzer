from lexic_tokens import TOKENS
def lexic(sentence):
    tokens = [ x.casefold() for x in sentence.split(" ")]
    analysis_array = list()
    for token in tokens:
        for language in TOKENS:
            for lexem,language_tokens in TOKENS[language].items():
                #print(token,lexem,language_tokens)
                if token in [ x.casefold() for x in language_tokens]:
                    print(token,"is",lexem)
                    analysis_array.append({
                        "token":token,
                        "lang":language,
                        "lexem":lexem
                    })
                    break
            

    return analysis_array