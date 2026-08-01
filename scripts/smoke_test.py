import sys
sys.path.insert(0, "src")
from provider import get_provider

provider = get_provider()
answer = provider.complete(
    system="You are a concise statistics tutor.",
    user="In one sentence, what's the difference between a t-test and a z-test?",
)
print(answer)
