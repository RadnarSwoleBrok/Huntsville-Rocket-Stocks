"""Grabs Data from TD Ameritrade API and Parses into a pandas Dataframe"""

import pandas as pd
import yaml
from td.option_chain import OptionChain
from td.client import TDClient

def createSession():
    with open('../../configs/config.yaml') as file:
        cfg = yaml.safe_load(file)
        session = TDClient(
            client_id=cfg['paths']['CONSUMER_KEY'],
            redirect_uri=cfg['paths']['REDIRECT'],
            credentials_path=cfg['paths']['JSON_PATH']
        )
    session.login()
    return session

def grabOptData(session, symbol):
    options=session.get_options_chain(OptionChain(symbol=symbol))
    return options

def parseData(data:dict, put=False):
    par_data = []
    if put:
      dataMap = data['putExpDateMap']
    else:
      dataMap = data['callDateExpMap']

    for expDate, option in dataMap.items():
        for strike, put_data in option.items():
            put_data = put_data[0]
            par_data.append({
                    'expiration_date': expDate,
                    'strike': strike,
                    'ask_price': put_data['ask'],
                    'bid_price': put_data['bid'],
                    'mid_price': (put_data['bid'] + put_data['ask']) / 2
                })
    return par_data

def formatData(par_data):
    return pd.DataFrame(par_data)

def main():
    return formatData(parseData(grabOptData(createSession(),'AAPL'), True))

if __name__ == '__main__':
    print(main())
    #print(os.getcwd())
