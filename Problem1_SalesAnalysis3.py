import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df=sales.groupby('product_id').agg(
        mindate=('sale_date','min'),
        maxdate=('sale_date','max')
    )

    df=df[(df['mindate']>='2019-01-01') & (df['maxdate']<='2019-03-31')]
    print(df)
    df=df.merge(product,
                on='product_id',
                how='inner')
    
    return df[['product_id','product_name']]