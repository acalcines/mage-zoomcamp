import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/mystic-cable-406415-ea44d9f6c5ba.json'

bucket_name = 'mage-zoomcamp-acalcines'
project_id = 'mystic-cable-406415'

table_name = 'green_taxi_data'

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols = ['lpep_pickup_date'],
        filesystem = gcs
    )
    


