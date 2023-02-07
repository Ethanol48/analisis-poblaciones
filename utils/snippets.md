For changing the male data to positive:


#### first, load the file

```python
  tmp_df = pd.read_csv('../../data/processed/Spain/Spain-1950.csv', index_col=0)
```

#### second, run this code

``` python
for index, cuerpo in tmp_df.iterrows():

    if tmp_df.iloc[index]['Gender'] == 'Male':
        tmp_df.iloc[index] = tmp_df.iloc[index]['Age'], \
            tmp_df.iloc[index]['Count'] * -1, \
                tmp_df.iloc[index]['Gender']
    else:
        pass
```

And that's it, enjoy the data
