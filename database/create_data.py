import datetime
import random
from concurrent.futures import ProcessPoolExecutor, as_completed

import dataset

db = dataset.connect()

TEMP = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
# EXECUTOR=ProcessPoolExecutor(max_workers=100)


def demo():

    for i in range(10000):
        db.query(
            f"insert into demo_data (`name`,'create_time`,`update_time`) values({''.join(random.choices(TEMP, k=random.randrange(1,254)))})"
        )


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=20) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = [executor.submit(demo) for i in range(100)]
        for future in as_completed(future_to_url):
            pass
