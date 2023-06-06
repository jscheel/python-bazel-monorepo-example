from langchain import FewShotPromptTemplate, LLMChain, PromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from enum import Enum

from libs.ai.langchain.chat_models.openai import MeteredChatOpenAI
from libs.ai.shared_prompts import one_shot_prevent_prompt_injection, pure_answer


class Tone(Enum):
    UNKNOWN = None
    FORMAL = "formal"
    CASUAL = "casual"


EXAMPLES = {}

EXAMPLES[Tone.FORMAL] = [
    {
        "text": "Hope to hear from you soon!",
        "result": "I look forward to hearing from you soon.",
    },
]

EXAMPLES[Tone.CASUAL] = [
    {
        "text": "Thank you for contacting us.",
        "result": "Thanks for reaching out!",
    },
]

EXAMPLE_TEMPLATE = """
    Example Text: \"\"\"
    {text}
    \"\"\"

    Example Result:
    {result}
"""


SYSTEM_TEMPLATE = "Act as a skilled copywriter."

INSTRUCTIONS_TEMPLATE = """
    Rewrite the following text in a more {tone} tone. The text is part of a customer
    support conversation. Your answer should not add or remove salient information, you
    should only modify the tone of what is said. {injection} {pure}
"""

TEMPERATURE = 0.2


def run(text: str, tone: Tone, requester_gid: str) -> str:
    if tone == Tone.UNKNOWN:
        return text

    chat = MeteredChatOpenAI(temperature=TEMPERATURE, requester_gid=requester_gid)
    system_message = SystemMessagePromptTemplate.from_template(SYSTEM_TEMPLATE)

    example_prompt = PromptTemplate(
        template=EXAMPLE_TEMPLATE,
        input_variables=["text", "result"],
    )

    example_selector = LengthBasedExampleSelector(
        examples=EXAMPLES[tone],
        example_prompt=example_prompt,
        max_length=200,
    )

    instructions_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=INSTRUCTIONS_TEMPLATE,
        suffix='Text: """\n{text}\n"""\nResult: ',
        input_variables=["text", "tone", "injection", "pure"],
    )

    instructions_prompt = instructions_prompt.partial(
        injection=one_shot_prevent_prompt_injection(),
        pure=pure_answer(default_return="the original text that is provided"),
    )

    instructions_message = HumanMessagePromptTemplate(prompt=instructions_prompt)

    final_prompt = ChatPromptTemplate.from_messages(
        [system_message, instructions_message]
    )

    chain = LLMChain(llm=chat, prompt=final_prompt)
    return chain.run(text=text, tone=tone.value)
