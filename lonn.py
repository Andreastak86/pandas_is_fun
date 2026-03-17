import pandas as pd

df = pd.read_csv("ansatte.csv")


def f(n):
    return f"{n:,.0f}".replace(",", " ")


median_v = f(df["Lønn"].median())
snitt_v = f(df["Lønn"].mean())
min_v = f(df["Lønn"].min())
max_v = f(df["Lønn"].max())

tabell_html = df.to_html(
    index=False, classes="dataframe", border=0, formatters={"Lønn": f}
)

html_output = f"""<!doctype html>
<html lang="no">
<head>
    <meta charset="UTF-8" />
    <title>Lønnsrapport</title>
    <link rel="stylesheet" href="styles.css" />
</head>
<body>
    <div class="summary-box">
        <h1>AndyCorp AS</h1>
        <div class="stats-grid">
            <p><b>Medianlønn</b> <span>{median_v} kr</span></p>
            <p><b>Snittlønn</b> <span>{snitt_v} kr</span></p>
            <p><b>Laveste lønn</b> <span>{min_v} kr</span></p>
            <p><b>Høyeste lønn</b> <span>{max_v} kr</span></p>
        </div>
    </div>

    <div id="table-container">
        {tabell_html}
    </div>
</body>
</html>"""

with open("ansatte.html", "w", encoding="utf-8") as f_out:
    f_out.write(html_output)
