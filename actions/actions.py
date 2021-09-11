# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa.shared.core.trackers import DialogueStateTracker, EventVerbosity
import requests
import json
import logging
logger = logging.getLogger(__name__)

#
#
class ActionGreet(Action):
#
     def name(self) -> Text:
         return "greet"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
         dispatcher.utter_message(text="Hey! How are you?")
#
         return []

class ActionCheer_up(Action):
#
     def name(self) -> Text:
         return "cheer_up"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
         dispatcher.utter_message(text="Here is something to cheer you up:")
#
         return []
     
class ActionHappy(Action):
#
     def name(self) -> Text:
         return "happy"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
         dispatcher.utter_message(text="Great, carry on!")
#
         return []
     
class ActionDidHelp(Action):
#
     def name(self) -> Text:
         return "did_that_help"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
         dispatcher.utter_message(text="Did that help you?")
#
         return []
     
        
class ActionBye(Action):
#
     def name(self) -> Text:
         return "action_goodbye"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
         dispatcher.utter_message(text="Bye!")
#
         return []

class ActionBot(Action):
#
     def name(self) -> Text:
         return "action_iamabot"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
         dispatcher.utter_message(text="I am a bot, powered by Ruan Donino.")
         
#
         return []

class ActionNLGBot(Action):
#
     def name(self) -> Text:
         return "action-nlg"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         data = {}
         pos = 0
         for event in tracker.events:    
             if event.get("text"):
                 #logger.debug(event.get("text"))
                 data[pos] = event.get("text")
                 logger.debug(data)
                 pos = pos+1
         
         json_data = json.dumps(data)
         logger.debug(json_data)
         #tracker_state = tracker.current_state()
         payload = data
         logger.debug(payload)
         #string_json= '{"tracker":' + json.dumps(tracker_state)+ '}'
         #parsed = json.loads(string_json)
         #print(json.dumps(parsed, indent=4))
         # Create a new resource
         response = requests.post('https://nlgdonexp-vc5xcezzwa-uc.a.run.app/chatbot', json = payload)
#
         
         dispatcher.utter_message(text= response.json()["text"])
#
         return []
