Nombre signé en binaire
=======================

Ecriture binaire
----------------

Les nombres entiers négatifs et positifs sont appelés des **nombres signés**.

-  Si l’écriture binaire du nombre commence par :math:`1` (bit de poids fort), alors le nombre est **négatif**.
-  Si l’écriture binaire du nombre commence par :math:`0` (bit de poids fort), alors le nombre est **positif**.

Sur un octet (8 bits), on peut écrire :math:`2^{8}=256` valeurs. La moitié de ces valeurs sont négatives et l'autre moitié sont des nombres positifs. 

-  On a 128 nombres négatifs compris entre :math:`-2^{7}=-128` et :math:`-1`,
-  On a 128 nombres positifs compris entre :math:`0` et :math:`2^{7}-1=127`.

Sur **n** bits, on a :math:`2^{n}` nombres entiers signés qui sont compris entre :math:`-2^{n-1}` et :math:`2^{n-1}-1`.
 
.. admonition:: Exemple

   Pour :math:`n = 5` bits, on dispose de :math:`2^{5}=32` écritures binaires.
   
   - Le plus petit nombre entier négatif a pour valeur : :math:`-2^{5-1}=-2^{4}=-16`;
   - Le plus grand nombre entier positif a pour valeur : :math:`2^{5-1}-1=2^{4}-1=16-1=15`;
   
   Sur 5 bits on écrit en binaire les nombres signés de :math:`-16` à :math:`15`.

Nombre de bits
--------------

Le nombre minimum de bits pour écrire un nombre signé en binaire dépend de la valeur de ce nombre. Pour connaître ce nombre de bits, il suffit de trouver le plus petit intervalle dont les bornes sont deux puissances de 2 contenant ce
nombre signé.

.. admonition:: Exemple

	Combien de bits pour écrire le nombre :math:`-23` en binaire ?

	On a :math:`-32 \leqslant -23 <32` ce qui est équivalent à :math:`-2^{5} <	-23 < 2^{5}`.

	On en déduit qu'il faut au minimum :math:`5+1=6` bits pour coder le nombre :math:`-23`.

De façon générale, cela revient à chercher un exposant :math:`k` tel que le nombre signé appartient à l'intervalle :math:`[-2^{k};2^{k}]`.

Cela nous donne :math:`2^{k+1}` nombres dans l'intervalle et donc il faut au minimum :math:`k+1` bits pour coder le nombre signé.

Complément à 2
--------------

Les nombres signés positifs se convertissent en binaire comme les nombres entiers (non signés).

Les nombres signés négatifs ne se convertissent pas comme les nombres positifs. Un nombre signé négatif est converti par la méthode du **complément à 2**.

L’écriture binaire d’un nombre signé négatif s’obtient à partir du nombre signé positif (valeur absolue) et de son complément à 2.

.. rubric:: Méthode du complément à 2

Elle se fait en trois étapes:

1. écriture binaire de la valeur absolue du nombre négatif,
2. le **complément à 1** de cette écriture binaire, ce qui signifie que chaque bit 0 est remplacé par le bit 1 et chaque bit 1 est remplacé par le bit 0.
3. le **complément à 2** c’est à dire en ajoutant 1 au complément à 1.

.. admonition:: Exemple

   Écriture binaire du nombre négatif :math:`-23` se code sur 6 bits.

   - on écrit 23 en binaire sur 6 bits : :math:`010111`
   - le complément à 1 de :math:`010111` est :math:`101000`
   - le complément à 2 de :math:`101000` est :math:`101000+1=101001`

   En binaire, le nombre :math:`-23` s'écrit :math:`101001` sur 6 bits.

.. important::

   Le nombre de bits utilisés est important. Par exemple, le nombre :math:`-23` s'écrit :math:`101001` sur 6 bits et il s'écrit :math:`11101001` sur 1 octet.

.. note::

   Soit :math:`n` le nombre signé négatif codé en binaire sur :math:`k` bits. Le nombre signé :math:`n` se code en binaire comme le nombre entier :math:`n+2^{k}`.

   1. On calcule la valeur :math:`n+2^{k}`.
   2. On convertit en binaire le nombre calculé précédemment.


   Par exemple, le nombre signé :math:`-23` se code sur 6 bits. 
      
   1. Il se code en binaire comme le nombre :math:`-23+2^{6}=-23+64=41`.
   2. Comme :math:`41_{10}=32+8+1` donc :math:`41_{10}=101001_{2}` sur 6 bits. 
      
   On en déduit que :math:`-23_{10}=101001_{2}` sur 6 bits.
