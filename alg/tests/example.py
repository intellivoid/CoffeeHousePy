from coffeehouse_alg.utilities import Utilities
from coffeehouse_alg.image_tagger import ImageTagger


url = "https://cdn4.telesco.pe/file/ETCYVng0VOEczJuIjUbsgzC4a7EOi8wMfwfFBAss_OlKZd822FNiF5Xy5V7MpY0nUvHcBCzDt1MexuBrawuit0WL5HGa0-O5bZXYsBwA5P4QAFKM6VyH0k1G9VbnCn-QiFJ5ipClcP1azPykgcRqDz4d-g_3IHWegBY3wHBD8BHm1T589XhkXbfCl_HN6TJSZ1LIYnoASnN1FF6YDV92UOhMc0-c2FTQkoxx-gGt4A7Vwy821x4-TAd6AlNI_q5NO4NKe047oRlJfm_MCtEsojYGP5tyJKB-xZYm_zRtzriwC0GSJh2zoY_RCv4L-Uudq3GGQ0_8A2OrHCmCNj0AGA.jpg"

image_tagger = ImageTagger()
image_content = Utilities.process_img_from_url(url)

print(image_tagger.predict_tags(image_content))
print(image_tagger.predict_inception(image_content))