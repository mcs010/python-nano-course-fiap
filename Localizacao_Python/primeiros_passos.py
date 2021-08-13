from pygeocoder import Geocoder

endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'

print(Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco).coordinates) #Api endpoint