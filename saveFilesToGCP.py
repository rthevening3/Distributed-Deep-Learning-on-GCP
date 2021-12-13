import glob
from google.cloud import storage
import os

CREDENTIAL_PATH = "/home/rami/Documents/OMSA/CSE6250BigDataforHealthcare/Project/windy-oxide-334905-b9ec2bc89933.json"
LIMIT_FILES = 10000
BUCKET_FOLDER_DIR = 'chexpertcse6250fall2021'

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=CREDENTIAL_PATH


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )


def readUploadRecords():
    
    with open('Project/Files loaded to gcp in rthevening3') as f:
        lines = [l.split(' ')[1] for l in f.readlines()]
    return lines

loadedFiles = readUploadRecords()

j = 1
for root, dirs, files in os.walk('CheXpert-v1.0-small', topdown=False):

    for name in files:
       if name[-4:] == '.jpg':

           source_file_name = os.path.join(root, name)
           destination_blob_name = os.path.join(root, name)
           if source_file_name not in loadedFiles:
               upload_blob(BUCKET_FOLDER_DIR, source_file_name, destination_blob_name)
           j +=1


    for name in dirs:
      if name[-4:] == '.jpg':
           source_file_name = os.path.join(root, name)
           destination_blob_name = os.path.join(root, name)
           if source_file_name not in loadedFiles:
               upload_blob(BUCKET_FOLDER_DIR, source_file_name, destination_blob_name)
           j +=1
    
    if j > 10000:
        break


