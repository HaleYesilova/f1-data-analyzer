from preswald import connect, get_df, query, table, text, slider, plotly
import plotly.express as px


text(" # Formula 1 Championship Data Analysis")
text("Exploring race history, top drivers, constructors, and circuits from 1950 to 2009 using Preswald's interactive UI and SQL-style data querying tools.")


connect()
results = get_df("results_csv")
drivers = get_df("drivers_csv")
constructors = get_df("constructors_csv")
races = get_df("races_csv")
circuits = get_df("circuits_csv")


text("## Top 10 Drivers by Race Wins")

sql = """
SELECT driverId, COUNT(*) AS wins
FROM results_csv
WHERE CAST(positionOrder AS INT) = 1
GROUP BY driverId
ORDER BY wins DESC
LIMIT 10
"""
driver_wins_df = query(sql, "results_csv")


text(f" Query returned {len(driver_wins_df)} rows.")
table(driver_wins_df, title="Debug: Raw SQL Query Output")


if not driver_wins_df.empty:
    driver_wins_df = driver_wins_df.merge(drivers, on="driverId", how="left")
    driver_wins_df["name"] = driver_wins_df["forename"] + " " + driver_wins_df["surname"]

    table(driver_wins_df[["name", "wins"]], title="Top 10 Drivers")

    threshold = slider("Minimum Wins", min_val=0, max_val=100, default=5)
    filtered_df = driver_wins_df[driver_wins_df["wins"] > threshold]

    text(f"### Drivers with more than {threshold} wins")
    if not filtered_df.empty:
        table(filtered_df[["name", "wins"]], title="Filtered Drivers by Wins")

        fig1 = px.bar(filtered_df, x="name", y="wins", title="Filtered Driver Wins")
        fig1.update_layout(template="plotly_white", xaxis_title="Driver", yaxis_title="Wins")
        plotly(fig1)
    else:
        text(" No drivers match this filter. Try lowering the slider.")
else:
    text(" Query returned no results. Check if `positionOrder` exists and has values.")


text("## Top 10 Constructors by Wins")

winners = results[results["positionOrder"].astype(str) == "1"]
constructor_wins = winners["constructorId"].value_counts().reset_index()
constructor_wins.columns = ["constructorId", "wins"]
top_constructors = constructor_wins.merge(constructors, on="constructorId", how="left").head(10)

table(top_constructors[["name", "wins"]], title="Top Constructors")

fig2 = px.bar(top_constructors, x="name", y="wins", title="Top 10 Constructors")
fig2.update_layout(template="plotly_white", xaxis_title="Constructor", yaxis_title="Wins")
plotly(fig2)


text("##  Most Frequent Race Circuits")

circuit_counts = races["circuitId"].value_counts().reset_index()
circuit_counts.columns = ["circuitId", "race_count"]
top_circuits = circuit_counts.merge(circuits, on="circuitId", how="left").head(10)

table(top_circuits[["name", "location", "country", "race_count"]], title="Most Frequent Circuits")

fig3 = px.bar(top_circuits, x="name", y="race_count", title="Top Circuits by Number of Races")
fig3.update_layout(template="plotly_white", xaxis_title="Circuit", yaxis_title="Races Held")
plotly(fig3)
