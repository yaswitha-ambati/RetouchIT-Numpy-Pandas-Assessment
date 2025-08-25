Section 1: NumPy

1 Broadcasting & Array Operations
Ans: A

2 Indexing & Slicing
Ans: A

3 Vectorized Operations
Ans:    import numpy as np 
        arr = np.array([-2, -1, 0, 1, 2])
        arr = np.where(arr<0, 0, arr)
        print(arr)

4 Aggregation & NaN Handling
Ans:    import numpy as np
        matrix = np.array([[1, np.nan, 3], [4, 5, np.nan]])
        row_mean = np.nanmean(matrix, axis=1)
        print(matrix)

5 Advanced Indexing
Ans: A

Section 2: Pandas

6 DataFrame Creation & Basics
Ans:    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
        df = pd.DataFrame(data, index=[100,101,102])

7 Handling Missing Data
Ans: 


8 GroupBy & Aggregation
Ans: import pandas as pd
     df = pd.DataFrame({
        'Region': ['North', 'South', 'North', 'South'],
        'Sales': [100, 200, 150, 250],
        'Profit': [20, 30, 25, 40]})
    df.groupby('Region').agg({'Sales':'sum', 'profit':'mean'}).reset_index()

9 Merging DataFrames
Ans:    import pandas as pd
        orders = pd.DataFrame({'order_id': [1, 2], 'cust_id': [101, 102]})
        customers = pd.DataFrame({'cust_id': [101, 103], 'name': ['Alice', 'Bob']})
        merged = pd.merge(orders, customers, on='cust_id', how='outer')

10 Time Series & Resampling
Ans:  import pandas as pd
        df = pd.DataFrame({
            'Date': ['2023-01-05', '2023-01-15', '2023-02-10'],
            'Value': [10, 20, 30]})
        
