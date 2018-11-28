# Flappy Bird Q-Learning Bot

Dit was een schoolproject die ik in **juni 2018** heb gedaan.

## Systeemvereisten
U dient Python en pip (package manager) te hebben geïnstalleerd op uw computer.

## Demo van de getrainde bot
U dient dit project te clonen of te downloaden en vervolgens het volgende te doen:

1. Voer `pip install -r requirements.txt` uit om de dependencies te installeren
2. Voer `python flappy.py` uit om het programma te starten

## Demo van het leerproces
U dient dit project te clonen of te downloaden en vervolgens het volgende te doen:

1. Verwijder/hernoem het bestand `/assets/q_values.json`
2. Voer `python flappy.py` uit

Om het leerproces te versnellen kunt u de waarde `FPS = 30` op lijn 13 van `flappy.py` verhogen naar een hoger getal.

## Doel
In dit project heb ik een Machine Learning algoritme (Q-Learning) geïmplementeerd voor het populaire spel Flappy Bird. Het doel was om de computer in staat te stellen het spel zelf te leren spelen, zonder specifieke instructies te geven.

## Ontwikkelomgeving
Python

## Omschrijving
Het doel van het spelen van Flappy Bird is het behalen van zoveel mogelijk punten door middel van het passeren van zoveel mogelijk openingen tussen de twee buizen. Hierbij kan de spelen de spatietoets indrukken om het vogeltje omhoog te laten vliegen óf niets doen om het vogeltje naar beneden te laten vallen.

In het bestand FlappyBot.py staat de code van de geïmplementeerde Machine Learning algoritme. In grote lijnen werkt het als volgt:

1. De computer weet initieel helemaal niets over het spel, behalve dat hij twee acties kan uitvoeren; vliegen (actie 1) óf niets doen (actie 2)
2. Bij iedere frame van het spel krijgt de computer de huidige toestand van het spel bestaande uit:
  - de horizontale afstand tussen het vogeltje en de opening
  - de verticale afstand tussen het vogeltje en de opening
  - de mate waarin het vogeltje naar boven of naar beneden gaat
3. Indien de computer zich eerder in dezelfde toestand heeft begeven -en dus een ervaring heeft opgebouwd op basis van zijn actie- weet hij welke van de twee acties in deze specifieke toestand het beste resultaat oplevert. Hij zal dan ook naargelang deze ervaring handelen. Echter, wanneer hij deze specifieke toestand niet eerder heeft ervaren doet hij niets (actie 2) en gaat later evalueren of dit positief of negatief uitpakt.
4. Na ieder spel evalueert de computer welke acties hebben geleid tot de beëindiging van het spel en leert op basis hiervan dat deze acties in de gegeven toestanden niet goed zijn om uit te voeren.
5. De ervaringen die de computer opdoet slaat hij op in het bestand /assets/q_values.json
6. Hierna begint hij een nieuw spel met de extra ervaring die hij heeft opgedaan in het vorige spel.

## Screenshot
![alt text](https://user-images.githubusercontent.com/18209782/49144186-050a2a00-f2fd-11e8-8b0e-03abb5a183b4.jpg "De computer is een potje Flappy Bird aan het spelen")
###### De computer is een potje Flappy Bird aan het spelen
