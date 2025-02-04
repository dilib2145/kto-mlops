import unittest

def count_long_names(names):
    """
    Count the number of names with more than seven letters.
    
    Args:
        names: List of names to evaluate.
    
    Returns:
        The number of names with more than seven letters.
    """
    long_name_count = 0
    long_word_threshold = 7
    
    for name in names:
        if len(name) > long_word_threshold :
            long_name_count += 1
            print(f"{name} est un prénom avec un nombre de lettres supérieur à 7")
        else:
            print(f"{name} est un prénom avec un nombre de lettres inférieur ou égal à 7")
    
    return long_name_count

class TestCountLongNames(unittest.TestCase):
    def test_count_long_names(self):
        names_list = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_long_names(names_list)
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()