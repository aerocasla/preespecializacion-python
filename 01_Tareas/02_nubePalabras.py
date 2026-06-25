##Install pip install wordcloud matplotlib in console

from wordcloud import WordCloud
import matplotlib.pyplot as plt

texto = """
python datos ciencia inteligencia artificial
python datos python codigo machine learning
visualizacion programacion python ciencia
datos analisis python ciencia datos
"""

nube = WordCloud(
    width=1000,
    height=500,
    background_color="white",
    colormap="viridis"
).generate(texto)

plt.figure(figsize=(10,5))
plt.imshow(nube, interpolation="bilinear")
plt.axis("off")
plt.show()