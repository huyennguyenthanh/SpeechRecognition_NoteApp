import json
import requests





SECRET_KEY = "secret_Kq3dHOm0c7hq0E6SXWESdpnRFE6FHzFBaJVMbzcPYLL"
NOTION_DATABSE_ID = "c5484bb45aba4fa3ae14b8319c3434f6"

class NotionClient:

    def __init__(self, token, database_id) -> None:
        self.database_id = database_id

        self.headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
            "Notion-Version": "2021-08-16"
        }

    def readDatabase(databaseId, headers):
        readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

        res = requests.request("POST", readUrl, headers=headers)
        data = res.json()
        print(res.status_code)
        # print(res.text)

        with open('./db.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)