# Différentes versions de quick sort

def quick_sort(arr, start, end):
    """
    Quick Sort (version 1)
    - pivot = arr[end] (dernier élément)
    - Partitionne, puis appelle récursivement sur la partie gauche et droite

    Complexités :
      - Pire cas : O(n^2)
      - Cas moyen : O(n log n)
      - Meilleur cas : O(n log n)

    Stability : Non stable
    """
    if start < end:
        # On récupère l'indice du pivot après partition
        pivot_index = partition(arr, start, end)

        # On trie la partie gauche (avant le pivot)
        quick_sort(arr, start, pivot_index - 1)

        # On trie la partie droite (après le pivot)
        quick_sort(arr, pivot_index + 1, end)

def partition(arr, start, end):
    """
    Partitionne arr[start..end] autour de arr[end] comme pivot

    Retourne l'index final du pivot.
    """
    pivot_value = arr[end]  # pivot = dernier élément
    i = start - 1  # frontière des éléments ≤ pivot

    # Parcourt toute la portion [start..end-1]
    for j in range(start, end):
        if arr[j] <= pivot_value:
            i += 1
            # Échange l'élément arr[j] avec arr[i]
            arr[i], arr[j] = arr[j], arr[i]

    # À la fin, on place le pivot juste après la dernière position ≤ pivot
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def quickSort2(alist, g, d):
    """
    QuickSort version 2
    - pivot = alist[(g + d)//2]
    - On avance i depuis g et j depuis d,
      puis on swap quand on trouve alist[i] >= pivot et alist[j] <= pivot
    - On s'arrête quand i >= j

    Complexités :
      - Pire cas : O(n²)
      - Cas moyen : O(n log n)
      - Meilleur cas : O(n log n)

    Stability : Non stable
    """
    if g < d:
        i = g
        j = d
        pivot = alist[(i + j) // 2]

        while True:
            # Avance i tant que alist[i] < pivot
            while alist[i] < pivot:
                i += 1
            # Recule j tant que alist[j] > pivot
            while alist[j] > pivot:
                j -= 1

            # Si i >= j, partition terminée
            if i >= j:
                break

            # Sinon, on swap les 2 valeurs qui ne sont pas du bon côté
            alist[i], alist[j] = alist[j], alist[i]
            i += 1
            j -= 1

        # Appel récursif sur partie gauche
        quickSort2(alist, g, i - 1)
        # Appel récursif sur partie droite
        quickSort2(alist, j + 1, d)

def quickSort3(alist, g, d):
    """
    QuickSort version 3
    - pivot = alist[g] (premier élément)
    - partition3 organise la liste pour mettre le pivot en bonne place
    - On applique ensuite la recursion à gauche puis à droite

    Complexités :
      - Pire cas : O(n²)
      - Cas moyen : O(n log n)
      - Meilleur cas : O(n log n)

    Stability : Non stable
    """
    if g < d:
        p = partition3(alist, g, d)
        # Partie gauche
        quickSort3(alist, g, p - 1)
        # Partie droite
        quickSort3(alist, p + 1, d)


def partition3(alist, g, d):
    """
    Partition avec pivot = alist[g].
    i part de g+1 vers la droite,
    j part de d vers la gauche,
    On échange quand alist[i] >= pivot et alist[j] <= pivot
    """
    pivot = alist[g]
    i = g + 1
    j = d
    done = False

    while not done:
        # Avancer i tant que alist[i] < pivot
        while i <= j and alist[i] < pivot:
            i += 1
        # Reculer j tant que alist[j] > pivot
        while j >= i and alist[j] > pivot:
            j -= 1
        if j < i:
            # i a dépassé j => on s'arrête
            done = True
        else:
            # On échange
            alist[i], alist[j] = alist[j], alist[i]
            i += 1
            j -= 1

    # Finalement, on met le pivot au bon endroit (index j)
    alist[g], alist[j] = alist[j], alist[g]
    return j

def quickSort_optim1(alist, g, d):
    """
    Quick Sort avec élimination de la recursion de queue (tail recursion)

    - On choisit pivot = arr[end] par ex. (via partition)
    - On n'appelle récursivement que sur la plus petite sous-liste
    - L'autre sous-liste est traitée en 'while' (mise à jour de g ou d)

    Avantage : réduit la profondeur de la pile.
    """
    while g < d:
        p = partition(alist, g, d)  # partition version pivot = alist[d]

        # On choisit la plus petite des 2 sous-listes pour l'appel récursif
        if (p - g) < (d - p):
            # Sous-liste gauche est plus petite
            quickSort_optim1(alist, g, p - 1)
            # On traite la sous-liste droite en itérant
            g = p + 1
        else:
            # Sous-liste droite est plus petite
            quickSort_optim1(alist, p + 1, d)
            d = p - 1


def partition(arr, start, end):
    """
    Même partition que la version 1 (pivot = arr[end]).
    """
    pivot_value = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

"""
Principe
On compare 3 valeurs : list[g] (début), alist[m] (milieu), alist[d] (fin).
On fait de petits swaps pour mettre la médiane de ces 3 valeurs en position alist[m].
Puis, souvent, on swap alist[m] avec alist[d] afin d'utiliser la médiane comme pivot final (ex. pivot = alist[d]).
Avantage : Réduit le risque d'un mauvais pivot (trop petit ou trop grand). Diminue la probabilité d'tre en O(n²).
"""
def optimisePivot(alist, g, d):
    """
    Choix d'un pivot avec 'median of three' :
    Compare alist[g], alist[m], alist[d]
    s'assure de mettre la médiane au final en alist[d].
    """
    m = (g + d) // 2

    # 1) On veut s'assurer que alist[g] <= alist[m] <= alist[d] ou un ordre équivalent
    # Compare pivot middle vs pivot end
    if alist[m] > alist[d]:
        alist[m], alist[d] = alist[d], alist[m]
    # Compare pivot start vs pivot middle
    if alist[g] > alist[m]:
        alist[g], alist[m] = alist[m], alist[g]
    # Compare pivot end vs pivot middle
    if alist[d] > alist[m]:
        alist[d], alist[m] = alist[m], alist[d]

    # Maintenant, la médiane est en 'alist[d]'
    # On peut s'en servir comme pivot dans la partition arr[end].


"""
Quicksort avec Insertion Sort, idée :
Quand la sous-liste [g..d] a moins de lim éléments (par ex. lim = 8), on applique Insertion Sort plutôt que de continuer Quick Sort.
Pour de petits segments, Insertion Sort peut être plus rapide que faire un partitionnement supplémentaire.
Avantage
On évite de faire beaucoup de partitions pour des très petits tableaux, ce qui peut être peu efficace.
Globalement, on gagne du temps.
"""

def qsort_with_insertion(alist, g, d, lim=8):
    """
    Quick Sort optimisé :
      - Tail Recursion Elimination
      - Pivot = median of three
      - On applique un insertion sort local sur les sous-listes de taille <= lim

    Paramètres:
      alist : la liste à trier (in-place)
      g : index de début
      d : index de fin
      lim : taille seuil en dessous de laquelle on fait insertion sort

    1. Tant que la portion [g..d] est plus grande que lim:
       a) On choisit un pivot 'intelligent' (median-of-three)
       b) On partitionne
       c) On appelle récursivement sur la plus petite sous-liste (pour limiter la profondeur)
       d) On met à jour g ou d pour continuer dans la boucle 'while'
    2. Quand la portion [g..d] fait <= lim, on applique un insertion_sort localement.

    Complexités (en moyenne):
      - O(n log n), 
      - Gain sur les petits segments (insertion sort) 
      - Pivot median-of-three réduit les risques de pire cas
    Non stable.
    """
    while (d - g + 1) > lim:
        # 1) On choisit le pivot par median-of-three
        optimisePivot(alist, g, d)
        # 2) On partitionne (pivot = alist[d])
        p = partition(alist, g, d)

        # 3) Tail recursion trick: on ne fait qu'un appel récursif (sur la plus petite partie)
        if (p - g) < (d - p):
            # Gauche plus petite => récursion à gauche
            qsort_with_insertion(alist, g, p - 1, lim)
            g = p + 1  # on itère sur la partie droite
        else:
            # Droite plus petite => récursion à droite
            qsort_with_insertion(alist, p + 1, d, lim)
            d = p - 1

    # Ici, la portion [g..d] a une taille <= lim
    sublist = alist[g : d + 1]
    insertion_sort(sublist)  
    # On réinjecte la sous-liste triée
    alist[g : d + 1] = sublist


def partition(arr, start, end):
    """
    Partition standard version pivot = arr[end].
    """
    pivot_value = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def optimisePivot(alist, g, d):
    """
    Place la médiane de alist[g], alist[m], alist[d] en alist[d].
    """
    m = (g + d) // 2
    if alist[m] > alist[d]:
        alist[m], alist[d] = alist[d], alist[m]
    if alist[g] > alist[m]:
        alist[g], alist[m] = alist[m], alist[g]
    if alist[d] > alist[m]:
        alist[d], alist[m] = alist[m], alist[d]


def insertion_sort(unsorted_list):
    """
    Tri par insertion : on construit la liste triée petit à petit
    """
    for i in range(1, len(unsorted_list)):
        key = unsorted_list[i]
        j = i - 1
        while j >= 0 and unsorted_list[j] > key:
            unsorted_list[j + 1] = unsorted_list[j]
            j -= 1
        unsorted_list[j + 1] = key
    return unsorted_list
# avec ce type de quick sort on a 
#Pivot médiane de 3 (optimisePivot)
#Partition standard (pivot = arr[end])
#Tail Recursion
#Insertion sort sur les petites sous-listes 

"""
Quick Sort : “Drapeau tricolore” (three-way partition)
Principe du drapeau tricolore
Au lieu de classer seulement < pivot et > pivot, on va gérer trois zones : 
Les éléments strictement inférieurs au pivot. Les éléments égaux au pivot. Les éléments strictement supérieurs au pivot.

Concrètement, on utilise trois indices : 
lt (low) : tout ce qui est avant lt est < pivot.
gt (great) : tout ce qui est après gt est > pivot.
i : on inspecte arr[i] et on déplace l'élément dans la zone appropriée.

Avantage :
Si beaucoup d'éléments sont égaux au pivot, on évite de multiplier les appels récursifs pour ces valeurs.
Tout ce qui est = pivot reste au milieu, on ne les re-trie pas.

Complexités :
Pire cas : O(n²) (si on choisit mal le pivot ou la distribution est extrême)
Cas moyen : O(n log n)
Meilleur cas : O(n log n)
Stabilité : Non stable
"""
def quickSort_3way(arr, start, end):
    """
    Quick Sort avec partitionnement en trois parties (drapeau tricolore).
    - Gère le cas où plusieurs éléments sont égaux au pivot.
    - Pivot = arr[start] ici par simplicité.

    Complexités:
      - Pire cas : O(n^2)
      - Cas moyen : O(n log n)
      - Meilleur cas : O(n log n)
    Non stable.
    """
    if start < end:
        lt, gt = partition_3way(arr, start, end)
        # lt = index où se finit la zone < pivot
        # gt = index où commence la zone > pivot
        # la zone [lt..gt] contient les éléments = pivot

        # On trie récursivement la zone < pivot
        quickSort_3way(arr, start, lt - 1)
        # On trie récursivement la zone > pivot
        quickSort_3way(arr, gt + 1, end)

def partition_3way(arr, start, end):
    """
    Partition drapeau tricolore.
    On prend pivot = arr[start].
    Les indices importants:
      - lt : frontière de la zone < pivot
      - gt : frontière de la zone > pivot
      - i  : index pour parcourir le tableau

    Au final:
      - tout avant lt est < pivot
      - tout entre lt et gt est = pivot
      - tout après gt est > pivot
    """
    pivot = arr[start]
    lt = start      # lt pointe le début de la zone = pivot
    i = start + 1   # i est le parcours
    gt = end        # gt pointe la fin de la zone = pivot
    while i <= gt:
        if arr[i] < pivot:
            # L'élément est < pivot => on swap arr[i] avec arr[lt], puis on avance lt et i
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            # L'élément est > pivot => on swap arr[i] avec arr[gt], on recule gt
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
            # Attention, on n'avance pas i car l'élément qu'on vient de swap depuis gt
            # peut être <, =, ou > pivot
        else:
            # arr[i] == pivot
            i += 1
    # A la fin:
    # [start..lt-1] = zone < pivot
    # [lt..gt] = zone = pivot
    # [gt+1..end] = zone > pivot

    return lt, gt

