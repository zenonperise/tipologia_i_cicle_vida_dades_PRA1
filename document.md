# Pràctica 1 de Tipologia i cicle de vida de les dades

## Context

Els medis de comunicació tenen una gran importància a la societat actual. L'anomenat "quart poder" té la capacitat de, a part d'informar sobre l'actuaiitat,
de formar, canviar i manipular l'opinió pública.

Per aquest motiu hem plantejat la possibilitat de fer un estudi sobre les noticies publicades durant un periode de temps per tal de veure quins esdeveniments o
personatges han tingut una certa rellevància durant un temps en el passat.

Com a font de dades hem escollit la web <https://www.meneame.net>. Aquesta web és un agregador de noticies, és a dir, recull noticies d'altres medis.
La particularitat d'aquesta pàgina és que la decisió sobre quines noticies apareixen a portada és pressa per la comunitat de la pàgina gracies a un sistema de votacions.
Per tant, les notícies que apareixen en portada tenen una certa rellevància social o interes per la major part d'usuaris.

## Títol del dataset

## Descripció

El dataset recull les noticies que han arribat a la portada de Meneame.

Com que la pàgina de Meneame és un agregador de noticies, el primer camp que trobem mostra la URL a la noticia propiament dita, és a dir, és un enllac a una altra web, ja sigui la versió digital d'un diari o un blog o qualsevol altre tipus de pàgina. A continuació trobem els dos camps principals de la noticia, que contenen la noticia pròpiament dita. Aquests són el títol i el resum de la noticia. Es tracta d'un text escrit normalment en castellà.

Per tal de posar les noticies en context temporal disposem de dues dates que enregistra Meneame. Aquestes són, per un costat, la data i hora en la que la noticia ha estat enregistrada a la pàgina. És a dir, el dia i hora en el que un usuari ha decidit que una determinada noticia d'un medi extern pot ser rellevant per a la comunitat i l'ha enregistrar a Meneame. Aquesta és la data d'enviament. Després de cert temps, la comunitat ha pogut veure aquesta noticia i ha pogut votar si és rellevant o no. L'algorisme de Meneame decideix a partir d'aquests vots si la noticia és rellevant i per tant, apareix en portada. Aquesta és la data de publicació i és la segona data que enregistrem.

Tal com hem dit, la decisió de publicació es pren en funció de les votacions que ha rebut una noticia determinada. Per tal de poder ponderar el pes d'una noticia determinada el nostre dataset també conté el número de vots que ha obtingut.

Per últim, no totes les noticies que s'envien a Meneame són d'actualitat propiament dites. També apareixen altres tipus com articles culturals o històrics. Per tal de diferenciar les noticies d'actualitat d'altre tipus de textos disposem d'una categoria, que és assignada per l'usuari que envia la noticia.

## Representació Grafica

## Contingut

- Pagina
- Titol
- Resum
- URL
- Vots
- Data Enviament
- Data Publicació
- Categoria

## Agraiments

La pàgina Meneame.net és un agregador de noticies en castellà creat al 2005 per Ricardo Galli, un professor de la Universitat de les Illes Balears (UIB). Meneame ofereix la possibilitat d'enviar noticies d'altres medis, votar-les i comentar-les. Les noticies s'ordenen segons la seva popularitat, mesurada a partir dels vots i número de comentaris. Les més populars apareixen a la portada de Meneame.

Anteriorment s'han utilititzat medis digitals per a fer un estudi sobre els titulars de noticies, majorment en llengua anglesa. També s'ha utilitzar Meneame per a extreure altres tipus d'informació. A continuació veiem els links:

### Analisis anteriors - Noticies de medis digitals

- <https://towardsdatascience.com/headlines-articles-analysis-and-nlp-4013a66dbac>
- <https://towardsdatascience.com/analyzing-cnets-headlines-3f350bb97cd4>
- <https://www.kaggle.com/therohk/million-headlines>
- <https://www.kaggle.com/richel145/analysis-of-a-million-news-headlines>

### Analisis anteriors - Meneame

- <https://www.kaggle.com/mrverde/meneamenet-front-page-news>
- <https://www.researchgate.net/figure/Scatter-plot-of-days-in-the-dataset-of-Meneame-2011-2015-Each-day-is-represented-by-a_fig2_318914420>
- <https://zenodo.org/record/2536218>
- <https://zenodo.org/record/4122059>

## Inspiració

Aquest dataset vol mostrar quins conceptes o personatges han tingut rellevància durant certs periodes de temps tenint en compte les noticies publicades a la prensa. Aquestes noticies, al estar publicades a Meneame, ja han passat un filtre de rellevància per part de la seva comunitat. Per tant, amb Meneame disposem d'una font de noticies rellevants ordenades cronologicament. Això ens permet fer diferents estudis

- Esdeveniments / Personatges / Conceptes
  - populars o més freqüents en un determinat interval de temps
  - ponderant amb el pes en vots
- Clustering de noticies que parlem de temes similars
- Classificació de noticies futures
- Estudi de paraules que apareixen associades. Per exemple (Pedro + Sanchez)
- Veure si esdeveniments que han ocorregut es reflexen a les noticies. Per exemple, Brexit.

## Preguntes a respondre

- Quina és la diferència entre la Descripció i el contingut?
- Cal fer les respostes punt a punt o en un text tot seguit? Hi han temes i conceptes que es repeteixen a diferents punts.
