# CoffeeHouse ALG

CoffeeHouse ALG is a algorithmia API wrapper

## Image Tagger

Predicts the content and appropriate tags for an image

```python
from coffeehouse_alg.image_tagger import ImageTagger
from coffeehouse_alg.utilities import Utilities

url = "https://upload.wikimedia.org/wikipedia/commons/9/9f/Gisele_Bundchen_2018_clear_original_%28cropped%29.jpg"

# Process the image
image_tagger = ImageTagger()
image_content = Utilities.process_img_from_url(url)

image_tagger.predict_tags(image_content)
# {'result': {'character': [], 'copyright': [], 'general': [{'photo': 0.995330810546875}, {'cosplay': 0.28029680252075195}, {'solo': 0.2679383456707001}], 'rating': [{'safe': 0.7592381834983826}, {'questionable': 0.21827033162117004}, {'explicit': 0.024775557219982147}]}, 'metadata': {'content_type': 'json', 'duration': 0.298899313}}

image_tagger.predict_inception(image_content)
# {'result': {'tags': [{'class': 'Persian cat', 'confidence': 0.6589894890785217}, {'class': 'Egyptian cat', 'confidence': 0.009713547304272652}, {'class': 'handkerchief, hankie, hanky, hankey', 'confidence': 0.00886216014623642}, {'class': 'Angora, Angora rabbit', 'confidence': 0.008085943758487701}, {'class': 'teddy, teddy bear', 'confidence': 0.00662141153588891}]}, 'metadata': {'content_type': 'json', 'duration': 0.594030507}}
```