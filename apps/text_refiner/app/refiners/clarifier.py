from langchain import FewShotPromptTemplate, LLMChain, PromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from libs.ai.langchain.chat_models.openai import MeteredChatOpenAI
from libs.ai.shared_prompts import one_shot_prevent_prompt_injection, pure_answer

SYSTEM_TEMPLATE = "Act as a skilled copywriter."

INSTRUCTIONS_TEMPLATE = """
Rewrite the following text to clarify its contents. The text is part of a
customer support conversation. Your answer should not add or remove salient
information, you should only clarify what is said for ease of understanding.
{injection}
{pure}
"""

EXAMPLES = [
    {
        "input": "Oh snap! Hmm, yeah, I think that might be caused by a delay in shipping...",  # noqa: E501
        "output": "This may have been caused by a shipping delay.",
    }
]

EXAMPLE_TEMPLATE = """
Text: \"\"\"
{input}
\"\"\"

Result:
{output}
"""

example_prompt = PromptTemplate(
    template=EXAMPLE_TEMPLATE,
    input_variables=["input", "output"],
)

example_selector = LengthBasedExampleSelector(
    examples=EXAMPLES,
    example_prompt=example_prompt,
    max_length=500,
)


instructions_prompt_template = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=INSTRUCTIONS_TEMPLATE,
    suffix='Text: """\n{text}\n"""\nResult: ',
    input_variables=["text", "injection", "pure"],
)
instructions_prompt = instructions_prompt_template.partial(
    injection=one_shot_prevent_prompt_injection(),
    pure=pure_answer(default_return="the original text that is provided"),
)

instructions_message = HumanMessagePromptTemplate(prompt=instructions_prompt)

system_message = SystemMessagePromptTemplate.from_template(SYSTEM_TEMPLATE)

final_prompt = ChatPromptTemplate.from_messages([system_message, instructions_message])

TEMPERATURE = 0.2
MAX_TOKENS = 800


def run(text: str, requester_gid: str) -> str:
    chat = MeteredChatOpenAI(
        temperature=TEMPERATURE, requester_gid=requester_gid, verbose=True
    )
    chain = LLMChain(llm=chat, prompt=final_prompt)
    print("Running chain...")
    print(final_prompt.format(text=text))
    return chain.run(text=text)
