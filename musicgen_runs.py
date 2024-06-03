import replicate
# model = "meta/musicgen:671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb"
model = "rohansahai/musicgen-mango-tuner:848c49e279280f7a9d003d4695f277a828cdde769ce317f581dad5f665bd35a9" # 3 epochs, version 1
# model = "rohansahai/musicgen-mango-tuner:fe52bc6a7bd85a6e58455c0c2e69cc4075e04cdeb725b74f4d92de8fa80167bb" # 20 epochs, version 2
output = replicate.run(
    model,
    input={
        "prompt": "An indie-soul funk song in the style of Sally Mango.",
        "duration": 16,
    }
)
print(output)

