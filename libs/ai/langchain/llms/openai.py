from langchain.llms.openai import OpenAI
from libs.ai.langchain.mixins import MeteredLLMMixin


class MeteredOpenAI(MeteredLLMMixin, OpenAI):
    pass
