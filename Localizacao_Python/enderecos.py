from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 sao paulo'

resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco) #Returns full address
print(resultado)

resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco).state #Returns only the state
print(resultado)

resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco).postal_code
print(resultado)

resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco).country
print(resultado)

resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco).coordinates
print(resultado)

resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWKw2yPMM').reverse_geocode(-23.570322, -46.6451267)
print(resultado)