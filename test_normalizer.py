from app.utils.text_normalizer import TextNormalizer

words = [

    "manage",

    "managed",

    "managing",

    "management",

    "renew",

    "renewed",

    "renewals",

    "customer",

    "customers",

    "account",

    "accounts"

]

for word in words:

    print(
        f"{word:15} -> {TextNormalizer.normalize(word)}"
    )