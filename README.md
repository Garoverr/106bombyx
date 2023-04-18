# Chaos Theory and Bombyx

## Français

   Dans les années 70, la théorie du chaos a ouvert la voie à une meilleure compréhension de l'évolution de certaines espèces animales. Les papillons, par exemple, ont été étudiés dans ce contexte. Nous allons nous intéresser au bombyx, qui est une espèce de papillon.

   Si une génération est surpeuplée, il est probable que la génération suivante le soit également, en fonction des règles naturelles de reproduction. Mais les ressources peuvent manquer pour cette nouvelle génération, elle peut donc ne pas être en mesure de se développer. Par conséquent, le nombre de bombyx dépend de ces deux facteurs contradictoires, et son évolution est loin d'être triviale.

   Appelons xi le nombre de la i-ème génération de papillons. Voici un modèle pour l'évolution de xi:

[equation](include/calculation.png)

Afin d'étudier cette évolution, il est demandé de tracer deux choses :

    *La courbe représentant le nombre d'individus en fonction de la génération (allant de 1 à 100).

    *Un schéma synthétique résumant tous les résultats pour un n donné ; il consiste à tracer chaque valeur de xi (entre deux bornes données), en fonction de k (k variant de 1 à 4 par pas de 0,01).

Dans les deux cas, votre programme doit afficher sur la sortie standard les valeurs à entrer dans gnuplot pour dessiner les graphes comme ci-dessus:

### Output
[output](/include/output.png)

### Graphs
[drawergnu](include/drawergnu.png)

Les graphes dépendent donc des paramètres de calcul mais aussi des paramètres que l'on donne dans le le fichier "drawer.gnu". En effet on utilise la redirection en rentrant cette commande ""cat drawer.gnu | gnuplot"" directement dans le terminal de gnuplot.
Vous pouvez vous amuser à modifier tout les paramètres et étudier les diferents comportemens.


## English

   In the 70's, chaos theory opened the way for a better understanding of the evolution of some animal species. Butterflies, for instance, have been studied in this context. We will be focusing on the bombyx, which is a species of butterfly.

   If a generation is crowded, chances are that the next generation will be crowded too, regarding the natural rules of reproduction. But resources may lack for this new generation, so it may not be able to develop. Therefore, the number of bombyx depends on these two contradictory factors, and its evolution is far from trivial.

   Let xi be the number of the ith generation of butterflies. Here is a model for the evolution of xi:

[equation](include/calculation.png)

In order to study this evolution, you are asked to plot two things:

    *The curve representing the number of individuals in relation to the generation (varying from 1 to 100).
    
    *A synthetic scheme summing all the results for a given n; it consists in plotting every value of xi (between two given bounds), in relation to k (k varying from 1 to 4 by 0.01 steps).

In both cases, your program shall print on the standard output the values to be entered into gnuplot to draw the graphs as follows :

### Output
[output](/include/output.png)

### Graphs
[drawergnu](include/drawergnu.png)

The graphs depend on the calculation parameters as well as the parameters provided in the "drawer.gnu" file. Indeed, we use redirection by entering the command "cat drawer.gnu | gnuplot" directly into the gnuplot terminal.

You can have fun modifying all the parameters and studying the different behaviors.
