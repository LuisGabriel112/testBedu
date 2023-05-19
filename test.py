import scipy.constants as const
import scipy.integrate as integrate

# Pedir al usuario los parámetros de la estrella
distancia = float(input("Ingrese la distancia a la estrella en años luz: "))
radio = float(input("Ingrese el radio de la estrella en unidades solares: "))
temperatura = float(input("Ingrese la temperatura de la estrella en Kelvin: "))

# Definir la función de Planck
def planck(wavelength):
    numerator = 2 * const.pi * const.h * const.c**2 / wavelength**5
    denominator = (const.h * const.c) / (wavelength * const.k * temperatura)
    return numerator / (np.exp(denominator) - 1)

# Calcular la luminosidad de la estrella mediante la integración numérica
luminosidad, error = integrate.quad(planck, 0, np.inf)

# Calcular la luminosidad total teniendo en cuenta la distancia
luminosidad_total = luminosidad * 4 * const.pi * radio**2 / (distancia * const.parsec)**2

# Mostrar el resultado
print(f"La luminosidad de la estrella es de {luminosidad_total:.2e} Watts.")
