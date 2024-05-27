
import time
import sys
import vertexai
from vertexai.preview.tuning import sft

# TODO(developer): Update and un-comment below lines
# project_id = "PROJECT_ID"

vertexai.init(project=project_id, location="us-central1")
# bucket = "gs://bucket-name"
bucket = sys.argv[1]


sft_tuning_job = sft.train(
    source_model="gemini-1.0-pro-002",
    train_dataset=bucket
)

# Polling for job completion
while not sft_tuning_job.has_ended:
    time.sleep(60)
    sft_tuning_job.refresh()

print(sft_tuning_job.tuned_model_name)
print(sft_tuning_job.tuned_model_endpoint_name)
print(sft_tuning_job.experiment)