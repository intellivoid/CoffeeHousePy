# CoffeeHouse ALG

CoffeeHouse ALG is a algorithmia API wrapper

## Image Tagger

Predicts the content and appropriate tags for an image

```python
from coffeehouse_alg.utilities import Utilities
from coffeehouse_alg.image_tagger import ImageTagger

url = "https://cdn4.telesco.pe/file/ETCYVng0VOEczJuIjUbsgzC4a7EOi8wMfwfFBAss_OlKZd822FNiF5Xy5V7MpY0nUvHcBCzDt1MexuBrawuit0WL5HGa0-O5bZXYsBwA5P4QAFKM6VyH0k1G9VbnCn-QiFJ5ipClcP1azPykgcRqDz4d-g_3IHWegBY3wHBD8BHm1T589XhkXbfCl_HN6TJSZ1LIYnoASnN1FF6YDV92UOhMc0-c2FTQkoxx-gGt4A7Vwy821x4-TAd6AlNI_q5NO4NKe047oRlJfm_MCtEsojYGP5tyJKB-xZYm_zRtzriwC0GSJh2zoY_RCv4L-Uudq3GGQ0_8A2OrHCmCNj0AGA.jpg"

# Process the image
image_tagger = ImageTagger()
image_content = Utilities.process_img_from_url(url)

image_tagger.predict_tags(image_content)
# {'result': {'character': [], 'copyright': [], 'general': [{'photo': 0.995330810546875}, {'cosplay': 0.28029680252075195}, {'solo': 0.2679383456707001}], 'rating': [{'safe': 0.7592381834983826}, {'questionable': 0.21827033162117004}, {'explicit': 0.024775557219982147}]}, 'metadata': {'content_type': 'json', 'duration': 0.298899313}}

image_tagger.predict_inception(image_content)
# {'result': {'tags': [{'class': 'Persian cat', 'confidence': 0.6589894890785217}, {'class': 'Egyptian cat', 'confidence': 0.009713547304272652}, {'class': 'handkerchief, hankie, hanky, hankey', 'confidence': 0.00886216014623642}, {'class': 'Angora, Angora rabbit', 'confidence': 0.008085943758487701}, {'class': 'teddy, teddy bear', 'confidence': 0.00662141153588891}]}, 'metadata': {'content_type': 'json', 'duration': 0.594030507}}
```