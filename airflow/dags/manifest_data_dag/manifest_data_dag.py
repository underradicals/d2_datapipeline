from airflow.sdk import task, dag


@dag
def manifest_data():
    @task.python
    def download_manifest():
        print("Downloading Manifest")

    @task.python
    def extract_urls_from_manifest():
        print("Extracting")

    @task.python
    def loading_manifest_table_into_minio():
        print("Loading data into MinIO...")

    (
        download_manifest()
        >> extract_urls_from_manifest()
        >> loading_manifest_table_into_minio()
    )


manifest_data()
