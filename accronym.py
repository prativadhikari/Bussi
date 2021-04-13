"""
the program prints an acronym which is formed by taking the first
letter of every word in a name and capitalizing it.
"""
def create_an_acronym(phrase):
    """
    :param phrase: string, any phrase to be entered for abbreviation
    :return: string, the string is splitted and only abbreviation is returned
    """
    phrase=phrase.split()
    accronym=[]
    for i in phrase:
        accronym=accronym+i[0].upper()
    return accronym




