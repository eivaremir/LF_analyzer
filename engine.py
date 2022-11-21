from lexic_tokens import TOKENS
from lexic_tokens import PRODUCTION_RULES
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

def syntax(sentence):
    l = lexic(sentence)
    lexems = [x["lexem"] for x in l]
    _in = "".join(lexems)
    result = False
    for lang in ["ENGLISH"]:#,"SPANISH","PORTUGUESE"]:
        _out = _in
        print(lang,"Processing"," ".join([x["token"] for x in l]),"\n\t"+_out)

        for c in PRODUCTION_RULES[lang]["CIRCUNSTANCE"]:
            _out =_out.replace(c,"CIRCUNSTANCE")
            print(f"\t{_out}")
            for m in PRODUCTION_RULES[lang]["MODIFIER"]:
                _out =_out.replace(m,"MODIFIER")
                print(f"\t{_out}")
                predicate_yet_in_phrase = True
                
                for p in PRODUCTION_RULES[lang]["PREDICATE"]:
                    _out =_out.replace(p,"PREDICATE")        
                    print(f"\t{_out}")
                
                for s in PRODUCTION_RULES[lang]["SUBJECT"]:
                    _out =_out.replace(s,"SUBJECT")
                    print(f"\t{_out}")

                predicate_yet_in_phrase = True
                while predicate_yet_in_phrase:
                    _out =_out.replace("PREDICATE","",1)
                    print(f"\t{_out}")
                    predicate_yet_in_phrase = len([x for x in _out.split("PREDICATE") if x ==""]) > 1
                
                for s in PRODUCTION_RULES[lang]["SENTENCE"]:
                    _out =_out.replace(s,"SENTENCE")
                    print(f"\t{_out}")
        if _out == "SENTENCE" : 
            result = True
            break
    return {
        "result":result,
        "language":lang

    }
    