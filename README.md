# 6040electoral
Sistema elettorale che dà il 60% dei seggi con metodo maggioritario e il 40% con il metodo dei più alti resti. La simulazione del software avviene con 40 seggi: 24 maggioritari e 16 proporzionali.

## Funzionamento del sistema
In ogni collegio uninominale:
* Il primo arrivato ottiene il seggio
* Il secondo arrivato mette i propri voti nella quota proporzionale
* Il terzo arrivato vede i propri voti dispersi

## Partiti 
Per simulare un sistema tripolare sono presenti tre partiti:
* Partito Popolare
* Partito Socialista
* Partito Democristiano

La loro forza elettorale è data da un coefficiente, che indica i limiti nella generazione dei voti per collegio. I coefficienti sono:
* PP: 100,400
* PS: 100,333
* PD: 50, 250

## Funzionalità
Il software calcola:
* Il numero dei seggi uninominali
* Il totale dei seggi
* I numeri di voti
* Approssimativamente, il totale di voti nel proporzionale puro
