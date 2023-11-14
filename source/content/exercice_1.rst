Exercices
=========

Exercice 1
----------

Donner l'encodage en binaire et sur 1 octet des nombres signés suivants. On détaillera la méthode.

a. :math:`-17`
b. :math:`33`
c. :math:`-78`
d. :math:`-104`
   
Exercice 2
----------

On s'interesse aux nombres écrits sur 4 bits. Tout l'exercice se fait dans un tableau représenté ci-dessous.

+--------------+--------------+--------------+--------------+--------------+
|nombre binaire|complément à 1|complément à 2|complément à 1|complément à 2|
+--------------+--------------+--------------+--------------+--------------+
|0101          |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+
|01110         |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+
|011011        |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+
|0111001       |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+
|01010110      |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+

#. Compléter les 2 premières colonnes avec le complément à 1 puis le complément à 2 du nombre binaire de la première colonne.
#. Compléter les colonnes 4 et 5 avec le complément à 1 puis le complément à 2 du nombre binaire de la troisième colonne.
#. Comparer les valeurs binaires des colonnes 1 et 5. Que peut-on en conclure ?

Exercice 3
----------

#. On donne le nombre signé :math:`10011011` encodé sur 1 octet.

   a. Quel est le signe de ce nombre? Justifier.
   b. Quelle est la valeur décimale de ce nombre ?
   c. Donner une écriture hexadécimale de ce nombre signé.

#. On donne le nombre signé :math:`11011010` encodé sur 1 octet.

   a. Quel est le signe de ce nombre? Justifier.
   b. Quelle est la valeur décimale de ce nombre ?
   c. Donner une écriture hexadécimale de ce nombre signé.

Exercice 4
----------

Dans l'interpréteur Python, il est possible de calculer en binaire et en hexadécimal. Il faut préfixer chaque écriture   de nombre par ``0b`` pour le binaire et ``0x`` pour l'hexadécimal. 

Par exemple, le nombre écrit en binaire :math:`101_{2}` est saisi par ``0b101`` et le nombre écrit en hexadécimal :math:`2c_{16}` est saisi par ``0x2c``.

Aussi, il existe 3 fonctions qui convertissent un nombre écrit dans une base dans une autre base.

-  ``bin`` prend en argument un nombre entier écrit dans une base et renvoie ce nombre écrit en binaire.

   >>> bin(15)
   '0b1111'
   >>> bin('0xa5')
   '0b10100101'

-  ``hex`` prend en argument un nombre entier écrit dans une base et renvoie ce nombre écrit en hexadécimal.

   >>> hex(45)
   '0x2d'
   >>> hex(0b11110001)
   '0xf1'

- ``int`` prend en argument un nombre entier écrit dans une base et renvoie ce nombre écrit en décimal.

   >>> int(0b111)
   7
   >>> int(0xff)
   255

.. caution::
   
   Les valeurs renvoyées par les fonctions ``bin`` et ``hex`` sont des chaines de caractères !

#. Dans l'interpréteur Python:

   a. Convertir en décimal les nombres :math:`1001_{2}` et :math:`11010_{2}`.
   b. Calculer la somme et le produit des nombres :math:`1001_{2}` et :math:`11010_{2}`
   c. En utilisant la bonne fonction, convertir en binaire et en hexadécimal les résultats précédents.
   
#. Dans l'interpréteur Python:

   a. Convertir en décimal les nombres :math:`a8_{16}` et :math:`54_{16}`
   b. Calculer la somme et le produit des nombres :math:`a8_{16}` et :math:`54_{16}`.
   c. En utilisant la bonne fonction, convertir en hexadécimal et en binaire les résultats précédents.
