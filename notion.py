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

    # read, update
    def create_page(self, description, date, status):
        create_url = 'https://api.notion.com/v1/pages'

        data = {
        "parent": { "database_id": self.database_id },
        "properties": {
            "Description": {
                "title": [
                    {
                        "text": {
                            "content": description
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                            "start": date,
                            "end": None
                        }
            },
            "Status": {
                "rich_text": [
                    {
                        "text": {
                            "content": status
                        }
                    }
                ]
            }
        }}

        data = json.dumps(data)
        res = requests.post(create_url, headers=self.headers, data=data)
        print(res.status_code)
        return res