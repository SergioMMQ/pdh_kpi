import requests
import pandas as pd

# API URL y headers
url = "https://api.tinybird.co/v0/pipes/api_Users.json?vApiKey=b8d73514bc987a84"
headers = {
    "accept": "application/json",
    "authorization": "Bearer p.eyJ1IjogIjYwNGM4YTQ3LWEzZTItNDYxMy1hMTNmLWIyNmQwMmFkNDNjMiIsICJpZCI6ICJkMmJmMTc3YS01ZGVlLTRmNzMtYjVhMS1kOTA3OGQ2NDllY2QiLCAiaG9zdCI6ICJldV9zaGFyZWQifQ.8832SA1_zlD2TMz9f_MKeheNqKTIJcVDiqkJH1xThCw"
}

# Obtener datos
response = requests.get(url, headers=headers)
data = response.json()
df = pd.DataFrame(data['data'])

# ------------------------- Filtro 1 -------------------------
# app_delihealths_telemedicina.xlsx
filtro1 = df[
    (df['company_group_code'] == 'PdH') &
    (df['usertype'] == 'primary') &
    (df['first_accessed_at_utc'] != "")
]
filtro1.to_excel("app_delihealths_telemedicina.xlsx", index=False)
print(f"Filtro 1: {len(filtro1)} registros guardados en 'app_delihealths_telemedicina.xlsx'")

# ------------------------- Filtro 2 -------------------------
# Usabilidad App Delihealths.xlsx
filtro4 = df[
    (df['company_group_code'] == 'PdH') &
    (df['usertype'] == 'primary') &
    (df['first_accessed_at_utc'] != "") &
    (df['has_consultation'] == "1")
]
filtro4.to_excel("Usabilidad App Delihealths.xlsx", index=False)
print(f"Filtro 4: {len(filtro4)} registros guardados en 'Usabilidad App Delihealths.xlsx'")

# ------------------------- Filtro 3 -------------------------
# app_delihealths_telemedicina_familiares.xlsx
filtro3 = df[
    (df['company_group_code'] == 'PdH') &
    (df['usertype'] == 'secondary')
]
filtro3.to_excel("app_delihealths_telemedicina_familiares.xlsx", index=False)
print(f"Filtro 3: {len(filtro3)} registros guardados en 'app_delihealths_telemedicina_familiares.xlsx'")


# ------------------------- Filtro 4 -------------------------
# usabilidad_app_delihealths_familiares.xlsx
filtro2 = df[
    (df['company_group_code'] == 'PdH') &
    (df['usertype'] == 'secondary') &
    (df['has_consultation'] == "1")
]
filtro2.to_excel("usabilidad_app_delihealths_familiares.xlsx", index=False)
print(f"Filtro 2: {len(filtro2)} registros guardados en 'usabilidad_app_delihealths_familiares.xlsx'")

