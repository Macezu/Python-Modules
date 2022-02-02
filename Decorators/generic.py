from functools import wraps

def tee_kolmen_kolmio():
    tahti = ""
    for i in range(3):
        tahti += "*"
        print(tahti)
        
tee_kolmen_kolmio()
print("")

def tee_vapaavalintainen_kolmio(korkeus : int):
    tahti = ""
    for i in range(korkeus):
        tahti += "*"
        print(tahti)
        
        
tee_vapaavalintainen_kolmio(6)
print("")

def tee_vapaa_kolmio_omilla_symbolilla(korkeus : int, symboli : str = "*"):
    for i in range(korkeus):
        print(symboli)
        symboli += symboli[0]

tee_vapaa_kolmio_omilla_symbolilla(5,"$")
print("")



def koriste_funktio(original_function):
    #args ja kwargs sallivat datan läpiliikkumisen
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        print("\nTämän koristefunktion tulostus on ennen alkuperäistä funktiota: {}".format(original_function.__name__))
        print(f"Olen tietoinen alkuperäisistä argumenteistä: {args}")
        for arg in args:
            if isinstance(arg,str):
                print("Argumenteissä oli tekstiä")
        return original_function(*args, **kwargs)
    return wrapper_function


@koriste_funktio
def koristeltu_vapaa_kolmio_omilla_symbolilla(korkeus : int, symboli : str = "*"):
    for i in range(korkeus):
        print(symboli)
        symboli += symboli[0]
        
koristeltu_vapaa_kolmio_omilla_symbolilla(4,"€")