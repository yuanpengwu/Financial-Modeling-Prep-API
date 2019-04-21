#
import urllib3
import json


class json_loader(object):
    def __init__(self, url):
        self._url = url
    def get_json(self):
        http = urllib3.PoolManager()
        req =  http.request('GET', self._url)
        return json.loads(req.data.decode('utf-8'))

class fundamentals(object):
    '''
    based on https://github.com/yuanpengwu/Financial-Modeling-Prep-API.git
    '''
    def __init__(self):

        # from income statement
        self._total_rev = {}
        self._net_income = {}

        # from cash flow
        self._operating_cash_flow = {}

        # utility



    def get_income_statement(self, symbol):
        # base url
        base_url = "https://financialmodelingprep.com/api/financials/income-statement/"
        if symbol == None:
            return None
        else:
            req_url = base_url+symbol+"?datatype=json"

        json_ld = json_loader(req_url)
        json_content = json_ld.get_json()

        return json_content

    def get_cash_flow(self, symbol):
        # base url
        base_url = "https://financialmodelingprep.com/api/financials/cash-flow-statement/"
        if symbol == None:
            return None
        else:
            req_url = base_url + symbol + "?datatype=json"

        json_ld = json_loader(req_url)
        json_content = json_ld.get_json()

        return json_content

    def get_balance_sheet(self, symbol):
        # base url
        base_url = "https://financialmodelingprep.com/api/financials/balance-sheet-statement/"
        if symbol == None:
            return None
        else:
            req_url = base_url + symbol + "?datatype=json"

        json_ld = json_loader(req_url)
        json_content = json_ld.get_json()

        return json_content

    #####################################

    def get_rev(self, symbol):
        # get rev from income statement
        content = self.get_income_statement(symbol)
        try:
            rev = content[symbol]["Revenue"]
        except KeyError:
            return None
        else:
            self._total_rev[symbol] = rev
        return rev
    def get_net_income(self,symbol):
        # get net income form income statement
        content = self.get_income_statement(symbol)
        print(content)
        try:
            NI = content[symbol]["Net income"]
        except KeyError:
            return None
        else:
            self._net_income[symbol] = NI
        return NI
    def get_operating_cash_flow(self, symbol):
        # get operating cash flow form cash flow
        content = self.get_cash_flow(symbol)
        try:
            cfo = content[symbol]["Operating cash flow"]
        except KeyError:
            return None
        else:
            self._operating_cash_flow[symbol] = cfo
        return cfo





if __name__ == '__main__':
    test_stock = 'AAPL'
    fund_test = fundamentals()
    json_result = fund_test.get_income_statement(test_stock)
    print(json_result)
    json_result1 = fund_test.get_cash_flow(test_stock)
    print(json_result1)
    print(fund_test.get_operating_cash_flow(test_stock)['TTM'])
    print(fund_test.get_net_income(test_stock))