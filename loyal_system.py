import streamlit as st 
import pandas as pd


st.title('LOYAL SYSTEM')
userid = pd.to_numeric(st.text_input('User ID'))


df = pd.read_csv("clusteredData.csv")
top_cluster_category = pd.read_csv('cluster_categories.csv')
top_category_merchant = pd.read_csv('category_merchants.csv')


if st.button('Predict') :
    
    if userid in df['User_Id'].values:

        st.text(f'UserID {userid} information:-')
        
        cluster = df.loc[df["User_Id"] == userid , "clusterID"].item()
        st.text(f'User Cluster is  {cluster}')
        
        category1 = top_cluster_category.loc[top_cluster_category['clusterID']==cluster]['Category In English'].values[0]
        merchant1_cat1 = top_category_merchant.loc[top_category_merchant['Category In English']==category1]['Mer_Id'].values[0]
        merchant2_cat1 = top_category_merchant.loc[top_category_merchant['Category In English']==category1]['Mer_Id'].values[1]
        
        category2 = top_cluster_category.loc[top_cluster_category['clusterID']==cluster]['Category In English'].values[1]
        merchant1_cat2 = top_category_merchant.loc[top_category_merchant['Category In English']==category2]['Mer_Id'].values[0]
        merchant2_cat2 = top_category_merchant.loc[top_category_merchant['Category In English']==category2]['Mer_Id'].values[1]
        
        
        category3 = top_cluster_category.loc[top_cluster_category['clusterID']==cluster]['Category In English'].values[2]
        merchant1_cat3 = top_category_merchant.loc[top_category_merchant['Category In English']==category3]['Mer_Id'].values[0]
        merchant2_cat3 = top_category_merchant.loc[top_category_merchant['Category In English']==category3]['Mer_Id'].values[1]
        
        
        st.text(f'The Top Category is {category1}')
        st.text(f'--> Top Merchants for {category1} is {merchant1_cat1} and {merchant2_cat1}')
        st.text(f'The Second Category is {category2}')
        st.text(f'--> Top Merchants for {category2} is {merchant1_cat2} and {merchant2_cat2}')
        st.text(f'The Third Category is {category3}')
        st.text(f'--> Top Merchants for {category3} is {merchant1_cat3} and {merchant2_cat3}')
        
        user_statues = df.loc[df['User_Id'] == userid, 'customers_statues'].item()
        if user_statues == 'not active':
            st.text(f'THIS USER IS {user_statues}  😥')
        else:
            st.text(f'THIS USER IS {user_statues} 😀')
            
        
    else:
        st.text("This user not in dataset")