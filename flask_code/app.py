import json
import random

import os
import dataset
from flask import Flask, Response

app = Flask(__name__)

DATABASE_URL = f"mysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:3306/demo"
db = dataset.connect(DATABASE_URL, engine_kwargs={"pool_size": 10000})

TEMP = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"


@app.route("/demo", methods=["GET"])
def demo_code():
    return Response(
        response=json.dumps(
            list(
                db.query(
                    f"select * from demo_data where name='{''.join(random.choices(TEMP, k=random.randrange(1, 254)))}'"
                )
            )
        ),
        status=200,
        content_type="application/json",
    )


if __name__ == "__main__":
    app.run(debug=True)
