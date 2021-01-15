import os
from resource_fetch import ResourceFetch
from coffeehouse_dltc.main import DLTC

__all__ = ['EmotionPrediction']


class EmotionPrediction(object):

    def __init__(self):
        """
        Public Constructor
        """
        self.dltc = DLTC()
        self.rf = ResourceFetch()
        self.model_directory = os.path.join(
            self.rf.fetch("Intellivoid", "CoffeeHouseData-ProfleIO"),
            "advanced_sentiments_build"
        )
        self.dltc.load_model_cluster(self.model_directory)

    def predict(self, text_input):
        """
        Takes the user input and predicts if the input is either
        spam or ham

        :param text_input:
        :return: Returns dictionary "neutral", "happiness", "affection", "sadness" and "anger" prediction values
        """
        return self.dltc.predict_from_text(text_input)
