
# mylambdata/my_script.py

from my_lambdata.my_mod import enlarge, Df_fancy
import pandas as pd

# print("Hello World")


# x = 5
# print("Number", x)
# print("Enlarged number", enlarge(x))

# Test the generate_data function
df = pd.DataFrame(data={'target': [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                        'cat1': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
                        'cat2': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']})

# Instantiate an instance of Df_fancy
df_fancy = Df_fancy(df)

# See shape before generating new data
print(df_fancy.df.shape)

# Generate new data for 2 rows
df_fancy.generate_data(rows_to_add=2)

# Check the shape to see if it changed correctly
print(df_fancy.df.shape)


