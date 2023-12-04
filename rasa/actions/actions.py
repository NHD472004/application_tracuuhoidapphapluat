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
    client = MongoClient("mongodb+srv://admin:admin@cluster0.nn6abqc.mongodb.net/?retryWrites=true&w=majority")
    client.admin.command("ping")

    db = client.todo_db

    collection_name = db["todo_collection"]
    return collection_name



class an_ninh_quoc_gia(Action):

    def name(self) -> Text:
        return "act_an_ninh_quoc_gia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class bao_hiem(Action):

    def name(self) -> Text:
        return "act_bao_hiem"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class buu_chinh_vien_thong(Action):

    def name(self) -> Text:
        return "act_buu_chinh_vien_thong"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class bo_tro_tu_phap(Action):

    def name(self) -> Text:
        return "act_bo_tro_tu_phap"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class canBo_congChuc_vienChuc(Action):

    def name(self) -> Text:
        return "act_canBo_congChuc_vienChuc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class chinh_sach_xa_hoi(Action):

    def name(self) -> Text:
        return "act_chinh_sach_xa_hoi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class cong_nghiep(Action):

    def name(self) -> Text:
        return "act_cong_nghiep"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class giaDinh_treEm_binhDangGioi(Action):

    def name(self) -> Text:
        return "act_giaDinh_treEm_binhDangGioi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class dan_su(Action):

    def name(self) -> Text:
        return "act_dan_su"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class dan_toc(Action):

    def name(self) -> Text:
        return "act_dan_toc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class dat_dai(Action):

    def name(self) -> Text:
        return "act_dat_dai"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []

class doanhNghiep_hopTacXa(Action):

    def name(self) -> Text:
        return "act_doanhNghiep_hopTacXa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class giaoDuc_daoTao(Action):

    def name(self) -> Text:
        return "act_giaoDuc_daoTao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class giao_thong_van_tai(Action):

    def name(self) -> Text:
        return "act_giao_thong_van_tai"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class hanh_chinh_tu_phap(Action):

    def name(self) -> Text:
        return "act_hanh_chinh_tu_phap"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class hinh_su(Action):

    def name(self) -> Text:
        return "act_hinh_su"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class ke_toan_kiem_toan(Action):

    def name(self) -> Text:
        return "act_ke_toan_kiem_toan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class khieu_nai_to_cao(Action):

    def name(self) -> Text:
        return "act_khieu_nai_to_cao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class khoa_hoc_cong_nghe(Action):

    def name(self) -> Text:
        return "act_khoa_hoc_cong_nghe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class lao_dong(Action):

    def name(self) -> Text:
        return "act_lao_dong"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class moi_truong(Action):

    def name(self) -> Text:
        return "act_moi_truong"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class ngan_hang_tien_te(Action):

    def name(self) -> Text:
        return "act_ngan_hang_tien_te"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class ngoai_giao(Action):

    def name(self) -> Text:
        return "act_ngoai_giao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class nong_thon(Action):

    def name(self) -> Text:
        return "act_nong_thon"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class quoc_phong(Action):

    def name(self) -> Text:
        return "act_quoc_phong"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class tai_chinh(Action):

    def name(self) -> Text:
        return "act_tai_chinh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class tai_nguyen(Action):

    def name(self) -> Text:
        return "act_tai_nguyen"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class thi_hanh_an(Action):

    def name(self) -> Text:
        return "act_thi_hanh_an"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class thong_ke(Action):

    def name(self) -> Text:
        return "act_thong_ke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class thue(Action):

    def name(self) -> Text:
        return "act_thue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class ton_giao(Action):

    def name(self) -> Text:
        return "act_ton_giao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class trat_tu_an_toan_xa_hoi(Action):

    def name(self) -> Text:
        return "act_trat_tu_an_toan_xa_hoi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class vanHoa_theThao_duLich(Action):

    def name(self) -> Text:
        return "act_vanHoa_theThao_duLich"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class xayDung_nhaO_doThi(Action):

    def name(self) -> Text:
        return "act_xayDung_nhaO_doThi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class y_te(Action):

    def name(self) -> Text:
        return "act_y_te"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # kết nối với db
        collection = connect_to_mongodb()
        
        document_name = tracker.latest_message.get("text", "")
        result = collection.find_one({"Name": document_name})

        if result:
            content = result.get("Không có nội dung.")
        else:
            content = "Xin lỗi, không tìm thấy thông tin cho tên {document_name}"

        dispatcher.utter_message(text=content)

        return []


class help(Action):

    def name(self) -> Text:
        return "utter_did_that_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="chào bạn, tôi có thể giúp được gì cho bạn")

        return []
