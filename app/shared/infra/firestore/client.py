import os
from google.cloud.firestore_v1 import Client
from google.oauth2 import service_account
import googleapiclient.discovery

credentials = service_account.Credentials.from_service_account_file(
  filename=os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
  scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
client = Client(credentials=credentials)
