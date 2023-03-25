from google.cloud.firestore_admin_v1 import FirestoreAdminClient
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
client = datastore.FirestoreAdminClient(credentials=credentials)
