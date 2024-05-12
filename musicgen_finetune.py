import replicate

training = replicate.trainings.create(
    version="sakemin/musicgen-fine-tuner:b1ec6490e57013463006e928abc7acd8d623fe3e8321d3092e1231bf006898b1",
  input={
    "dataset_path":"./Homemade.zip",
    "one_same_description":"Music in the style of Sally Mango, an indie soul bound with a touch of pop, jazz, rnb, and rock.",
    "epochs":3,
    "updates_per_epoch":100,
    "model_version":"medium",
  },
  destination="rohansahai/musicgen-mango-tuner"
)

print(training)