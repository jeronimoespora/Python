import pandas as pd

import requests

datos_covid = requests.get("http://api.covid19api.com/summary").json()

covid19 = pd.DataFrame.from_dict(datos_covid["Countries"])

print(covid19["Country"])
