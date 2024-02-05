if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data.columns = (data.columns
                    .str.replace(' ', '_')
                    .str.lower()
                    )
    print(f"Preprocessings: rows with zero passengers {data['passenger_count'].isin([0]).sum()}")
    print(f"Preprocessings: rows with trip distances equal zero {data['trip_distance'].isin([0]).sum()}")

    data['lpep_pickup_date'] = data.lpep_pickup_datetime.dt.date
    data['lpep_dropoff_date'] = data.lpep_dropoff_datetime.dt.date

    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rows with zero passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rows with trip distance equal zero'
    assert output['vendorid'].isin([1,2]).sum() == len(output), 'There are rows with vendorid different to 1 or 2'