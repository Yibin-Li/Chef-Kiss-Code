## Figma Prototype Link: https://www.figma.com/file/SDThHApw8okxiZDlRlIIKv/Chefs-Kiss-v2?node-id=0%3A1
# Chef-Kiss-Code
Our code samples contains two most important parts of the prototype: receipt scanner and food recipe recommendation based on leftover food. Each of the code script (*.py) can be executed with `python <filename>.py`.
## Recipe Recommender
Utilized dataset from Kaggle for list of recipes and ingredients.
*Note: The recommender only lists the ID of the recipes since the dataset does not have recipe name itself.
![alt text](https://github.com/Yibin-Li/Chef-Kiss-Code/blob/main/sample_recipe_rec.png)
## Receipt Scanner
Utilized pytesseract for image OCR to convert the image to text. The script will process a receipt image and store the data to a pandas dataframe.

input

![Receipt](https://github.com/Yibin-Li/Chef-Kiss-Code/blob/main/receipt.jpg)

output

![Receipt Scanner](https://github.com/Yibin-Li/Chef-Kiss-Code/blob/main/Screen%20Shot%202020-11-29%20at%208.53.48%20PM.png)
