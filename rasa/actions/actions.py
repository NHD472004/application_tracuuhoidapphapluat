# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from typing import Any, Text, Dict, List
from pymongo import MongoClient

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# kết nôi với database
def connect_to_mongodb():
    client = MongoClient("mongodb://localhost:27017")
    client.admin.command("ping")

    db = client.phapDien

    return db


class bao_hiem(Action):

    def name(self) -> Text:
        return "act_bao_hiem"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        collection = connect_to_mongodb()
        chi_muc_db = collection["chi_muc_bao_hiem"]

        name_ques = tracker.get_slot("luat")
        

        query = {"$text": {"$search": name_ques}}
        projection = {"score": {"$meta": "textScore"}}

        results = chi_muc_db.find(query, projection).sort([("score", {"$meta": "textScore"})]).limit(1)

        for result in results:
            dispatcher.utter_message(text=f"{result['Name']} \n {result['Content']}")
                    

        return []
