frases = [
    "Los lunes son los mejores dias para programar",
    "Python es moderno",
    "Veremos Inteligencia Artificial más adelante",
    "Lambda simplifica el código",
]

frases.sort(key=lambda f: len(f.split()), reverse=True)

print(frases)