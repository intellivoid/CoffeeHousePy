import os
from resource_fetch import ResourceFetch
from coffeehouse_dltc.main import DLTC

__all__ = ['SpamDetection']


class SpamDetection(object):

    def __init__(self):
        """
        Public Constructor
        """
        self.dltc = DLTC()
        self.rf = ResourceFetch()
        self.model_directory = os.path.join(self.rf.fetch("Intellivoid", "CoffeeHouseData-Spam"), 'spam_ham_build')
        self.dltc.load_model_cluster(self.model_directory)

    def predict(self, text_input):
        """
        Takes the user input and predicts if the input is either
        spam or ham

        :param text_input:
        :return: Returns dictionary "ham", "spam" prediction values
        """
        return self.dltc.predict_from_text(text_input)
