import pandas as pd

data = {
    "Biler": [
        "BMW",
        "Ford",
        "Toyota",
        "Tesla",
        "Audi",
        "Mercedes",
        "Volkswagen",
        "Honda",
        "Volvo",
    ],
    "Pris": [
        500000,
        450000,
        390000,
        600000,
        700000,
        670000,
        385000,
        350000,
        550000,
    ],
}

df = pd.DataFrame(data)
snitt = df["Pris"].mean()
print(f"Snittprisen for bilene er: {snitt:.2f}")
tall = f"{snitt:,.0f}".replace(",", " ")
print(f"Snittprisen på bilene er: {tall} kr.")
