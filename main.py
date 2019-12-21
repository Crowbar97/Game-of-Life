from time import sleep
from game import Biome

biome = Biome(20, 80, 500)
# biome.make_pattern("penta", 3, 2)
while(True):
    biome.print_field()
    sleep(0.1)
    biome.next()

