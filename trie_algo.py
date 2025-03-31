"""
Bubble sort
Complexité en temps :

Pire cas : O(n²)
Cas moyen : O(n²)
Meilleur cas (si déjà trié) : O(n)

Stabilité : Stable
Les éléments égaux conservent leur ordre d'apparition initial

"""
def bubble_sort(unsorted_list):
    """ algo de trie qui fonctionne comme des bulles, il va prendre celui où il point et celui d'après pour les swaps
    """
    # Car on commence à compter par 0
    taille_list = len(unsorted_list) - 1
    # On définit de base que la liste n'est pas trié pour itérer dedans
    sorted = False
    while not sorted:
        # C'est pour qu'on n'ait pas à refaire une boucle si la liste est trié
        sorted = True
        # On itère jusqu'à l'avant dernier et pas jusqu'au dernier car range s'arrête dès qu'il est au dernier pour pouvoir les échanger
        for i in range(0, taille_list):
            # c'est ici qu'on compare car si on s'arrête pas à l'avant dernier et on s'arrête au dernier bah on aura
            # un index qui va au delà de la taille de la liste avec le i+1 et cela provoquera une erreur index out of range
            if unsorted_list[i] > unsorted_list[i+1]:
                # Si on a trouvé une seule différence c'est que la liste n'est pas trié et qu'on devra encore re itéré pour pouvoir tout mettre dans le bon ordre
                sorted = False
                # On swap car les deux valeurs ne sont pas au bon endroit
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
    # Après toutes les itérations on retourne la liste trié
    return unsorted_list

test_bs = [1,5,3,6,2,67,2,154,53,6]
print("Test bubble sort : ",bubble_sort(test_bs))


"""
Selection Sort
Complexité en temps :

Pire cas : O(n²)
Cas moyen : O(n²)
Meilleur cas : O(n²)

Stabilité : Non stable 
Si deux valeurs sont égales, l'ordre initial entre elles n'est généralement pas garanti

"""
# Selection sort (unstable)
def selection_sort(unsorted_list):
    """ algo de tri qui fonctionne avec un minimum où on va aller dans la liste et supposer que le 1er est le minimum, ensuite
    si on trouve un autre plus petit que ce nombre bah il devient le minimum et on fait ça jusqu'à la fin
    et quand on a fini d'itérer à travers toute la liste comme ça on est sûr que dans la liste on a récupéré ce minimum, on l'échange avec notre 1er élément
    car on est sûr que c'est le minimum, maintenant on fait de même mais avec une sous liste qui prend tout les éléments après cette élément déjà trié comme ça on est sûr qu'on va pas retomber 
    sur le minimum qu'on a déjà trié et aller sur le restant de la liste et faire ce qu'on a fait encore et encore jusqu'à la fin et à la fin on aura tout les minimums trié un par un jusqu'à la liste trié
    """
    # On récupère la taille de la liste pour savoir jusqu'où itérer
    taille_list = len(unsorted_list)
    # On parcourt la liste indice par indice
    for i in range(taille_list):
        # On part du principe que l'élément à l'indice i est le plus petit de la partie non triée
        index_min = i
        # On cherche dans la partie non triée (de l'indice i+1 à la fin de la liste)
        for j in range(i+1, taille_list):
            # Si on trouve un élément plus petit que celui actuellement considéré
            if unsorted_list[j] < unsorted_list[index_min]:
                # On met à jour l'indice du plus petit élément
                index_min = j
        # Une fois le plus petit élément trouvé dans la partie non triée,
        # on échange cet élément avec celui à l'indice i
        unsorted_list[i], unsorted_list[index_min] = unsorted_list[index_min], unsorted_list[i]
    # Après avoir parcouru toute la liste, celle-ci est triée
    return unsorted_list

# Exemple de test
test = [1, 5, 3, 6, 2, 67, 2, 154, 53, 6]
print(selection_sort(test))


"""
Insertion Sort
Complexité en temps :

Pire cas : O(n²)
Cas moyen : O(n²)
Meilleur cas : O(n)

Stabilité : Stable

Les éléments égaux conservent leur ordre d'apparition initial
"""
# Insertion sort (stable)
def insertion_sort(unsorted_list):
    """
    L'algorithme de tri par insertion (insertion sort) fonctionne en construisant progressivement
    une liste triée, en insérant les éléments un à un dans la bonne position.
    """

    # On récupère la taille de la liste pour savoir jusqu'où on va itérer
    taille_list = len(unsorted_list)

    # On commence à partir du 2ᵉ élément, car on considère que le 1er est déjà "trié" tout seul
    for i in range(1, taille_list):
        
        # On sauvegarde la valeur de l'élément qu'on veut insérer
        valeur_a_inserer = unsorted_list[i]

        # On crée un index temporaire (j) qu'on utilisera pour comparer/insérer l'élément (c'est genre un poiteur pour savoir où on est)
        j = i - 1

        # Tant qu'on n'est pas au tout début de la liste ET que l'élément précédent est plus grand
        # que la valeur à insérer, on décale cet élément vers la droite.
        while j >= 0 and unsorted_list[j] > valeur_a_inserer:
            unsorted_list[j + 1] = unsorted_list[j]
            j -= 1
        
        # À ce stade, on a trouvé l'emplacement correct pour insérer la valeur
        unsorted_list[j + 1] = valeur_a_inserer
    
    # Après avoir inséré tous les éléments, la liste est triée
    return unsorted_list


# Exemple de test avec des nombres variés
test_insertion = [8, 3, 1, 7, 2, 9, 0]
print("Avant tri :", test_insertion)
print("Après tri (insertion sort) :", insertion_sort(test_insertion))

"""
Merge sort
Complexité en temps :

Pire cas : O(n log n)
Cas moyen : O(n log n)
Meilleur cas : O(n log n)

Stabilité : Stable

Les éléments égaux conservent leur ordre d'apparition initial

Inconvénient : Nécessite de la mémoire supplémentaire pour fusionner (surtout dans la version top-down comme ici).


"""

def merge_sort(unsorted_list):
    """
    Merge Sort est un algorithme de tri qui suit un principe «diviser pour régner».
    Il divise la liste en deux, trie récursivement chaque moitié, puis fusionne les deux moitiés triées.
    """
    # Si la liste a 0 ou 1 élément, elle est déjà triée par définition
    if len(unsorted_list) <= 1:
        return unsorted_list

    # 1. On trouve le point médian pour couper la liste en deux
    mid = len(unsorted_list) // 2

    # 2. On sépare la liste en deux parties : gauche et droite
    left_half = unsorted_list[:mid]
    right_half = unsorted_list[mid:]

    # 3. On trie récursivement la partie gauche et la partie droite
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 4. On fusionne (merge) les deux sous-listes triées
    return merge(left_sorted, right_sorted)


def merge(left_list, right_list):
    """
    Fusionne deux sous-listes déjà triées (left_list et right_list)
    en une seule liste triée, et la retourne.
    """
    sorted_list = []
    i, j = 0, 0  # i parcourra la left_list, j parcourra la right_list

    # Tant qu'on n'a pas atteint la fin de l'une des deux listes
    while i < len(left_list) and j < len(right_list):
        # On compare les éléments courants de chaque sous-liste
        if left_list[i] <= right_list[j]:
            # Si left_list[i] est plus petit ou égal, on l'ajoute au résultat
            sorted_list.append(left_list[i])
            i += 1
        else:
            # Sinon, on ajoute celui de la right_list
            sorted_list.append(right_list[j])
            j += 1

    # On ajoute les éléments restants (s'il y en a) de la left_list
    while i < len(left_list):
        sorted_list.append(left_list[i])
        i += 1

    # On ajoute les éléments restants (s'il y en a) de la right_list
    while j < len(right_list):
        sorted_list.append(right_list[j])
        j += 1

    return sorted_list


# Exemple d'utilisation :
test_merge_list = [38, 27, 43, 3, 9, 82, 10]
print("Liste avant tri :", test_merge_list)
result = merge_sort(test_merge_list)
print("Liste après tri (Merge Sort) :", result)

def shell_sort(arr):
    """
    Tri Shell (Shell Sort):
    1) On commence avec un gap (demi-taille de la liste par ex.)
    2) Pour chaque gap, on effectue un 'insertion sort' sur des sous-listes espacées de gap
    3) On réduit progressivement le gap jusqu'à 1
    4) Quand gap = 1, on fait un insertion sort final (sur la liste presque triée), puis c'est fini
    
    Complexités:
      - Pire cas : O(n^2)
      - Cas moyen : dépend de la séquence de gaps (souvent ~ O(n^(3/2)) ou O(n^(1.3)) )
      - Non stable

    Il est en place, pas besoin de mémoire en plus
    """
    
    n = len(arr)
    gap = n // 2  # Par exemple, on commence par la moitié, On choisit un gap initial, souvent n//2

    # Tant qu'il y a un gap > 0
    while gap > 0:

        # On effectue un 'insertion sort' modifié pour chaque sous-liste définie par le gap
        for start_position in range(gap):
            # On trie la sous-liste formée par les indices start_position, start_position+gap, ...
            gap_insertion_sort(arr, start_position, gap)

        # On réduit le gap
        gap //= 2
    
    return arr


def gap_insertion_sort(arr, start, gap):
    """
    Cette fonction fait un tri par insertion 
    sur les éléments séparés par 'gap'.

    Ex: si start = 0 et gap = 4, on va traiter 
    arr[0], arr[4], arr[8], arr[12], ...
    """
    i = start + gap
    while i < len(arr):
        current_value = arr[i]
        position = i

        # On compare arr[position-gap] et current_value
        # et on décale si l'élément précédent est plus grand
        while position >= gap and arr[position - gap] > current_value:
            arr[position] = arr[position - gap]
            position -= gap
        
        # On insère la current_value dans la bonne position
        arr[position] = current_value
        i += gap

# Exemple d'utilisation
test_shell = [14, 4, 2, 6, 3, 5, 12, 10] 
print("Liste avant tri :", test_shell)
shell_sort(test_shell)
print("Liste après Shell Sort :", test_shell)

"""
Quick sort 1er version
Complexité en temps :

Pire cas : O(n²)
Cas moyen : O(n log n)
Meilleur cas : O(n log n)

Stabilité : Non stable sauf implémentation spéciale

Pour voir les autres version de quicksort et optimisé voir autre fichier quicksort_algo_trie
"""
def quick_sort(arr, start, end):
    """
    Quick Sort est un algorithme de tri en 'divide and conquer'.
    Il sélectionne un pivot, partitionne le tableau, et trie récursivement
    les parties gauche et droite.
    
    :param arr: la liste à trier
    :param start: index de début (inclus)
    :param end: index de fin (inclus)
    """
    if start < end:
        # 1. On récupère l'indice du pivot après partition
        pivot_index = partition(arr, start, end)

        # 2. On trie la partie gauche (avant le pivot)
        quick_sort(arr, start, pivot_index - 1)

        # 3. On trie la partie droite (après le pivot)
        quick_sort(arr, pivot_index + 1, end)


def partition(arr, start, end):
    """
    La fonction partition réorganise la portion de la liste arr[start..end]
    autour d'un pivot. Ici, on choisit le pivot comme étant arr[end] (le dernier élément).
    
    :return: l'indice final du pivot dans le tableau partitionné.
    """
    pivot_value = arr[end]  # On prend le dernier élément comme pivot
    i = start - 1  # i va pointer vers la frontière entre les éléments < pivot et > pivot

    # On parcourt tous les éléments de start à end-1
    for j in range(start, end):
        # Si l'élément courant est <= pivot, on l'échange pour le mettre à gauche
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # À la fin, on place le pivot (arr[end]) juste après les éléments <= pivot
    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    # i+1 devient l'emplacement final du pivot
    return i + 1



# Exemple d'utilisation
test_quick = [10, 7, 8, 9, 1, 5]
print("Liste avant tri :", test_quick)

# On appelle quick_sort en précisant les indices de début et de fin
quick_sort(test_quick, 0, len(test_quick) - 1)
print("Liste après Quick Sort :", test_quick)




