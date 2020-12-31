from googletrans import Translator

__all__ = ['ChTranslation']


class ChTranslation(object):

    def __init__(self):
        """
        Public Constructor
        """
        self.google_translator = Translator()

    def google_translate(self, source, output, text_input):
        """
        Translates the given input using Google Translate

        :rtype: object
        """
        results = self.google_translator.translate(text_input, src=source, dest=output)
        return {
            "text": results.text,
            "pronunciation": results.pronunciation
        }