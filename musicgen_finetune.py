import replicate

training = replicate.trainings.create(
  version="sakemin/musicgen-fine-tuner:b1ec6490e57013463006e928abc7acd8d623fe3e8321d3092e1231bf006898b1",
  input={
    "dataset_path":"https://github.com/rohansahai/musicgen_experiments/raw/main/all_mp3s.zip",
    "epochs":5,
    "updates_per_epoch":100,
    "model_version":"medium",
    "lr": .01,
  },
  destination="rohansahai/musicgen-mango-tuner"
)

print(training)