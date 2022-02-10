"""Grabs Data from TD Ameritrade API and Parses into a pandas Dataframe"""
import pandas as pd
import yaml
from td.option_chain import OptionChain
from td.client import TDClient


class TDData():

    def __init__(self, conf_path):
        self.conf_path = conf_path
        self.session = self.createSession()

    def createSession(self) -> object:
        with open(self.conf_path) as file:
            cfg = yaml.safe_load(file)
            cons_key = cfg['paths']['CONSUMER_KEY']
            redirect = cfg['paths']['REDIRECT']
            cred_path = cfg['paths']['JSON_PATH']
            self.session = TDClient(
                client_id=cons_key,
                redirect_uri=redirect,
                credentials_path=cred_path
            )
        self.session.login()
        return self.session

    def parseOptData(self:dict, put=False):
        par_data = []
        if put:
          dataMap = self['putExpDateMap']
        else:
          dataMap = self['callExpDateMap']

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

    def parseStockData(self:dict):
        par_stock_data = []
        for data in self['candles']:
            par_stock_data.append({
                'datetime': data['datetime'],
                'high': data['high'],
                'low': data['low'],
                'open': data['open'],
                'volume':data['volume'],
                'close': data['close']
            })
        return par_stock_data

    def formatData(par_data: list):
        return pd.DataFrame(par_data)

    def grabOptData(self,symbol):
        return self.session.get_options_chain((OptionChain(symbol=symbol)))


    #def grabStockData(self, symbol: str, period_type:str = None, period: str = None, start_date:str = None,
                      #end_date:str = None, frequency_type: str = None, frequency: str = None, extended_hours: bool = True,):

        #return self.session.get_price_history(symbol,period_type,period,start_date,end_date,frequency_type,frequency,extended_hours)



def main():
    client = TDData(conf_path='../../configs/config.yaml')
    data_pull = client.grabOptData(symbol='AAPL')
    parsed_data = TDData.parseOptData(data_pull)
    formatted_data = TDData.formatData(parsed_data)
    print(formatted_data)

if __name__ == '__main__':
    main()
