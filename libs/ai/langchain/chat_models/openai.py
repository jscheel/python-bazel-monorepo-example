from langchain.chat_models import ChatOpenAI

# from groove.langchain.decorators import meter_openai_agenerate, meter_openai_generate
from libs.ai.langchain.mixins import MeteredLLMMixin


class MeteredChatOpenAI(MeteredLLMMixin, ChatOpenAI):
    pass


# class MeteredChatOpenAI(ChatOpenAI):
#     """Metered OpenAI chat client. Each call is first checked against the
#     TokenWallet to ensure that the requester has enough tokens to make the call."""

#     # requester_gid: str
#     # wallet: Optional[TokenWallet]

#     def __init__(self, **data):
#         super().__init__(**data)
#         self.wallet = TokenWallet(owner_gid=self.requester_gid)

#     def _reconcile_budget(self, budget: int, spend: int) -> None:
#         difference = budget - spend
#         if difference > 0:
#             self.wallet.deposit(difference)
#         elif difference < 0:
#             # TODO (jscheel): Something went wrong and we spent more than expected.
#             # If this number is way off we should probably log in bugsnag.
#             pass


# MeteredChatOpenAI._generate = meter_openai_generate(MeteredChatOpenAI._generate)
# MeteredChatOpenAI._agenerate = meter_openai_agenerate(MeteredChatOpenAI._agenerate)
