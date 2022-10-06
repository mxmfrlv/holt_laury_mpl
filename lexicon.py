class Lexicon:
    def __init__(self,lang):
        self.lang=lang
    def get(self,phrase):
        res=phrase
        lphrase=phrase.lower().strip()
        if self.lang == "fr":
            if   lphrase == "your decision" : res = "Votre décision"
            elif lphrase == "with a probability of" : res = "avec une probabilité de"
            elif lphrase == "otherwise" : res = "sinon"
            elif lphrase == "results" : res = "Résultats"
        return res
