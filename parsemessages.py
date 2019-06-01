from tinder_api_sms import *;
from features import *;
import pprint
import datetime
import string

printer = pprint.PrettyPrinter(indent=4)

#recs = get_recommendations()["results"];
count = "50";
match_dict = all_matches(count);

date = str(datetime.datetime.now()).replace(" ", "");
#print(date);

self_dict = get_self();
selfId = self_dict['_id'];

matches = match_dict["data"]["matches"];

#find last message that we didnt send for each user
for user in matches:
	userId = user['_id'];
	if user['messages']:
		lastMessage = user['messages'][-1];
		if lastMessage['from'] != selfId:
			message = lastMessage['message'];
			printer.pprint(message);

