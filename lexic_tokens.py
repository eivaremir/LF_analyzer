TOKENS ={
    "ENGLISH": {
        "PREPOSITION":["To","From","With","In","Without"],
        "CONJUNCTION":["But","Otherwise","And","Or","Because","Well"],
        "GERUND_VERB":["Buying","Having","paying","Taking","is going to","are going to"],
        "INFINITIVE_VERB":["To buy","To have","TO Pay","TO Drink","to be"],
        "VERB":["buy","have","Pay","Drink","is","are"],
        "PARTICIPLE_VERB":["bought","Dyed","paid out","taken","been"],
        "NOUN":["Milk","Margarine","Cheese","Egg","Meat","Chicken","Rice","Beans","Noodles","Sugar","Onion","Tomatoes","Beer","Wine","money","cents"],
        "ADV":["morning","Now","After","Soon","Yet","Here","There","Much","Okay","Hardly","Bad","Almost","Usually","Never"],
        "ARTICLE":["The","A","Some"],
        "PRONOUN":["I","You","He","She","Us","You","they","it","we"],
        "ADJECTIVE":["great","pretty","small","afternoon","important","animated","large","narrow","bass","length","Okay","cold","warm","easy","bad","tall","strong","same","new"]

    },

    "SPANISH": {
        "PREPOSITION":["a","de","con","en","sin"],
        "CONJUNCTION":["pero","sino","y","o","porque","pues"],
        "VERB":["comprando","compramos","compraron","teniendo","pagando","tomando","comprar","tener","pagar","tomar","comprado","tenido","pagado","tomado","soy","eres","es","somos","son","estoy"",","estás","está","estamos","están"],
        "NOUN":["frijoles","leche","margarina","queso","huevo","carne","pollo","arroz","frijol","fideos","azúcar","cebolla","tomate","cerveza","cervezas","vino"],
        "ADJECTIVE":["estupendo","bonita","pequeña","tarde","importante","animado","amplio","angosto","bajo","largo","bueno","frío","cálido","fácil","malo","alto","fuerte","mismo","nuevo","buen","mal","buena"],
        "ADV":["algo","mañana","ahora","después","pronto","todavía","aquí","ahí","mucho","bueno","buen","mal","difícilmente","malo","casi","generalmente"],
        "ARTICLE":["el","la","los","las","un","una","uno","unos","unas"],
        "PRONOUN":["yo","tú","usted","él","ella","nosotros","nosotras","ustedes","ellos","ellas"],
        
    },

    "PORTUGUESE":{
        "PREPOSITION":["a","de","con","em","sem"],
        "CONJUNCTION":["mas","senão","e","ou","porque","pois"],
        "VERB":["comprando","tendo","pagando","pegando","comprar","ter","pagar","pegar","comprado","tido","pago","pegado","sou","é","somos","são","estou","está","estamos","estão"],
        "NOUN":["leite","margarina","queijo","ovo","carne","frango","arroz","feijões","macarrão","açúcar","cebola","tomates","cerveja","veio"],
        "ADV":["manhã","agora","depois","brevemente","ainda","aqui","lá","muito","ok","dificilmente","mau","quase","usualmente","nunca"],
        "ARTICLE":["o","a","os","as","um","uma","um","uns","umas"],
        "PRONOUN":["eu","você","ele","ela","nós","vocês","eles","elas"],
        "ADJECTIVE":["excelente","bonito","pequeña","tarde","importantes","importante","animado","ampla","estreito","Baixo","comprimento","Bom","frio","caloroso","fácil","mau","alta","Forte","mesmo","novo"],
    }
}

PRODUCTION_RULES = {
    "ENGLISH":{
        "SENTENCE" : ["SUBJECTPREDICATE","SUBJECT"],
        "SUBJECT" : ["PRONOUN"],
        "PREDICATE" : ["VERBNOUN","VERB","CIRCUNSTANCE","MODIFIER"],
        "MODIFIER" : ["CIRCUNSTANCE"],
        "CIRCUNSTANCE" : ["PREPOSITIONNOUN","CONJUNCTIONNOUN"]
    },
    "SPANISH":{
        "SENTENCE" : ["SUBJECTPREDICATE","SUBJECT"],
        "SUBJECT" : ["ARTICLENOUN","PRONOUN"],
        "PREDICATE" : ["VERBARTICLENOUNADJECTIVE","VERBARTICLEADJECTIVENOUN","VERBNOUN","VERBARTICLENOUN","VERBADJECTIVE","VERB","CIRCUNSTANCE","MODIFIER"],
        "MODIFIER" : ["CIRCUNSTANCE"],
        "CIRCUNSTANCE" : ["PREPOSITIONNOUN","CONJUNCTIONNOUN"]
    },
    "PORTUGUESE":{
        "SENTENCE" : ["SUBJECTPREDICATE","SUBJECT"],
        "SUBJECT" : ["ARTICLENOUN","PRONOUN"],
        "PREDICATE" : ["VERBARTICLENOUNADJECTIVE","VERBARTICLEADJECTIVENOUN","VERBNOUN","VERBARTICLENOUN","VERBADJECTIVE","VERB","CIRCUNSTANCE","MODIFIER"],
        "MODIFIER" : ["CIRCUNSTANCE"],
        "CIRCUNSTANCE" : ["PREPOSITIONNOUN","CONJUNCTIONNOUN"]
    }

}