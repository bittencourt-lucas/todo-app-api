from google.cloud import datastore
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
client = datastore.Client(credentials=credentials)
