from nltk.corpus import machado, mac_morpho, floresta, genesis
from nltk.text import Text
from nltk.probability import FreqDist
from nltk.util import bigrams
from nltk.misc import babelize_shell

print("*** Exemplos introdutórios do livro NLTK em Português ***")
print("Carregando ptext1...ptext4 e psent1...ptext4")
print("Use 'texts()' ou 'sents()' para listar os materiais de texto ou sentença.")

ptext1 = Text(machado.words('romance/marm05.txt'), name="Memórias Póstumas de Brás Cubas (1881)")
ptext2 = Text(machado.words('romance/marm08.txt'), name="Dom Casmurro (1899)")
ptext3 = Text(genesis.words('portuguese.txt'), name="Gênesis")
ptext4 = Text(mac_morpho.words('mu94se01.txt'), name="Folha de Sao Paulo (1994)")

def texts():
    print("ptext1:", ptext1.name)
    print("ptext2:", ptext2.name)
    print("ptext3:", ptext3.name)
    print("ptext4:", ptext4.name)

psent1 = "o amor da glória era a coisa mais verdadeiramente humana que há no homem , e , conseqüentemente , a sua mais genuína feição .".split()
psent2 = "Não consultes dicionários .".split()
psent3 = "No princípio, criou Deus os céus e a terra.".split()
psent4 = "A Cáritas acredita que outros cubanos devem chegar ao Brasil .".split()

def sents():
    print("psent1:", " ".join(psent1))
    print("psent2:", " ".join(psent2))
    print("psent3:", " ".join(psent3))
    print("psent4:", " ".join(psent4))