import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

df_regions = pd.read_csv("../dati-regioni/dpc-covid19-ita-regioni.csv")
regioni = ["Toscana", "Veneto", "Friuli Venezia Giulia","Lombardia"]
colori = ["red","blue","green","red"]
toplot = "nuovi_positivi"


for i, regione in enumerate(regioni):
	fig, ax = subplots()
	a = df_regions.loc[df_regions['denominazione_regione'] == regione]
	a.plot(kind='line',x='data',y=toplot,color=colori[i], ax=ax)
	ax.legend([toplot + " " +regione]);



df_nazionale = pd.read_csv("../dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")
plot_nazionale = "nuovi_positivi"
df_nazionale["nuovi_deceduti"] =  df_nazionale["deceduti"] -df_nazionale["deceduti"].shift(1)
df_nazionale["nuovi_dimessi_guariti"] =  df_nazionale["dimessi_guariti"] -df_nazionale["dimessi_guariti"].shift(1)
df_nazionale["nuovi_positivi2"] = df_nazionale["totale_positivi"] -df_nazionale["totale_positivi"].shift(1)
df_nazionale["nuovi_tamponi"] =  df_nazionale["tamponi"] -df_nazionale["tamponi"].shift(1)
df_nazionale["ratio"] =  df_nazionale["nuovi_positivi"]/df_nazionale["nuovi_tamponi"]*100

fig, ax = subplots()
df_nazionale.plot(kind='line',x='data',y=plot_nazionale,color="blue", ax=ax)
ax.legend([plot_nazionale + "_nazionale"]);

plot_nazionale2 = "nuovi_deceduti"
fig, ax = subplots()
df_nazionale.plot(kind='line',x='data',y=plot_nazionale2,color="blue", ax=ax)
ax.legend([plot_nazionale2 + "_nazionale"]);

plot_nazionale3 = "nuovi_dimessi_guariti"
fig, ax = subplots()
df_nazionale.plot(kind='line',x='data',y=plot_nazionale3,color="blue", ax=ax)
ax.legend([plot_nazionale3 + "_nazionale"]);

plot_nazionale3 = "variazione_totale_positivi"
fig, ax = subplots()
df_nazionale.plot(kind='line',x='data',y=plot_nazionale3,color="blue", ax=ax)
ax.legend([plot_nazionale3 + "_nazionale"]);

plot_nazionale3 = "ratio"
fig, ax = subplots()
df_nazionale.plot(kind='line',x='data',y=plot_nazionale3,color="blue", ax=ax)
ax.legend([plot_nazionale3 + "_nazionale"]);


plt.show()
