import json
import random

import dataset
from flask import Flask, Response

app = Flask(__name__)

db = dataset.connect()

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
