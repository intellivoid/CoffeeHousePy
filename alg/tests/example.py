from coffeehouse_alg.utilities import Utilities
from coffeehouse_alg.image_tagger import ImageTagger


url = "https://upload.wikimedia.org/wikipedia/commons/9/9f/Gisele_Bundchen_2018_clear_original_%28cropped%29.jpg"

image_tagger = ImageTagger()
image_content = Utilities.process_img_from_url(url)

print(image_tagger.predict_tags(image_content))
print(image_tagger.predict_inception(image_content))