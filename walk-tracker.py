import os
from dotenv import load_dotenv

from stravaio import strava_oauth2
from stravaio import StravaIO


load_dotenv()

# run this to get a browser w/ oauth flow
STRAVA_CLIENT_ID = os.environ['STRAVA_CLIENT_ID']
STRAVA_CLIENT_SECRET= os.environ['STRAVA_CLIENT_SECRET']
STRAVA_ACCESS_TOKEN= os.environ['STRAVA_ACCESS_TOKEN']

# go to https://www.strava.com/oauth/authorize?client_id=[clientId]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read_all
# replace clientId, see the code in the query params of the url, that's the short lived access token
# then post to get the oath token: 
# curl -X POST https://www.strava.com/api/v3/oauth/token \
#           -d client_id=ReplaceWithClientID \
#             -d client_secret=ReplaceWithClientSecret \
#               -d code=ReplaceWithCode \
#                 -d grant_type=authorization_code
# OR:
# ret = strava_oauth2(client_id=STRAVA_CLIENT_ID, client_secret=STRAVA_CLIENT_SECRET)

client = StravaIO(access_token=STRAVA_ACCESS_TOKEN)

athlete = client.get_logged_in_athlete().to_dict()

print(athlete['id'])

def get_live_activities_and_store():
    # Get list of athletes activities since a given date (after) given in a human friendly format.
    # Kudos to [Maya: Datetimes for Humans(TM)](https://github.com/kennethreitz/maya)
    # Returns a list of [Strava SummaryActivity](https://developers.strava.com/docs/reference/#api-models-SummaryActivity) objects
    list_activities = client.get_logged_in_athlete_activities(after='2018-01-01')
    
    # Obvious use - store all activities locally
    for a in list_activities:
        activity = client.get_activity_by_id(a.id)
        activity.store_locally()
        

# get_live_activities_and_store()   
# 
# # List local activities (returns a generator of JSON friendly dicts)
activities = client.local_activities(athlete_id=73427769) # athlete['id'])

# for activity in activities:
    # print(activity['map']['polyline'])
    # print(activity)
 
print('done')
