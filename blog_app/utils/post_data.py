from faker import Faker
import random


def get_post_data():
    fake = Faker()
    title = (
        f"{fake.catch_phrase()} {random.choice(['Tips', 'Tricks', 'Guide', 'Ideas'])}"
    )
    content = fake.text(
        max_nb_chars=1000
    )  # Generates random text up to 1000 characters

    return {
        "title": title,
        "content": content,
        "num_words": len(content.split()),
    }
