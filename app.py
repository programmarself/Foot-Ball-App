# Import required modules
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np 
import json
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
# import creds
# import config
from PIL import Image
import plotly.express as px
import plotly.io as pio


# Set up title
st.set_page_config(page_title="Football App", 
                   layout="wide", 
                   page_icon=":soccer:", 
                   menu_items= 
         {'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!" }    
)


API_KEY = os.getenv("API_KEY")

# Hide Streamlit's default main menu & footer notes
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
	        content:'Made by SDW in Python '; 
	        visibility: visible ;
        }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown('<style>h1{color: green;}</style>', unsafe_allow_html=True)
st.markdown('<style>p{color: navyblue;}</style>', unsafe_allow_html=True)

pio.renderers.default = 'browser'
st.title("Football App")
st.header("Welcome to my Football App!")
st.write("""

#### Football stats on the top leagues in Europe for the 2021-22 season

""")





# load_dotenv()


# Load animations via Lottie website
def load_animation_via_link(web_link):
    r = requests.get(web_link)
    if r.status_code != 200:
        return None
    return r.json()


# Style your contact form
def style_contact_doc(file_name):
    with open(file=file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)




# Get the English Premier League table standings from RapidAPI
 ## League
st.markdown("***")
with st.container():
    columnL, columnR = st.columns(2)
    with columnL:  
       st.title("Table Standings")
       st.sidebar.header("League")
       league_table_options = st.sidebar.selectbox("Select a league:",["Premier League","Bundesliga","La Liga","Serie A","Ligue 1"])
       @st.cache
       def get_table_standings(league_id):

            ############################################# 1. PREMIER LEAGUE ##############################################
           if league_table_options == "Premier League":
               league_id = "39"
               endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/standings"
               query_string = {"season":"2021","league":league_id}
               headers = {
               'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
               'x-rapidapi-key': API_KEY
               }
               response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
               e = response.json()['response'] 
               df_e = pd.DataFrame(e)
               df_e1 = df_e['league'].apply(pd.Series)
               df_e2 = df_e1['standings'].apply(pd.Series)
               df_e2.columns = ['data']
               df_e3 = df_e2['data'].apply(pd.Series)
               output = df_e2.explode('data').assign(Co2 = lambda x: 
                                         x['data'].str.get('rank')).reset_index(drop=True)
               d = output['data'].apply(pd.Series)
               teams = d['team'].apply(pd.Series)
               games = d['all'].apply(pd.Series)
               goals = games['goals'].apply(pd.Series)    
               df = pd.DataFrame()
               df['Team'] = teams['name']
               df['MP'] = games['played']
               df['W'] = games['win']
               df['D'] = games['draw']
               df['L'] = games['lose']
               df['GF'] = goals['for']
               df['GA'] = goals['against']
               df['GD'] = d['goalsDiff']
               df['Pts'] = d['points']
               df['League'] = 'Premier League'
               df.index = np.arange(1, len(df)+1)
               print(df.to_string(index=False))
               table_standings_df = df    

            ############################################# 2. GERMAN BUNDESLIGA ##############################################               
           if league_table_options == "Bundesliga":
               league_id = "78"
               endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/standings"
               query_string = {"season":"2021","league":league_id}
               headers = {
               'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
               'x-rapidapi-key':  "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
               }
               response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
               e = response.json()['response'] 
               df_e = pd.DataFrame(e)
               df_e1 = df_e['league'].apply(pd.Series)
               df_e2 = df_e1['standings'].apply(pd.Series)
               df_e2.columns = ['data']
               df_e3 = df_e2['data'].apply(pd.Series)
               output = df_e2.explode('data').assign(Co2 = lambda x: x['data'].str.get('rank')).reset_index(drop=True)
               d = output['data'].apply(pd.Series)
               teams = d['team'].apply(pd.Series)
               games = d['all'].apply(pd.Series)
               goals = games['goals'].apply(pd.Series)
               df = pd.DataFrame()
               df['Team'] = teams['name']
               df['MP'] = games['played']
               df['W'] = games['win']
               df['D'] = games['draw']
               df['L'] = games['lose']
               df['GF'] = goals['for']
               df['GA'] = goals['against']
               df['GD'] = d['goalsDiff']
               df['Pts'] = d['points']
               df['League'] = 'Bundesliga'
               df.index = np.arange(1, len(df)+1)
               # print(df.to_string(index=False))
               table_standings_df = df


            ####################################### 3. LA LIGA ##############################################
           if league_table_options == "La Liga":
               league_id = "140"
               endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/standings"
               query_string = {"season":"2021","league":league_id}
               headers = {
               'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
               'x-rapidapi-key':  "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
               }
               response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
               e = response.json()['response'] 
               df_e = pd.DataFrame(e)
               df_e1 = df_e['league'].apply(pd.Series)
               df_e2 = df_e1['standings'].apply(pd.Series)
               df_e2.columns = ['data']
               df_e3 = df_e2['data'].apply(pd.Series)
               output = df_e2.explode('data').assign(Co2 = lambda x: x['data'].str.get('rank')).reset_index(drop=True)
               d = output['data'].apply(pd.Series)
               teams = d['team'].apply(pd.Series)
               games = d['all'].apply(pd.Series)
               goals = games['goals'].apply(pd.Series)
               df = pd.DataFrame()
               df['Team'] = teams['name']
               df['MP'] = games['played']
               df['W'] = games['win']
               df['D'] = games['draw']
               df['L'] = games['lose']
               df['GF'] = goals['for']
               df['GA'] = goals['against']
               df['GD'] = d['goalsDiff']
               df['Pts'] = d['points']
               df['League'] = 'La Liga'
               df.index = np.arange(1, len(df)+1)
               # print(df.to_string(index=False))
               table_standings_df = df


            ####################################### 4. SERIE A ##############################################            
           if league_table_options == "Serie A":
               league_id = "135"
               endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/standings"
               query_string = {"season":"2021","league":league_id}
               headers = {
               'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
               'x-rapidapi-key':  "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
               }
               response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
               e = response.json()['response'] 
               df_e = pd.DataFrame(e)
               df_e1 = df_e['league'].apply(pd.Series)
               df_e2 = df_e1['standings'].apply(pd.Series)
               df_e2.columns = ['data']
               df_e3 = df_e2['data'].apply(pd.Series)
               output = df_e2.explode('data').assign(Co2 = lambda x: x['data'].str.get('rank')).reset_index(drop=True)
               d = output['data'].apply(pd.Series)
               teams = d['team'].apply(pd.Series)
               games = d['all'].apply(pd.Series)
               goals = games['goals'].apply(pd.Series)
               df = pd.DataFrame()
               df['Team'] = teams['name']
               df['MP'] = games['played']
               df['W'] = games['win']
               df['D'] = games['draw']
               df['L'] = games['lose']
               df['GF'] = goals['for']
               df['GA'] = goals['against']
               df['GD'] = d['goalsDiff']
               df['Pts'] = d['points']
               df['League'] = 'Serie A'
               df.index = np.arange(1, len(df)+1)
               # print(df.to_string(index=False))
               table_standings_df = df   


            ####################################### 5. LIGUE 1 ##############################################       
           if league_table_options == "Ligue 1":
               league_id = "61"
               endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/standings"
               query_string = {"season":"2021","league":league_id}
               headers = {
               'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
               'x-rapidapi-key':  "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
               }
               response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
               e = response.json()['response'] 
               df_e = pd.DataFrame(e)
               df_e1 = df_e['league'].apply(pd.Series)
               df_e2 = df_e1['standings'].apply(pd.Series)
               df_e2.columns = ['data']
               df_e3 = df_e2['data'].apply(pd.Series)
               output = df_e2.explode('data').assign(Co2 = lambda x: x['data'].str.get('rank')).reset_index(drop=True)
               d = output['data'].apply(pd.Series)
               teams = d['team'].apply(pd.Series)
               games = d['all'].apply(pd.Series)
               goals = games['goals'].apply(pd.Series)
               df = pd.DataFrame()
               df['Team'] = teams['name']
               df['MP'] = games['played']
               df['W'] = games['win']
               df['D'] = games['draw']
               df['L'] = games['lose']
               df['GF'] = goals['for']
               df['GA'] = goals['against']
               df['GD'] = d['goalsDiff']
               df['Pts'] = d['points']
               df['League'] = 'Ligue 1'
               df.index = np.arange(1, len(df)+1)
               # print(df.to_string(index=False))
               table_standings_df = df   
           return table_standings_df 
       
       # Set up variables for top goal scorers with functions and corresponding league ids   
       premier_league_table =        get_table_standings(league_id = 39)
       bundesliga_table =            get_table_standings(league_id = 78)
       la_liga_table =               get_table_standings(league_id = 140)
       serie_a_table =               get_table_standings(league_id = 135)
       ligue_1_table =               get_table_standings(league_id = 61)
             
       
       # Display Premier League top goal scorers this season 
       if league_table_options == "Premier League":
           st.caption("Premier League Table 2021-22")
           st.dataframe(premier_league_table, width=800, height=600)
       
       
       # Display Bundesliga top goal scorers this season 
       elif league_table_options == "Bundesliga":
           st.caption("Bundesliga Table 2021-22")
           st.dataframe(bundesliga_table, width=800, height=600) 
       
       
       # Display La Liga top goal scorers this season 
       elif league_table_options == "La Liga":
           st.caption("La Liga Table 2021-22")
           st.dataframe(la_liga_table, width=800, height=600)
       
       
       # Display Serie A top goal scorers this season 
       elif league_table_options == "Serie A":
           st.caption("Serie A Table 2021-22")
           st.dataframe(serie_a_table, width=800, height=600) 
       
       # Display Ligue 1 top goal scorers this season 
       elif league_table_options == "Ligue 1":
           st.caption("Ligue 1 Table 2021-22")
           st.dataframe(ligue_1_table, width=800, height=600) 
       
       
       else:
           st.warning("Other leagues under construction!!!")
    with columnR:
        lottie_animation = load_animation_via_link("https://assets7.lottiefiles.com/packages/lf20_bvxz04bd.json")
        st_lottie(lottie_animation, height=400, width=700, key="tactics")
        
        lottie_animation = load_animation_via_link("https://assets7.lottiefiles.com/packages/lf20_ee2kjf6e.json")
        st_lottie(lottie_animation, height=400, width=700, key="tactics2")








## Top Goal Scorers
st.markdown("***")
st.title("Top Goal Scorers")
with st.container():
    columnL, columnR = st.columns(2)
    with columnL:
        
        st.sidebar.header("Top Goal Scorers")     
        top_goal_scorer_options = st.sidebar.selectbox("Select a league: ",["Premier League","Bundesliga","La Liga","Serie A","Ligue 1"])
        
        @st.cache
        def get_top_goal_scorers(league_id):

            ############################################# 1. PREMIER LEAGUE ##############################################
            if top_goal_scorer_options == "Premier League":
                league_id = "39"
                endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"
                query_string = {"season":"2021","league":league_id}
                headers = {
                'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
                'x-rapidapi-key': API_KEY
                }
                response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
                e = response.json()['response']
                df_e = pd.DataFrame(e)
                player_goals_stats_df_e1 = df_e['player'].apply(pd.Series)
                goals_stats_df_e1 = df_e['statistics'].apply(pd.Series)
                goals_stats_df_e1.columns = ['data']
                goals_stats_df_e2=goals_stats_df_e1['data'].apply(pd.Series)
                goals_stats_df_e3=goals_stats_df_e2['goals'].apply(pd.Series)
                df_concat = pd.concat([player_goals_stats_df_e1, goals_stats_df_e3], axis=1)
                final_df = df_concat[['name', 'age', 'nationality', 'total']]
                final_df['player'] = final_df['name']
                final_df['goals'] = final_df['total'].astype(int)
                final_df = final_df.drop(['total'], axis=1)
                final_df = final_df.drop(['name'], axis=1)
                final_df = final_df[['player', 'age', 'nationality', 'goals']]
                final_df.index = np.arange(1, len(final_df)+1)
                final_df['league'] = 'Premier League'
                top_goals_df = final_df



            ############################################# 2. GERMAN BUNDESLIGA ##############################################
            if top_goal_scorer_options == "Bundesliga":
                league_id = "78"
                endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"
                query_string = {"season":"2021","league":league_id}
                headers = {
                'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
                'x-rapidapi-key': API_KEY
                }
                response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
                e = response.json()['response']
                df_e = pd.DataFrame(e)
                player_goals_stats_df_e1 = df_e['player'].apply(pd.Series)
                goals_stats_df_e1 = df_e['statistics'].apply(pd.Series)
                goals_stats_df_e1.columns = ['data']
                goals_stats_df_e2=goals_stats_df_e1['data'].apply(pd.Series)
                goals_stats_df_e3=goals_stats_df_e2['goals'].apply(pd.Series)
                df_concat = pd.concat([player_goals_stats_df_e1, goals_stats_df_e3], axis=1)
                final_df = df_concat[['name', 'age', 'nationality', 'total']]
                final_df['player'] = final_df['name']
                final_df['goals'] = final_df['total'].astype(int)
                final_df = final_df.drop(['total'], axis=1)
                final_df = final_df.drop(['name'], axis=1)
                final_df = final_df[['player', 'age', 'nationality', 'goals']]
                final_df.index = np.arange(1, len(final_df)+1)
                final_df['league'] = 'Bundesliga'
                top_goals_df = final_df  



            ####################################### 3. LA LIGA ##############################################
            if top_goal_scorer_options == "La Liga":
                league_id = "140"
                endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"
                query_string = {"season":"2021","league":league_id}
                headers = {
                'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
                'x-rapidapi-key': API_KEY
                }
                response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
                e = response.json()['response']
                df_e = pd.DataFrame(e)
                player_goals_stats_df_e1 = df_e['player'].apply(pd.Series)
                goals_stats_df_e1 = df_e['statistics'].apply(pd.Series)
                goals_stats_df_e1.columns = ['data']
                goals_stats_df_e2=goals_stats_df_e1['data'].apply(pd.Series)
                goals_stats_df_e3=goals_stats_df_e2['goals'].apply(pd.Series)
                df_concat = pd.concat([player_goals_stats_df_e1, goals_stats_df_e3], axis=1)
                final_df = df_concat[['name', 'age', 'nationality', 'total']]
                final_df['player'] = final_df['name']
                final_df['goals'] = final_df['total'].astype(int)
                final_df = final_df.drop(['total'], axis=1)
                final_df = final_df.drop(['name'], axis=1)
                final_df = final_df[['player', 'age', 'nationality', 'goals']]
                final_df.index = np.arange(1, len(final_df)+1)
                final_df['league'] = 'La Liga'
                top_goals_df = final_df 



            ####################################### 4. SERIE A ##############################################
            if top_goal_scorer_options == "Serie A":
                league_id = "135"
                endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"
                query_string = {"season":"2021","league":league_id}
                headers = {
                'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
                'x-rapidapi-key': API_KEY
                }
                response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
                e = response.json()['response']
                df_e = pd.DataFrame(e)
                player_goals_stats_df_e1 = df_e['player'].apply(pd.Series)
                goals_stats_df_e1 = df_e['statistics'].apply(pd.Series)
                goals_stats_df_e2 = goals_stats_df_e1.apply(pd.Series)
                goals_stats_df_e2.columns = ['data']
                goals_stats_df_e3= goals_stats_df_e2['data'].apply(pd.Series)
                goals_stats_df_e4 = goals_stats_df_e3['goals'].apply(pd.Series)
                df_concat = pd.concat([player_goals_stats_df_e1, goals_stats_df_e4], axis=1)
                final_df = df_concat[['name', 'age', 'nationality', 'total']]
                final_df['player'] = final_df['name']
                final_df['goals'] = final_df['total'].astype(int)
                final_df = final_df.drop(['total'], axis=1)
                final_df = final_df.drop(['name'], axis=1)
                final_df = final_df[['player', 'age', 'nationality', 'goals']]
                final_df.index = np.arange(1, len(final_df)+1)
                final_df['league'] = 'Serie A'
                top_goals_df = final_df 



            ####################################### 5. LIGUE 1 ##############################################
            if top_goal_scorer_options == "Ligue 1":
                league_id = "61"
                endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"
                query_string = {"season":"2021","league":league_id}
                headers = {
                'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
                'x-rapidapi-key': API_KEY
                }
                response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
                e = response.json()['response']
                df_e = pd.DataFrame(e)
                player_goals_stats_df_e1 = df_e['player'].apply(pd.Series)
                goals_stats_df_e1 = df_e['statistics'].apply(pd.Series)
                goals_stats_df_e2 = goals_stats_df_e1.apply(pd.Series)
                goals_stats_df_e2.columns = ['data']
                goals_stats_df_e3= goals_stats_df_e2['data'].apply(pd.Series)
                goals_stats_df_e4 = goals_stats_df_e3['goals'].apply(pd.Series)
                df_concat = pd.concat([player_goals_stats_df_e1, goals_stats_df_e4], axis=1)
                final_df = df_concat[['name', 'age', 'nationality', 'total']]
                final_df['player'] = final_df['name']
                final_df['goals'] = final_df['total'].astype(int)
                final_df = final_df.drop(['total'], axis=1)
                final_df = final_df.drop(['name'], axis=1)
                final_df = final_df[['player', 'age', 'nationality', 'goals']]
                final_df.index = np.arange(1, len(final_df)+1)
                final_df['league'] = 'Ligue 1'
                top_goals_df = final_df    

            return top_goals_df    
    
        # Set up variables for top goal scorers with functions and corresponding league ids   
        premier_league_top_scorers = get_top_goal_scorers(league_id = 39)
        bundesliga_top_scorers =     get_top_goal_scorers(league_id = 78)
        la_liga_top_scorers =        get_top_goal_scorers(league_id = 140)
        serie_a_top_scorers =        get_top_goal_scorers(league_id = 135)
        ligue_1_top_scorers =        get_top_goal_scorers(league_id = 61)
        
        # Display Premier League top goal scorers this season 
        if top_goal_scorer_options == "Premier League":
            st.caption("Premier League Top Goal Scorers 2021-22")
            st.dataframe(premier_league_top_scorers, width=800, height=600)

        # Display Bundesliga top goal scorers this season 
        elif top_goal_scorer_options == "Bundesliga":
            st.caption("Bundesliga Top Goal Scorers 2021-22")
            st.dataframe(bundesliga_top_scorers, width=800, height=600) 

        # Display La Liga top goal scorers this season 
        elif top_goal_scorer_options == "La Liga":
            st.caption("La Liga Top Goal Scorers 2021-22")
            st.dataframe(la_liga_top_scorers, width=800, height=600)

        # Display Serie A top goal scorers this season 
        elif top_goal_scorer_options == "Serie A":
            st.caption("Serie A Top Goal Scorers 2021-22")
            st.dataframe(serie_a_top_scorers, width=800, height=600) 

        # Display Ligue 1 top goal scorers this season 
        elif top_goal_scorer_options == "Ligue 1":
            st.caption("Ligue 1 Top Goal Scorers 2021-22")
            st.dataframe(ligue_1_top_scorers, width=800, height=600) 

        else:
            st.warning("Top scorers currently under construction!!!")


    with columnR:
        # lottie_animation = load_animation_via_link("https://assets2.lottiefiles.com/packages/lf20_5mdp6mp1.json")
        lottie_animation = load_animation_via_link("https://assets2.lottiefiles.com/packages/lf20_wcgfedqr.json")
        st_lottie(lottie_animation, height=500, width=700, key="goal")



if top_goal_scorer_options == "Premier League":
    fig = px.bar(premier_league_top_scorers, x='player', y='goals',
         # hover_data=['lifeExp', 'gdpPercap'], 
         color='goals',
         labels={'goals':'Total goals scored'}, height=700)
    st.plotly_chart(fig, use_container_width=True)


if top_goal_scorer_options == "Bundesliga":
    fig = px.bar(bundesliga_top_scorers, x='player', y='goals',
         # hover_data=['lifeExp', 'gdpPercap'], 
         color='goals',
         labels={'goals':'Total goals scored'}, height=700)
    st.plotly_chart(fig, use_container_width=True)

if top_goal_scorer_options == "La Liga":
    fig = px.bar(la_liga_top_scorers, x='player', y='goals',
         # hover_data=['lifeExp', 'gdpPercap'], 
         color='goals',
         labels={'goals':'Total goals scored'}, height=700)
    st.plotly_chart(fig, use_container_width=True)

if top_goal_scorer_options == "Serie A":
    fig = px.bar(serie_a_top_scorers, x='player', y='goals',
         # hover_data=['lifeExp', 'gdpPercap'], 
         color='goals',
         labels={'goals':'Total goals scored'}, height=700)
    st.plotly_chart(fig, use_container_width=True)

if top_goal_scorer_options == "Ligue 1":
    fig = px.bar(ligue_1_top_scorers, x='player', y='goals',
         # hover_data=['lifeExp', 'gdpPercap'], 
         color='goals',
         labels={'goals':'Total goals scored'}, height=700)
    st.plotly_chart(fig, use_container_width=True)









st.markdown("****")
with st.container():
    columnL, columnR = st.columns(2)
    with columnL:
        st.title("Top Assists")
        st.sidebar.header("Top Assists")
        top_assists_options = st.sidebar.selectbox("Choose a league:", ["Premier League","Bundesliga","La Liga","Serie A","Ligue 1"])
        
        @st.cache       
        def get_top_assists(league_id):
        
            ############################################# 1. PREMIER LEAGUE ##############################################
            if top_assists_options == "Premier League":
                league_id = "39"
                endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/players/topassists"
                query_string = {"season":"2021","league":league_id}
                headers = {
                'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
                'x-rapidapi-key': API_KEY
                }
                response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
                e = response.json()['response']
                df_e = pd.DataFrame(e)
                player_assists_stats_df_e1 = df_e['player'].apply(pd.Series)
                assists_stats_df_e1 = df_e['statistics'].apply(pd.Series)
                assists_stats_df_e1.columns = ['data']
                assists_stats_df_e2=assists_stats_df_e1['data'].apply(pd.Series)
                assists_stats_df_e3=assists_stats_df_e2['goals'].apply(pd.Series)
                df_concat = pd.concat([player_assists_stats_df_e1, assists_stats_df_e3], axis=1)
                final_df = df_concat[['name', 'age', 'nationality', 'assists']]
                final_df['assists'] = final_df['assists'].astype(int)
                final_df['player'] = final_df['name']
                final_df = final_df.drop(['name'], axis=1)
                final_df = final_df[['player', 'age', 'nationality', 'assists']]
                final_df.index = np.arange(1, len(final_df)+1)
                final_df['league'] = 'Premier League'
                top_assists_df = final_df



            ############################################# 2. GERMAN BUNDESLIGA ##############################################
            if top_assists_options == "Bundesliga":
                league_id = "78"
                endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/players/topassists"
                query_string = {"season":"2021","league":league_id}
                headers = {
                'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
                'x-rapidapi-key': API_KEY
                }
                response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
                e = response.json()['response']
                df_e = pd.DataFrame(e)
                player_assists_stats_df_e1 = df_e['player'].apply(pd.Series)
                assists_stats_df_e1 = df_e['statistics'].apply(pd.Series)
                assists_stats_df_e1.columns = ['data']
                assists_stats_df_e2=assists_stats_df_e1['data'].apply(pd.Series)
                assists_stats_df_e3=assists_stats_df_e2['goals'].apply(pd.Series)
                df_concat = pd.concat([player_assists_stats_df_e1, assists_stats_df_e3], axis=1)
                final_df = df_concat[['name', 'age', 'nationality', 'assists']]
                final_df['assists'] = final_df['assists'].astype(int)
                final_df['player'] = final_df['name']
                final_df = final_df.drop(['name'], axis=1)
                final_df = final_df[['player', 'age', 'nationality', 'assists']]                
                final_df.index = np.arange(1, len(final_df)+1)
                final_df['league'] = 'Bundesliga'
                top_assists_df = final_df  



            ####################################### 3. LA LIGA ##############################################
            if top_assists_options == "La Liga":
                league_id = "140"
                endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/players/topassists"
                query_string = {"season":"2021","league":league_id}
                headers = {
                'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
                'x-rapidapi-key': API_KEY
                }
                response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
                e = response.json()['response']
                df_e = pd.DataFrame(e)
                player_assists_stats_df_e1 = df_e['player'].apply(pd.Series)
                assists_stats_df_e1 = df_e['statistics'].apply(pd.Series)
                assists_stats_df_e1.columns = ['data']
                assists_stats_df_e2=assists_stats_df_e1['data'].apply(pd.Series)
                assists_stats_df_e3=assists_stats_df_e2['goals'].apply(pd.Series)
                df_concat = pd.concat([player_assists_stats_df_e1, assists_stats_df_e3], axis=1)
                final_df = df_concat[['name', 'age', 'nationality', 'assists']]
                final_df['assists'] = final_df['assists'].astype(int)
                final_df['player'] = final_df['name']
                final_df = final_df.drop(['name'], axis=1)
                final_df = final_df[['player', 'age', 'nationality', 'assists']]
                final_df.index = np.arange(1, len(final_df)+1)
                final_df['league'] = 'La Liga'
                top_assists_df = final_df 



            ####################################### 4. SERIE A ##############################################
            if top_assists_options == "Serie A":
                league_id = "135"
                endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/players/topassists"
                query_string = {"season":"2021","league":league_id}
                headers = {
                'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
                'x-rapidapi-key': API_KEY
                }
                response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
                e = response.json()['response']
                df_e = pd.DataFrame(e)
                player_assists_stats_df_e1 = df_e['player'].apply(pd.Series)
                assists_stats_df_e1 = df_e['statistics'].apply(pd.Series)
                assists_stats_df_e2 = assists_stats_df_e1.apply(pd.Series)
                assists_stats_df_e3= assists_stats_df_e2.drop(assists_stats_df_e2.columns[1], axis=1)
                assists_stats_df_e4 = assists_stats_df_e3.apply(pd.Series)
                assists_stats_df_e4.columns = ['data']
                assists_stats_df_e5 = assists_stats_df_e4['data'].apply(pd.Series)
                assists_stats_df_e6=assists_stats_df_e5['goals'].apply(pd.Series)
                df_concat = pd.concat([player_assists_stats_df_e1, assists_stats_df_e6], axis=1)
                final_df = df_concat[['name', 'age', 'nationality', 'assists']]
                final_df['assists'] = final_df['assists'].astype(int)
                final_df['player'] = final_df['name']
                final_df = final_df.drop(['name'], axis=1)
                final_df = final_df[['player', 'age', 'nationality', 'assists']]
                final_df.index = np.arange(1, len(final_df)+1)
                final_df['league'] = 'Serie A'
                top_assists_df = final_df 



            ####################################### 5. LIGUE 1 ##############################################
            if top_assists_options == "Ligue 1":
                league_id = "61"
                endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/players/topassists"
                query_string = {"season":"2021","league":league_id}
                headers = {
                'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
                'x-rapidapi-key': API_KEY
                }
                response = requests.request("GET", endpoint_url, headers=headers, params=query_string)
                e = response.json()['response']
                df_e = pd.DataFrame(e)
                player_assists_stats_df_e1 = df_e['player'].apply(pd.Series)
                assists_stats_df_e1 = df_e['statistics'].apply(pd.Series)
                assists_stats_df_e2 = assists_stats_df_e1.apply(pd.Series)
                assists_stats_df_e3= assists_stats_df_e2.drop(assists_stats_df_e2.columns[1], axis=1)
                assists_stats_df_e4 = assists_stats_df_e3.apply(pd.Series)
                assists_stats_df_e4.columns = ['data']
                assists_stats_df_e5 = assists_stats_df_e4['data'].apply(pd.Series)
                assists_stats_df_e6=assists_stats_df_e5['goals'].apply(pd.Series)
                df_concat = pd.concat([player_assists_stats_df_e1, assists_stats_df_e6], axis=1)
                final_df = df_concat[['name', 'age', 'nationality', 'assists']]
                final_df['assists'] = final_df['assists'].astype(int)
                final_df['player'] = final_df['name']
                final_df = final_df.drop(['name'], axis=1)
                final_df = final_df[['player', 'age', 'nationality', 'assists']]
                final_df.index = np.arange(1, len(final_df)+1)
                final_df['league'] = 'Ligue 1'
                top_assists_df = final_df    

            return top_assists_df    
    
        
        # Set up variables for top assists with functions and corresponding league ids   
        premier_league_top_assists = get_top_assists(league_id = 39)
        bundesliga_top_assists =     get_top_assists(league_id = 78)
        la_liga_top_assists =        get_top_assists(league_id = 140)
        serie_a_top_assists =        get_top_assists(league_id = 135)
        ligue_1_top_assists =        get_top_assists(league_id = 61)

        # Display Premier League top assists this season 
        if top_assists_options == "Premier League":
            st.caption("Premier League Top Assists 2021-22")
            st.dataframe(premier_league_top_assists, width=800, height=600)
        

        # Display Bundesliga top assists this season 
        elif top_assists_options == "Bundesliga":
            st.caption("Bundesliga Top Assists 2021-22 ")
            st.dataframe(bundesliga_top_assists, width=800, height=600)

        # Display La Liga top assists this season 
        elif top_assists_options == "La Liga":
            st.caption("La Liga Top Assists 2021-22 ")
            st.dataframe(la_liga_top_assists, width=800, height=600)
        
        # Display Serie A top assists this season 
        elif top_assists_options == "Serie A":
            st.caption("Serie A Top Assists 2021-22 ")
            st.dataframe(serie_a_top_assists, width=800, height=600)


        # Display Ligue 1 top assists this season 
        elif top_assists_options == "Ligue 1":
            st.caption("Ligue 1 Top Assists 2021-22 ")
            st.dataframe(ligue_1_top_assists, width=800, height=600)

        else:
            st.warning("Top assists currently under construction!!!")

    with columnR:
        lottie_animation = load_animation_via_link("https://assets7.lottiefiles.com/packages/lf20_q3NQef.json")
        st_lottie(lottie_animation, height=650, width=700, key="assist")


if top_assists_options == "Premier League":
    fig = px.bar(premier_league_top_assists, x='player', y='assists',
         # hover_data=['lifeExp', 'gdpPercap'], 
         color='assists',
         labels={'assists':'Total assists'}, height=700)
    st.plotly_chart(fig, use_container_width=True)


if top_assists_options == "Bundesliga":
    fig = px.bar(bundesliga_top_assists, x='player', y='assists',
         # hover_data=['lifeExp', 'gdpPercap'], 
         color='assists',
         labels={'assists':'Total assists'}, height=700)
    st.plotly_chart(fig, use_container_width=True)

if top_assists_options == "La Liga":
    fig = px.bar(la_liga_top_assists, x='player', y='assists',
         # hover_data=['lifeExp', 'gdpPercap'], 
         color='assists',
         labels={'assists':'Total assists '}, height=700)
    st.plotly_chart(fig, use_container_width=True)

if top_assists_options == "Serie A":
    fig = px.bar(serie_a_top_assists, x='player', y='assists',
         # hover_data=['lifeExp', 'gdpPercap'], 
         color='assists',
         labels={'assists':'Total assists '}, height=700)
    st.plotly_chart(fig, use_container_width=True)

if top_assists_options == "Ligue 1":
    fig = px.bar(ligue_1_top_assists, x='player', y='assists',
         # hover_data=['lifeExp', 'gdpPercap'], 
         color='assists',
         labels={'assists':'Total assists '}, height=700)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("****")

st.header("Development Plans :wrench:")
with st.container():
    columnL, columnR = st.columns(2)
    with columnL:
        st.markdown(
            """
        Plans to converting this into an SPA with additional more features will be available in the next release. This tool is quite useful when keeping on top of my favourite teams from each of the 5 largest league competitions in football. Hopefully you find it the same!    
      
        Any suggestions to improving this app is welcome, so express any sentiments you have towards it - reach out to me on:

        * [LinkedIn](https://www.linkedin.com/in/stephen-david-williams-860428123/)
        * [Gmail](mailto:stephenodavidwilliams@gmail.com) 

        
        """)
    with columnR:
        lottie_animation = load_animation_via_link("https://assets3.lottiefiles.com/packages/lf20_ofa3xwo7.json")
        st_lottie(lottie_animation, height=400, width=700, key="ai_robot2")

contact_doc = """

<form action="https://formsubmit.co/stephenodavidwilliams@gmail.com" method="POST">
     <input type="hidden" name="_capcha" value="false">
     <input type="text" name ="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>

"""


with st.container():
    columnL, columnR = st.columns(2)    
    with columnL:
        st.markdown("""
        You can also use the contact form below to reach out to me here: 

        """)
        st.header("Contact Me :email:")
        st.markdown(contact_doc, unsafe_allow_html=True)
    with columnR:
        st.empty()


# Highlight top 4 ranked teams with the colour 'green' 
## Logic = If Rank is less than or equal to 4, colour entire row green

style_contact_doc("style.css")

st.markdown("****")


# League Logos

# Premier League
prem_league_logo = Image.open('images/premier-league-2.png')
prem_league_logo = prem_league_logo.resize((400,160))


bundesliga_logo = Image.open('images/bundesliga-logo-2.png')
bundesliga_logo = bundesliga_logo.resize((400, 200))

la_liga_logo = Image.open('images/LaLiga.svg.png')
la_liga_logo = la_liga_logo.resize((400, 200))

serie_a_logo = Image.open('images/serie_a_logo.png')
serie_a_logo = serie_a_logo.resize((400, 200))

ligue_1_logo = Image.open('images/ligue_1.png')
ligue_1_logo = ligue_1_logo.resize((400, 200))


with st.container():
    columnA, columnB, columnC, columnD, columnE = st.columns(5)
    with columnA:
        st.image(prem_league_logo)
    with columnB:
        st.image(bundesliga_logo)
    with columnC:
        st.image(la_liga_logo)
    with columnD:
        st.image(serie_a_logo)
    with columnE:
        st.image(ligue_1_logo)