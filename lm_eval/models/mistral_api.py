import os
import requests
from lm_eval.base import LM
from lm_eval import utils

class MistralAPIModel(LM):
    def __init__(self, model='mistral-large-latest', api_key=None, **kwargs):
        super().__init__()
        self.model = model
        self.api_key = api_key or os.getenv("MISTRAL_API_KEY")
        self.api_url = "https://api.mistral.ai/v1/chat/completions"

    def _chat_request(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0,
            "top_p": 1,
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()

    def loglikelihood(self, requests):
        # Not supported in Mistral chat endpoint
        return [(-float("inf"), False) for _ in requests]

    def loglikelihood_rolling(self, requests):
        return [(-float("inf")) for _ in requests]

    def generate_until(self, requests):
        generations = []
        for request in requests:
            prompt, until = request
            output = self._chat_request(prompt)
            generations.append(output)
        return generations

    def greedy_until(self, requests):
        return self.generate_until(requests)
