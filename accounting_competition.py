# accounting test
import financial_fund as ff
import csv

def accounting_task(stock_list):
    # load stock list
    stock_symbols = []
    with open(stock_list, 'r+') as of:
        lines = of.readlines()
        for line in lines:
            line = line.strip()
            if line != '':
                stock_symbols.append(line)

    # (NI-cfo)/rev
    stock_result = {}
    fund_hl = ff.fundamentals()
    for symbol in stock_symbols:
        TTM_NI = fund_hl.get_net_income(symbol)
        TTM_CFO = fund_hl.get_operating_cash_flow(symbol)
        TTM_Rev = fund_hl.get_rev(symbol)


        if TTM_Rev != None and TTM_NI != None and TTM_CFO != None:
            stock_result[symbol] = []
            if len(TTM_Rev) == len(TTM_NI) and len(TTM_NI) == len(TTM_CFO):
                print(TTM_Rev)
                print(TTM_CFO)
                for key, val in TTM_Rev.items():
                    #print(TTM_Rev[key])
                    #print(TTM_CFO[key])
                    #print(TTM_NI[key])
                    #print(key)
                    try:
                        if TTM_Rev[key] != '' and TTM_CFO[key] != '' and TTM_NI[key] != '' and TTM_Rev[key] != '0':
                            ratio = (float(TTM_NI[key]) - float(TTM_CFO[key])) / float(TTM_Rev[key])
                    except KeyError:
                        continue
                    except ZeroDivisionError:
                        continue
                    else:
                        stock_result[symbol].append(ratio)
                        print(ratio)

    w = csv.writer(open("/home/pwu/github/Financial-Modeling-Prep-API/finance_nyse_result.csv","w+"), delimiter=',')
    for key, val in stock_result.items():
        input_list = []
        input_list.append(key)
        for item in val:
            input_list.append(round(item,2))
        print(input_list)
        w.writerow(input_list)
    # find the max ratio
    res = max(stock_result, key = lambda x: stock_result.get(x))
    print(res, "'s ratio = ", stock_result[res])


if __name__ == '__main__':
    file = "/home/pwu/github/Financial-Modeling-Prep-API/nyse_list.txt"
    accounting_task(file)