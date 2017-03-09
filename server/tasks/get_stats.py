import requests

CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']

def retrieve_and_store_user_stats_data():
  """Retrieve stats data and store it in GCS for later processing."""
    # TODO(justinlulejian): HTTP request the file from F@H website.
    stats_data_file = request.files.get('file')

    if not uploaded_file:
        return 'No file uploaded.', 400

    # Create a Cloud Storage client.
    gcs = storage.Client()

    # Get the bucket that the file will be uploaded to.
    bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)

    # Create a new blob and upload the file's content.
    blob = bucket.blob(uploaded_file.filename)

    blob.upload_from_string(
        uploaded_file.read(),
        content_type=uploaded_file.content_type
    )

    # The public URL can be used to directly access the uploaded file via HTTP.
    return blob.public_url
