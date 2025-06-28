import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    Buyer2019=orders[(orders['order_date']>='2019-01-01')&(orders['order_date']<='2019-12-31')][['order_id','buyer_id']]
    Buyer2019=Buyer2019.groupby('buyer_id')['order_id'].size().reset_index(name='orders_in_2019')
    df=users.merge(Buyer2019,
                   left_on='user_id',
                   right_on='buyer_id',
                   how='left'
                   )
    
    df['orders_in_2019']=df['orders_in_2019'].fillna(0)
    return df[['user_id','join_date','orders_in_2019']].rename(columns={'user_id':'buyer_id'})
    