# Création Min Heap (Heapify) - même logique pour un max mais là c'est un min
# Time: O(n), Space: O(1) car on le fait en place si on a déjà un array

def heapify(arr, n, i):
    """
    arr : tableau représentant le heap
    n   : taille du heap (nombre d'éléments dans arr)
    i   : index du nœud "racine" du sous-arbre qu'on veut heapifier
    
    But : s'assurer que le sous-arbre à la position i respecte la propriété de min-heap.
    """
    smallest = i          # On suppose que le parent est le plus petit
    left = 2 * i + 1      # Index de l'enfant gauche
    right = 2 * i + 2     # Index de l'enfant droit

    # Vérifie si l'enfant gauche existe et est plus petit que arr[smallest]
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    # Vérifie si l'enfant droit existe et est plus petit que arr[smallest]
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # Si le plus petit n'est plus le parent, on échange et on continue
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Échange
        heapify(arr, n, smallest)  # Continue la vérification plus bas

def heap_insert(heap, val):
    """
    heap : tableau représentant le min-heap
    val  : valeur à insérer
    """
    # 1. On ajoute la valeur à la fin
    heap.append(val)
    i = len(heap) - 1  # index du nouvel élément

    # 2. On remonte l'élément si nécessaire
    while i > 0:
        parent = (i - 1) // 2
        # Si le parent est plus grand que le nouvel élément, on échange
        if heap[parent] > heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break

def heap_pop(heap):
    """
    heap : tableau représentant le min-heap
    Retourne l'élément minimum (racine) et réorganise le heap.
    """
    n = len(heap)
    if n == 0:
        return None
    
    # 1. Le plus petit élément est à la racine
    min_val = heap[0]
    
    # 2. On met le dernier élément à la racine
    heap[0] = heap[n - 1]
    
    # 3. On retire le dernier élément de la liste
    heap.pop()  # supprime la dernière case, déjà copiée en racine
    n -= 1
    
    # 4. On rétablit la structure de min-heap
    if n > 0:
        heapify(heap, n, 0)
    
    return min_val

def build_min_heap(arr):
    """
    Transforme un tableau 'arr' en min-heap.
    """
    n = len(arr)
    # On part du dernier nœud non-feuille (index = (n//2) - 1) jusqu'à 0
    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort_desc(arr):
    """
    Trie le tableau 'arr' en ordre décroissant
    en utilisant un min-heap.
    """
    n = len(arr)
    
    # 1. Construire un min-heap
    build_min_heap(arr)
    
    # 2. Extraire le min, et le placer à la fin
    for i in range(n - 1, 0, -1):
        # On échange la racine (le plus petit) avec l'élément en cours de slot
        arr[0], arr[i] = arr[i], arr[0]
        
        # maintenant, arr[i] est le plus petit et placé à la fin (pour un tri décroissant)
        # on "réduit" le tas à la portion arr[0..i-1]
        heapify(arr, i, 0)  # i = taille effective du tas restant

# ----------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------

def heapify_max(arr, n, i):
    """
    Assure la propriété de max-heap pour le sous-arbre dont la racine est à l'indice i.

    Paramètres :
    ----------
    arr : list
        Le tableau représentant le tas (max-heap).
    n : int
        La taille EFFECTIVE du tas à prendre en compte dans arr (souvent = len(arr)).
        On ne doit pas dépasser cet index lorsqu'on regarde les enfants.
    i : int
        L'index de la « racine » du sous-arbre que l'on veut corriger/réorganiser.
        (Cette racine a potentiellement deux enfants, situés à 2*i+1 et 2*i+2.)
    
    Fonctionnement :
    ---------------
    - On compare arr[i] avec ses deux enfants (indices left = 2*i+1, right = 2*i+2).
    - Si l'un des enfants est plus grand que arr[i], on l'échange avec celui qui est le plus grand.
      (On nomme cette position 'largest').
    - Ensuite, on continue la vérification (heapify_max) plus bas dans l'arbre, car l'échange 
      a pu casser la propriété max-heap en dessous.
    
    But :
    ----
    - Après l'appel, le sous-arbre enraciné à i respecte la propriété du max-heap :
      * tout parent est >= à chacun de ses enfants.
    """
    largest = i  # On suppose, pour commencer, que le parent 'i' est le plus grand
    left = 2 * i + 1  # index enfant gauche
    right = 2 * i + 2  # index enfant droit

    # Vérifie si l'enfant gauche existe (left < n) et s'il est plus grand que le parent courant
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Vérifie si l'enfant droit existe (right < n) et s'il est plus grand que le 'plus grand' actuel
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si le plus grand n'est pas le parent, on échange
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Puis on continue la vérification plus bas
        heapify_max(arr, n, largest)


def heap_insert_max(heap, val):
    """
    Insère un nouvel élément 'val' dans le max-heap 'heap'.

    Paramètres :
    ----------
    heap : list
        Le tableau représentant un max-heap valide (avant insertion).
    val : int
        La valeur à insérer dans le tas.
    
    Fonctionnement :
    ---------------
    1. On ajoute 'val' à la fin de la liste (heap.append).
    2. Tant que l'élément ajouté est plus grand que son parent,
       on l'échange avec son parent et on remonte (i = parent).
    3. On s'arrête quand la propriété max-heap est rétablie ou qu'on est arrivé à la racine.
    """
    # 1. Ajouter la valeur à la fin
    heap.append(val)
    i = len(heap) - 1  # index du nouvel élément

    # 2. Rééquilibrer en "remontant" l'élément, tant qu'il est plus grand que son parent
    while i > 0:
        parent = (i - 1) // 2  # index du parent
        if heap[i] > heap[parent]:
            # Échange
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent  # On remonte d'un niveau
        else:
            # Si le parent est déjà plus grand, on ne fait rien de plus
            break


def heap_pop_max(heap):
    """
    Retire et retourne le plus grand élément (la racine) du max-heap 'heap'.

    Paramètres :
    ----------
    heap : list
        Le tableau représentant un max-heap valide.

    Retourne :
    --------
    Le maximum (racine du tas) ou None si heap est vide.

    Fonctionnement :
    ---------------
    1. On prend l'élément racine (index 0) : c'est le plus grand.
    2. On place le dernier élément du tableau à la racine (index 0).
    3. On supprime le dernier élément (qui a été "copié" en racine).
    4. On appelle heapify_max(...) sur l'index 0 pour rétablir la propriété max-heap.
    """
    n = len(heap)
    if n == 0:
        return None  # Rien à retirer

    # 1. Le plus grand élément est à la racine (index 0)
    max_val = heap[0]

    # 2. On place le dernier élément du tableau à la racine
    heap[0] = heap[-1]
    # 3. On supprime le dernier élément
    heap.pop()

    # 4. On restaure la structure max-heap à la racine
    heapify_max(heap, len(heap), 0)

    return max_val


def build_max_heap(arr):
    """
    Transforme la liste 'arr' en un max-heap.

    Paramètres :
    ----------
    arr : list
        Le tableau contenant des nombres dans n'importe quel ordre.

    Fonctionnement :
    ---------------
    - On part du dernier 'parent' potentiel, c'est-à-dire (n//2) - 1, et on remonte
      jusqu'à l'indice 0.
    - Pour chaque index i, on appelle heapify_max pour forcer la propriété de max-heap.
    - Résultat : 'arr' est réorganisé pour devenir un tas binaire (max-heap).
    
    Rappel indices :
    - En Python, on indexe depuis 0 : 
      * enfant_gauche(i) = 2*i + 1
      * enfant_droit(i)  = 2*i + 2
    - Les "feuilles" commencent à index (n//2).
    """
    n = len(arr)
    # On "heapify" en partant du dernier parent pour descendre jusqu'à 0 en index
    for i in range((n // 2) - 1, -1, -1):
        heapify_max(arr, n, i)


def heap_sort_asc(arr):
    """
    Trie la liste 'arr' en ordre croissant (ascending) en utilisant un max-heap.

    Paramètres :
    ----------
    arr : list
        La liste de nombres à trier.

    Fonctionnement :
    ---------------
    1. On construit d'abord un max-heap à partir de 'arr' (build_max_heap).
    2. On va alors extraire le plus grand élément et le placer en fin de liste.
    3. On rétrécit la partie "heap" du tableau (car l'élément du fond est déjà bien placé)
       et on appelle à nouveau heapify_max pour maintenir le max-heap dans le reste.
    4. On répète jusqu'à ce que tous les éléments soient placés dans l'ordre croissant.

    Exemples :
    ---------
    Si arr = [3, 1, 5, 2], après appel, arr sera [1, 2, 3, 5].
    (On a trié croissant grâce au max-heap.)
    """
    n = len(arr)

    # 1. Construire un max-heap (après ceci, arr[0] = plus grand élément)
    build_max_heap(arr)

    # 2. Extraire le max en l'échangeant avec la fin, puis "réduire" le tas
    #    pour ne plus y inclure l'élément placé à la fin.
    for i in range(n - 1, 0, -1):
        # Échanger le plus grand (racine) avec l'élément en position i
        arr[0], arr[i] = arr[i], arr[0]
        # Maintenant, arr[i] est "le plus grand" et placé à sa position finale.
        
        # Rétablir la propriété max-heap pour la portion arr[0..i-1]
        heapify_max(arr, i, 0)

