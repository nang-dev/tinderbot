from tinder_api_sms import *;
from features import *;
import pprint
import datetime
import string
import dialogflow
import os   
from google.api_core.exceptions import InvalidArgument
from twilio.rest import Client

account_sid = '#'
auth_token = '#'
client = Client(account_sid, auth_token)

DIALOGFLOW_PROJECT_ID = '#'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
GOOGLE_APPLICATION_CREDENTIALS = 'C:\\Users\\natha\\Documents\\TinderAPI\\Tinder\\#.json'

	
credential_path = "C:\\Users\\natha\\Documents\\TinderAPI\\Tinder\\#.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def MLtext(message):
	text_to_be_analyzed = message;

	session_client = dialogflow.SessionsClient()
	session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

	text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
	query_input = dialogflow.types.QueryInput(text=text_input)
	try:
	    response = session_client.detect_intent(session=session, query_input=query_input)
	except InvalidArgument:
	    raise
	#print("Query text:", response.query_result.query_text)
	#print("Detected intent:", response.query_result.intent.display_name)
	#print("Detected intent confidence:", response.query_result.intent_detection_confidence)
	#print("Fulfillment text:", response.query_result.fulfillment_text)
	#print("\n");

	return response.query_result.fulfillment_text;

def twilioMsg(name, pic, message):
	message = client.messages \
                .create(
                     body = name + " " + message,
                     from_='+14082157063',
                     media_url = pic,
                     to = '+14088911891'
                 )


	print(message.sid)


printer = pprint.PrettyPrinter(indent=4)

#recs = get_recommendations()["results"];
count = "50";
match_dict = all_matches(count);

date = str(datetime.datetime.now()).replace(" ", "");
#print(date);

self_dict = get_self();
selfId = self_dict['_id'];

matches = match_dict["data"]["matches"];

i = 0;
#find last message that we didnt send for each user
for user in matches:
	i+=1;
	if i == 1:
		userId = user['_id'];
		if user['messages']:
			lastMessage = user['messages'][-1];
			if lastMessage['from'] != selfId:
				message = lastMessage['message'];
				reply = MLtext(message);
				#print(reply)
				if "hangout request" in reply:
					name = user['person']['name'];
					pic = user['person']['photos'][0]['processedFiles'][0]['url'];
					twilioMsg(name, pic, reply);

				if reply:
					#send_msg(userId, reply);
					print("hi");
					name = user['person']['name'];
					pic = user['person']['photos'][0]['processedFiles'][0]['url'];

					#testing purposes
					reply = "wants to hangout tomorrow at 5pm. Would you like to?"
					twilioMsg(name, pic, reply);
