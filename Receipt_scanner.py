#!/usr/bin/env python
import pytesseract
from PIL import Image
import pandas as pd

img = Image.open('receipt.jpg')

# Simple image to string
text = pytesseract.image_to_string(img)
# print(type(text))
# print(text)

text_splitted = text.splitlines()
text_splitted

# create a dataframe
data_pd = {"item_id":[], "item":[], "price":[]}
for line in text_splitted:
    if len(line) > 9:
        split_space = line.split(" ")
#         print(split_space)
        try:
            item_id_test_int = int(split_space[0])
            item_id = split_space[0]
            price = split_space[-1]
#             print(item_id)
#             print(price)
            split_space.remove(item_id)
            split_space.remove(price)
            item = " ".join(split_space)
            data_pd["item_id"].append(item_id)
            data_pd["item"].append(item)
            data_pd["price"].append(price)
        except:
            continue

df = pd.DataFrame(data=data_pd)
print(df)
