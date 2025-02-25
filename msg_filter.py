def filter_message(commit):
    if b"fake commit" in commit.message:
        return b"Updated mission logs"
    return commit.message
