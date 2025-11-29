CS6223 Course Project
=====================================================

This project builds on top of https://github.com/eth-sri/type-constrained-code-generation

### Setup

To install the package, we recommend setting up a conda environment using NVIDIA GPUs.

```bash
git clone https://github.com/eth-sri/type-constrained-code-generation.git
cd type-constrained-code-generation  
conda create -n typesafe_llm python=3.11
conda activate typesafe_llm

# for LLM inference
# set up torch
conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia -y
# install flash-attention
pip install flash-attn==2.7.3 --no-build-isolation

# install package
pip install -e .
```

If you only want to use the parser and do not want to sample from a language model, you can skip the installation of `torch` and `flash-attention`.


## Reproducing experiments

### Requirements

Further the Gemma 2 model family requires accepting an EULA. Please create a huggingface account and visit the model websites to accept the EULA.
- https://huggingface.co/google/gemma-2b-it
- https://huggingface.co/google/gemma-9b-it
- https://huggingface.co/google/gemma-27b-it

You will later be requested for a Hugginface Access Token. Log in with the account with which you accepted the EULA and visit [the Access Token page](https://huggingface.co/settings/tokens) to generate an access token: https://huggingface.co/settings/tokens

### Setup

Follow the installation instructions to install conda and all dependencies for the experiments:

```bash
bash ./setup_conda.sh
# Restart your shell
bash ./setup_env.sh 
# NOTE: Some models are guarded on huggingface, so you will need to visit their model page, accept the EULA and enter the huggingface Access Token to your account when prompted. See section "Requirements" for more details.
```

> Important note: Before running the experiments, you need to download the models and datasets used for the experiments.

We provide a script to download the required dataset and models for our experiments. This script must be run before starting the experiments.
You may specify models to download by passing the `models` paramater.

```bash
python3 experiments/main/download_models.py --models google/gemma-2-2b-it,google/gemma-2-9b-it
```

To download all required models and datasets, run the following command:

```bash
python3 experiments/main/download_models.py
```


### Reproducing Results

Our method

```bash
CUDA_VISIBLE_DEVICES=0,1 python3 experiments/main/run_experiments_syn_tran.py --models google/gemma-2-2b-it,google/gemma-2-9b-it --tasks synth,translate --subsets humaneval --trials 2
```

Baseline

Same command. Modify the following locations in the project:\
- In `experiments/main/run_experiments_syn_tran.py`, comment out lines 191-196, uncomment lines 198-203
- In `experiments/main/inference_multiple_repair_with_trials.py`, comment out lines 269-273, uncomment lines 275-276
- In `typesafe_llm/sampling.py`, comment out lines 283-322, run `python -m build`

Data Analysis

Use script `data_analysis.py`, modify line 3 to analyze different files.