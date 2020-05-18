## THIS IS OUR PROGRAM WHICH WILL BE USED TO MAKE API CALLS AND CREATE DATA FOR THE APPLICATION

from stravalib.client import Client
import json
import time
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import swagger_client
from swagger_client.rest import ApiException


def main(args):
    client = Client()
    client_id = 40291
    client_secret = '174e515190aa81a04416b147a32937ea5a86c672'
    with open("stravtoken.json", "r") as stravtoken:
        tokendict = json.load(stravtoken)
    access_token = tokendict["access_token"]
    refresh_token1 = tokendict["refresh_token"]
    expires_at = tokendict['expires_at']  
    if time.time() > tokendict['expires_at']:
            refresh_response = client.refresh_access_token(client_id, client_secret, refresh_token1)
            access_token = refresh_response['access_token']
            refresh_token1 = refresh_response['refresh_token']
            expires_at = refresh_response['expires_at']
            with open("stravtoken.json", "w+") as json_file:
                json.dump(refresh_response, json_file)
                
    client.access_token=access_token
    client.refresh_access_token= refresh_token1
    client.token_expires_at = expires_at

    api_instance = swagger_client.ActivitiesApi()
    api_instance.api_client.configuration.access_token = access_token
    list_acts2 = []
    for x in range (1,20):
        try:
            api_response = api_instance.get_logged_in_athlete_activities(page=x, per_page=100)
            acts = str(api_response)
            acts = acts.replace("\'", "\"")
            acts = acts.replace("None", "0")
            acts = acts.replace("False", "0")
            acts = acts.replace("True", "1")
            acts = json.loads(acts)
            for each in acts:
                if isinstance(each['start_latlng'],list):
                    list_acts2.append([each['id'],each['distance']/1609.344,each['moving_time'],
                                each['elapsed_time']-each['moving_time'],each['total_elevation_gain'],
                                each['total_elevation_gain']/each['moving_time'],each['start_latlng'][0],
                                       each['start_latlng'][1],each['map']['summary_polyline']])
        except ApiException as e:
            print(x)

    acts_df = pd.DataFrame(list_acts2)
    acts_df.columns = ['Run ID', 'Distance', 'Time', 'Resting Time','Elevation Gain',
                       'Elevation Grade','Start Latitude','Start Longitude','Polyline']

    acts_df_clean = acts_df.drop(acts_df[acts_df['Start Latitude']>34].index)
    acts_df_clean = acts_df_clean.drop(acts_df[acts_df['Start Latitude']<33].index).reset_index()

    clust_df = acts_df_clean.filter(['Distance','Elevation Grade'], axis=1)
    clust_df['Distance'] = clust_df['Distance'].apply(lambda x: pow(x*150,.35))
    clust_df['Elevation Grade'] = clust_df['Elevation Grade'].apply(lambda x: pow(x*150,.8))
    kmeans = KMeans(n_clusters=6,random_state=3425)
    kmeans.fit(clust_df)
    labels = pd.Series(kmeans.predict(clust_df),name='Difficulty').to_frame().reset_index()
    clust_df = pd.concat([clust_df, labels], axis=1, sort=False)
    acts_df_clean = pd.concat([acts_df_clean, labels], axis=1, sort=False)
    maps = {0:2,1:1,2:0,3:2,4:0,5:1}
    acts_df_clean['Difficulty'] = acts_df_clean['Difficulty'].apply(lambda x: maps[x])

    acts_df_clean.to_csv('activities.csv', index=False)

if __name__=="__main__":
    import sys
    main(sys.argv)