import unittest

# Renommage de la fonction pour un nom plus explicite
# 'names' -> 'count_long_names'
def count_long_names(names):
    """
    Count the number of names with more than seven letters.
    
    Args:
        names: List of names to evaluate.
    
    Returns:
        The number of names with more than seven letters.
    """
    long_name_count = 0
    
    # Introduction d'une variable pour éviter le nombre magique 7
    long_word_threshold = 7
    
    for name in names:
        # Utilisation de la variable 'long_word_threshold' pour améliorer la lisibilité
        if len(name) > long_word_threshold:
            long_name_count += 1
            # Utilisation de f-strings pour rendre l'affichage plus lisible
            print(f"{name} est un prénom avec un nombre de lettres supérieur à {long_word_threshold}")
        else:
            print(f"{name} est un prénom avec un nombre de lettres inférieur ou égal à {long_word_threshold}")
    
    return long_name_count

# Renommage de la classe de test pour correspondre à la nouvelle fonction
class TestCountLongNames(unittest.TestCase):
    def test_count_long_names(self):
        # Renommage de la liste pour un nom plus descriptif
        names_list = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_long_names(names_list)
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()