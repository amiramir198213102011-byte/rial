USERS = {}

def get_user(uid: int):
    if uid not in USERS:
        USERS[uid] = {"balance": 0, "nfts": []}
    return USERS[uid]
