class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, premise, conclusion):
        self.rules.append((premise, conclusion))

    def forward_chain(self):
        inferred = True
        while inferred:
            inferred = False
            for premise, conclusion in self.rules:
                if all(p in self.facts for p in premise) and conclusion not in self.facts:
                    self.facts.add(conclusion)
                    inferred = True

kb = KnowledgeBase()
kb.add_fact('rain')
kb.add_fact('sprinkler_on')
kb.add_rule(['rain'], 'wet_grass')
kb.add_rule(['sprinkler_on'], 'wet_grass')
kb.add_rule(['wet_grass'], 'slippery_ground')

kb.forward_chain()
print('wet_grass' in kb.facts)
print('slippery_ground' in kb.facts)
print('sunny' in kb.facts)
