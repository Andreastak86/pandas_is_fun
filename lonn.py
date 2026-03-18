import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ansatte.csv")


def f(n):
    return f"{n:,.0f}".replace(",", " ")


median_v = f(df["Lønn"].median())
snitt_v = f(df["Lønn"].mean())
min_v = f(df["Lønn"].min())
max_v = f(df["Lønn"].max())

stilling_stats = df.groupby("Stilling")["Lønn"].mean().reset_index()
stilling_stats.columns = ["Stilling", "Snittlønn"]

plt.style.use("dark_background")
plt.figure(figsize=(10, 6))
plt.bar(stilling_stats["Stilling"], stilling_stats["Snittlønn"], color="#007bff")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Kroner")
plt.title("Snittlønn per stillingstype")
plt.tight_layout()
plt.savefig("stats_plot.png")

stilling_stats_html = stilling_stats.to_html(
    index=False,
    classes="dataframe",
    border=0,
    formatters={"Snittlønn": f},
    table_id="stats-table",
)
tabell_html = df.to_html(
    index=False,
    classes="dataframe",
    border=0,
    formatters={"Lønn": f},
    table_id="main-table",
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
        <section class="table-section">
            <h2>Lønnsfordeling (Graf)</h2>
            <img src="stats_plot.png" alt="Lønnsgraf" style="max-width:100%; border-radius:12px; margin-bottom:30px;">
        </section>

        <section class="table-section">
            <h2>Snittlønn per stilling</h2>
            {stilling_stats_html}
        </section>
        
        <section class="table-section">
            <h2>Fullstendig oversikt</h2>
            {tabell_html}
        </section>
    </div>

    <script src="script.js"></script>
</body>
</html>"""

with open("ansatte.html", "w", encoding="utf-8") as f_out:
    f_out.write(html_output)

print("Suksess! Rapporten er nå komplett med graf.")
