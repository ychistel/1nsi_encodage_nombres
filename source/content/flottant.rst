Les nombres flottants
=====================

Les nombres à virgule ont une représentation en binaire. En informatique, ces nombres sont dits **flottants**.

Représentation en virgule fixe
------------------------------

Les nombres flottants ont une partie avant la virgule et une partie après la virgule.

- La partie entière est composée de puissances de 2 positives;
- La partie après la virgule (ou le point), est composée de puissances de 2 d'exposants négatifs.

.. admonition:: Exemple

   Le nombre :math:`1001,01` écrit en binaire représente un nombre à virgule. Pour le convertir en écriture décimale, on associe à chaque chiffre sa puissance de 2.
   
   .. math::
      
      1001,01_{2} &= 1\times 2^{3} + 0\times 2^{2} + 0\times 2^{1} + 1\times 2^{0} + 0\times 2^{-1} + 1\times 2^{-2}\\
      1001,01_{2} &= 8 + 1 + \dfrac{1}{4}\\
      1001,01_{2} &= 9,25_{10}
      
La représentation des nombres à virgules en binaire est dans certains cas inexacte. En effet la partie située après la virgule n'est pas nécessairement décomposable avec des puissances de 2. Cela conduit donc a des approximations dont la précision dépend du nombre de bits alloués à l'écriture de la partie après la virgule.

.. admonition:: Exemple

   La partie après la virgule du nombre :math:`0,3` est représenté sur 1 octet par ``01001100``. 
   En effectuant le calcul des puissances de 2, on obtient:

   .. math::

      01001100_{2} &=  0 \times 2^{-1} + 1 \times 2^{-2} + 0 \times 2^{-3} + 0 \times 2^{-4} + 1 \times 2^{-5} + 1 \times 2^{-6} + 0 \times 2^{-3} + 0 \times 2^{-4}\\
      01001100_{2} &=  \dfrac{1}{4} + \dfrac{1}{32} + \dfrac{1}{64}\\
      01001100_{2} &= 0,296875
      
.. important::

   C'est pour cette raison qu'on ne peut pas effectuer de test d'égalité entre 2 nombres à virgule. 

   Si ``a`` et ``b`` sont 2 nombres à virgule, le test ``a == b`` est remplacé par le test ``abs(a - b) < 0.0001`` où le nombre ``0.0001`` représente la précision attendue.

Représentation en virgule flottante
-----------------------------------

Dans le système décimal, la **notation scientifique** est une écriture d'un nombre sous la forme :math:`a \times 10^{n}` où le nombre :math:`a` est compris entre 1 et 10.
L'exposant :math:`n` correspond au décalage de la virgule dans le nombre.

En binaire, les nombres peuvent s'écrire avec une puissance de :math:`2`. On décale la virgule jusqu'au premier chiffre non nul. Voilà pourquoi on parle de **flottant** en faisant référence à cette virgule qui **flotte** (se décale).

.. admonition:: Exemple

	-  :math:`11010101_{2}=1,1010101 \times 2^{7}`
	-  :math:`11010,101_{2}=1,1010101 \times 2^{3}`
	-  :math:`0,0000101_{2}=1,01 \times 2^{-5}`

Norme IEEE 754
--------------

Les représentations des nombres flottants suivent une **norme** d’écriture selon les modèles d’architecture 32 ou 64 bits.

Cette représentation binaire se décompose en 3 parties:

-	le premier bit est réservé au signe du nombre; le bit 0 pour un nombre positif et le bit 1 pour un nombre négatif.
-	les bits suivants (8 ou 11) sont réservés à l'exposant que l'on décale en ajoutant la valeur :math:`127` pour une architecture 32 bits et la valeur :math:`1023` pour une architecture 64 bits.
-	les derniers bits (23 ou 52) représentent la **mantisse** du nombre. Cette valeur est toujours comprise entre 1 et 2 ce qui implique que le premier chiffre de la mantisse vaut 1 et n'est pas représenté. Par conséquent, seuls les chiffres écrits après la virgule sont représentés.

On résume cette représentation dans le tableau ci-dessous:

.. table::
   :class: border-style-solid border-width-1
   
   +------------+-----+-------------------+------------+
   |architecture|signe|exposant + décalage|mantisse - 1|
   +============+=====+===================+============+
   |32 bits     |1 bit|8 bits             |23 bits     |
   +------------+-----+-------------------+------------+
   |64 bits     |1 bit|11 bits            |52 bits     |
   +------------+-----+-------------------+------------+

.. admonition:: Exemple

   On donne la représentation binaire d'un nombre flottant sur une architecture 32 bits:

   .. figure:: ../img/flottant_2.svg
      :align: center
      :width: 480
	
	-	le bit de signe vaut 1, donc le nombre est négatif.
	-	l'exposant *e* est décalé de 127:

   .. math::

      e &= 2^{7}+2^{2}+2^{1} - 127\\
      e &= 128+4+2 - 127\\
      e &= 7
	
   -	la mantisse *m* vaut ``101011011``. En ajoutant le bit ``1`` devant la virgule, on obtient ``1,101011011``. Si on décale la virgule de 7 rangs, on obtient le nombre (à virgule fixe) ``11010110,11``. On peut convertir la partie avant la virgule:
	
   .. math::
      
      11010110_{2} &= 2^{7} + 2^{6} + 2^{4} + 2^{2} + 2^{1}\\
      11010110_{2} &= 128 + 64 + 16 + 4 + 2\\
      11010110_{2} &= 214
			
   et celle après la virgule:

   .. math::

      0,11_{2} &= 2^{-1} + 2^{-2}\\
      0,11_{2} &= \dfrac{1}{2} + \dfrac{1}{4}\\
      0,11_{2} &= 0,75
	
   Au final, on obtient le nombre :math:`-214,75`.


