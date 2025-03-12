import os

import tqdm
import requests

from sqlalchemy.orm import Session

from . import EMAIL, ENGINE, NAME, models


SEC_COMPANY_TICKERS_URL = os.environ.get("SEC_COMPANY_TICKERS_URL", "")


def download():
    with Session(ENGINE) as session:
        session.query(models.Ticker).delete()

        response = requests.get(
            SEC_COMPANY_TICKERS_URL,
            headers={"User-Agent": f"{NAME} {EMAIL}"},
        )

        tickers = response.json().values()
        tickers = [models.Ticker(**ticker) for ticker in tqdm.tqdm(tickers)]
        session.add_all(tickers)
        session.commit()
