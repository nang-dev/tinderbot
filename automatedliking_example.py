from tinder_api_sms import *;


recs = get_recommendations()["results"];

#print(recs);
i = 1;
for user in recs:
	if i < 30:
		userId = user['_id'];
		print(like(userId));
	i+=1;