class MyString:
    
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self.value.endswith(".")
    
    def is_question(self):
        return self.value.endswith("?")
    
    def is_exclamation(self):
        return self.value.endswith("!")
    
    def count_sentences(self):
        exclamations_removed = self.value.replace("!", ".")
        questions_and_exclamations_removed = exclamations_removed.replace("?", ".")
        sentence_list = questions_and_exclamations_removed.split(".")
        while "" in sentence_list:
            sentence_list.remove("")
        return len(sentence_list)