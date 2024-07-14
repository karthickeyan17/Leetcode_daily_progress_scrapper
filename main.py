import pandas as pd 
import scraper as Scraper
from datetime import datetime ,timedelta
import streamlit as st
import os
st.title("LEETCODE STATS TRACKER")
DB_PATH= "./Student_db.csv"
OUTPUT_PATH = "./leetcode_stats.csv"
def fetch_stats(date):
    df = pd.read_csv(DB_PATH)
    df2=None
    for index, row in df.iterrows():
        problems_byDate = Scraper.getProblems(row['Leetcode ID'])
        val=problems_byDate.get(date)
        t=pd.DataFrame(val if val else {'Easy': 0, 'Medium': 0, 'Hard': 0},index=[0])
        t['date'] = date
        t['Name']= row['Name']
        melted_df = pd.melt(t, id_vars=['date', 'Name'], var_name='level', value_name='count')
        pivot_df = pd.pivot_table(melted_df, columns=['date', 'level'], index='Name', values='count', aggfunc='sum')
        if df2 is None:
            df2=pivot_df
        else:
            df2=pd.concat([df2,pivot_df],axis=0)

    if os.path.isfile(OUTPUT_PATH):
        res=pd.read_csv(OUTPUT_PATH,header=[0, 1],index_col=[0])
        res.update(df2)
        res.to_csv(OUTPUT_PATH)
<<<<<<< HEAD
    print(res)  
    st.write(res) 
=======
    else:
         df2.to_csv(OUTPUT_PATH)
>>>>>>> 765dd166e931a8826953a5dc33532697a73d70aa
    
if __name__ == "__main__":
    date = datetime.now().date()
    print("Fetching for date:",date)
    fetch_stats(date)
