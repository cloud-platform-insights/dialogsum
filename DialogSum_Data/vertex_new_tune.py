
import time
import sys
import vertexai
from vertexai.preview.tuning import sft

# TODO(developer): Update and un-comment below lines
project_id = sys.argv[1]
# bucket = "gs://bucket-name"
gcs_train_dataset = sys.argv[2]

vertexai.init(project=project_id, location="us-central1")

sft_tuning_job = sft.train(
    source_model="gemini-1.0-pro-002",
    train_dataset=gcs_train_dataset,
    # The following parameters are optional
    validation_dataset="gs://cloud-samples-data/ai-platform/generative_ai/sft_validation_data.jsonl",
    epochs=4,
    # epoch_count
    # adapter_size
    learning_rate_multiplier=1.0,
    tuned_model_display_name="tuned_gemini_pro",
)

# Polling for job completion
while not sft_tuning_job.has_ended:
    time.sleep(60)
    sft_tuning_job.refresh()

print(sft_tuning_job.tuned_model_name)
print(sft_tuning_job.tuned_model_endpoint_name)
print(sft_tuning_job.experiment)