# LM Evaluation Harness - Our Tasks

This repository contains custom evaluation tasks *Benchmarks in Arabic* for the **LM Evaluation Harness** framework. Follow the steps below to set up and run the tasks.

---

## 1. Clone the Repository
First, clone the repository from GitLab:

```powershell
git clone https://gitlab.leandevclan.com/advanced-analytics/fine-tunning-llm/lm-evaluation-harness/lm-evaluation-harness.git
```

Navigate into the project folder:
```powershell
cd lm-evaluation-harness
```

---

## 2. Install The Requirements
You can use a virtual environment or just install the required dependencies:
```powershell
pip install -r requirements.txt
```

---

## 3. Run the Tasks
To run any task, you should chose a model to try it on, you can use a local model or a model from hugging face.
below are all the tasks with their commands to run it!

```powershell
# PubmedQA_ar
python -m lm_eval --model hf --model_args "pretrained=MODEL_PATH,trust_remote_code=True,device_map=cpu" --tasks pubmedqa_ar --device cpu --batch_size 1 --limit 0.001 --output_path ./results --log_samples

# MedQA_ar
python -m lm_eval --model hf --model_args "pretrained=MODEL_PATH,trust_remote_code=True,device_map=cpu" --tasks medqa_ar --device cpu --batch_size 1 --limit 0.001 --output_path ./results --log_samples

# MedMCQA_ar
python -m lm_eval --model hf --model_args "pretrained=MODEL_PATH,trust_remote_code=True,device_map=cpu" --tasks medmcqa_ar --device cpu --batch_size 1 --limit 0.001 --output_path ./results --log_samples

# MMLU - College Biology (Arabic)
python -m lm_eval --model hf --model_args "pretrained=MODEL_PATH,trust_remote_code=True,device_map=cpu" --tasks mmlu_college_biology_ar --device cpu --batch_size 1 --limit 0.001 --output_path ./mmlu_results --log_samples

# MMLU - Medical Genetics (Arabic)
python -m lm_eval --model hf --model_args "pretrained=MODEL_PATH,trust_remote_code=True,device_map=cpu" --tasks mmlu_medical_genetics_ar --device cpu --batch_size 1 --limit 0.001 --output_path ./results --log_samples

# MMLU - Anatomy (Arabic)
python -m lm_eval --model hf --model_args "pretrained=MODEL_PATH,trust_remote_code=True,device_map=cpu" --tasks mmlu_anatomy_ar --device cpu --batch_size 1 --limit 0.001 --output_path ./results --log_samples

# MMLU - Professional Medicine (Arabic)
python -m lm_eval --model hf --model_args "pretrained=MODEL_PATH,trust_remote_code=True,device_map=cpu" --tasks mmlu_professional_medicine_ar --device cpu --batch_size 1 --limit 0.001 --output_path ./results --log_samples

# MMLU - College Medicine (Arabic)
python -m lm_eval --model hf --model_args "pretrained=MODEL_PATH,trust_remote_code=True,device_map=cpu" --tasks mmlu_college_medicine_ar --device cpu --batch_size 1 --limit 0.001 --output_path ./results --log_samples

# MMLU - Clinical Knowledge (Arabic)
python -m lm_eval --model hf --model_args "pretrained=MODEL_PATH,trust_remote_code=True,device_map=cpu" --tasks mmlu_clinical_knowledge_ar --device cpu --batch_size 1 --limit 0.001 --output_path ./results --log_samples
```

---

## 4. Changing the Model
To run the evaluation on a different model, **replace** `MODEL_PATH` in the commands with:

- A **local model path** (if downloaded):
  ```powershell
  pretrained=path\to\the\model
  ```
- A **Hugging Face model name** (for online models):
  ```powershell
  pretrained=meta-llama/Llama-2-7b-hf
  ```

For example:
```powershell
python -m lm_eval --model hf --model_args "pretrained=meta-llama/Llama-2-7b-hf,trust_remote_code=True,device_map=cpu" --tasks pubmedqa_ar --device cpu --batch_size 1 --limit 0.001 --output_path ./results --log_samples
```
---

## Notes
to see all tasks, run: 
```powershell
python -m lm_eval --tasks list
```

**Explanation of the arguments in the commands**

**1️ --model hf**
This specifies a Hugging Face (hf) model type, if you're using a different model type, change this.

**2️ --model_args**
This argument configures how the model is loaded. The value inside "..." sets up the Hugging Face model.

*Parameters Inside model_args*
- pretrained=MODEL_PATH:
Specifies the path or Hugging Face model name.

- trust_remote_code=True:
Required if the model has custom code that needs to be executed safely.

- device_map=cpu:
I used this because I dont have a gpu, you can switch to GPU usage and replace cpu. it will automatically assign the model to CUDA if available, or CPU if no GPU is detected.

**3️ --tasks TASK_NAME**
Defines which evaluation task to run. Like: --tasks pubmedqa_ar

**4️ --device**
Specifies the computing device for evaluation, could be cpu or CUDA


**5️ --batch_size**
Controls how many samples are processed at once.

**6️ --limit 0.001**
Controls how much of the dataset to use.
0.001 means use only 0.1% of the data.
If you want to use the full dataset, remove this argument.

**7️ --output_path ./results**
Specifies where the evaluation results will be saved.

**8️ --log_samples**
Enables logging of individual samples.


- Contact me, *Meshael Alessa*, if you have any issues setting up.
