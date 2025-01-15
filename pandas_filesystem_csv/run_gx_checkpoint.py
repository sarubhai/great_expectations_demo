import great_expectations as gx

# Version
# print(gx.__version__)

# Data Context
context = gx.get_context()

# Run Checkpoint
context.run_checkpoint(checkpoint_name="gx_checkpoint_trip")
context.open_data_docs()
