class Language:
    def say_hello(self):
        raise NotImplementedError("Please use say_hello class in child class")

class French(Language):
    def say_hello(self):
        print("Bonjour")

class Chinese(Language):
    def say_hello(self):
        print("Ni hao")

class Finnish(Language):
    pass

def intro(lang):
    lang.say_hello()

joshua = French()
john = Chinese()
mikko = Finnish()

intro(joshua)
intro(john)
intro(mikko)