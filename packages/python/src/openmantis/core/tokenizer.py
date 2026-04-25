import json
import math


def estimate_tokens(value):
    '''Estimate token count for a value (roughly 4 chars per token).'''
    if value is None:
        return 0

    if isinstance(value, list):
        return sum(estimate_tokens(item) for item in value)

    if isinstance(value, dict):
        return estimate_tokens(json.dumps(value))

    text = str(value).strip()

    if not text:
        return 0

    return max(1, math.ceil(len(text) / 4))


def count_message_tokens(messages):
    '''Count total estimated tokens across a list of messages.'''
    total = 0
    for message in messages:
        total += estimate_tokens(message.get('role', ''))
        total += estimate_tokens(message.get('content', ''))
    return total
