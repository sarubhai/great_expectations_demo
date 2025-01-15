import great_expectations as gx
from great_expectations.core.expectation_configuration import ExpectationConfiguration
from great_expectations.checkpoint import Checkpoint

# Version
# print(gx.__version__)

# Data Context
context_root_dir = "./"
# context = gx.get_context()
context = gx.get_context(context_root_dir=context_root_dir)
# print(context)


# Data Source
datasource = context.sources.add_pandas_filesystem(
    name="gx_ds_local_fs",
    base_directory="./data"
)
# datasource = context.datasources["gx_ds_local_fs"]
# print(datasource)


# Data Asset
asset = datasource.add_csv_asset(
    name="gx_asset_csv_trip",
    batching_regex=r"yellow_tripdata_sample_(?P<year>\d{4})-(?P<month>\d{2}).csv",
    order_by=["year", "month"],
)

# Batch
# batch_request = asset.build_batch_request(options={"year": "2019", "month": "02"})
batch_request = asset.build_batch_request(options={"year": "2019"})
# options = asset.batch_request_options
# print(options)
batches = asset.get_batch_list_from_batch_request(batch_request)
for batch in batches:
    print(batch.batch_spec)



# Expectation Suite
suite = context.add_expectation_suite(expectation_suite_name="gx_expectation_suite_trip")

# expectation_configuration_1 = ExpectationConfiguration(
#     expectation_type="expect_column_values_to_not_be_null",
#     kwargs={
#         "column": "pickup_datetime",
#         "mostly": 1.0,
#     }
# )
# suite.add_expectation(
#     expectation_configuration=expectation_configuration_1
# )
# expectation_configuration_2 = ExpectationConfiguration(
#     expectation_type="expect_column_values_to_not_be_null",
#     kwargs={
#         "column": "vendor_id",
#         "mostly": 1.0,
#     }
# )
# suite.add_expectation(
#     expectation_configuration=expectation_configuration_2
# )
# context.save_expectation_suite(expectation_suite=suite)
# print(context.list_expectation_suite_names())


# Validator
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name="gx_expectation_suite_trip",
)
print(validator.head())

validator.expect_column_values_to_not_be_null(column="pickup_datetime")
validator.expect_column_values_to_not_be_null(column="vendor_id")
validator.save_expectation_suite(discard_failed_expectations=False)


# expectation_validation_result = validator.expect_column_values_to_not_be_null(column="vendor_id")
# print(expectation_validation_result)


# Checkpoint
# checkpoint = context.add_or_update_checkpoint(
#     name="gx_checkpoint_trip",
#     validations=[
#         {
#             "batch_request": batch_request,
#             "expectation_suite_name": "gx_expectation_suite_trip",
#         },
#     ],
# )


checkpoint = context.add_or_update_checkpoint(
    name="gx_checkpoint_trip",
    run_name_template="gx-run-trip-%Y%m%d-%H%M%S",
    expectation_suite_name = "gx_expectation_suite_trip",
    batch_request = batch_request,
    action_list=[
        {
            "name": "store_validation_result",
            "action": {"class_name": "StoreValidationResultAction"},
        },
        {
            "name": "update_data_docs", 
            "action": {"class_name": "UpdateDataDocsAction"}
        },
    ],
)



# retrieved_checkpoint = context.get_checkpoint(name="gx_checkpoint_trip")
checkpoint_result = checkpoint.run()
# print(checkpoint_result)



# Build Data Docs
context.build_data_docs()
context.open_data_docs()


context = context.convert_to_file_context()
print(context)
