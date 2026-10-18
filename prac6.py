import pandas as pd

data = {
    'Name': ['Apurva', 'Shruti', 'Sharad', 'Nilima', 'vedika'],
    'Age': [20, 21, None, 22, 20],
    'Marks': [85, 90, 75, None, 80],
    'City': ['Pune', 'Mumbai', 'Pune', 'Nashik', 'Mumbai']
}

df = pd.DataFrame(data)

print(df)