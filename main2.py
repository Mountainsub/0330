import pandas as pd
import numpy as np
import time 
import sys
import os
import random
import math
import datetime
from request.rakuten_rss import ind, rss , rss2 
from lib.ddeclient import DDEClient
from price_logger import ClientHolder 
from multiprocessing import Process
def ind():
	indexes = pd.read_csv("TOPIX_weight_jp.csv",encoding="sjis")

	indexes["コード"] = pd.to_numeric(indexes["コード"], errors='coerce')


	indexes_code = indexes["コード"].astype(int)
	
	for i,j in enumerate(indexes_code):
		indexes_code[i] = str(j) + ".T"
	indexes_code = np.array(indexes_code)
	indexes_code = indexes_code.flatten()

	for i,j in indexes.iterrows():
		# % を除去
		indexes.at[i, "TOPIXに占める個別銘柄のウェイト"] = indexes.loc[i, "TOPIXに占める個別銘柄のウェイト"]
	return [indexes_code, indexes]


def code_s(k):
	array = []
	weights = []
	count = 0
	
	
	# 以下csvファイルを都合いいようにエディット

	inde = ind()
	indexes_code, indexes = inde[0], inde[1] 
	
	# ddeを取得、格納、ウエイトをかけて計算
	
	for i,j in enumerate(indexes_code, start = k): 
		count += 1
		
		c = indexes["コード"][i]
		w = indexes["TOPIXに占める個別銘柄のウェイト"][i]
		weights.append(w)
		array.append(str(int(c))+ ".T")
		
		if count >= 126:
			break 
	return [array, weights]


def calculation(dde_ware, indexes_weight, num):
    calc = rss2("現在値", dde_ware, indexes_weight)
    return calc 

def notFirststep(holder):
    p = holder.get_prices()
    x = holder.calc(p, code_s(int(args[1]))[1])
    print(x)
    if KeyboardInterrupt :
        print(x)
    t2 = time.time()

    print("time:", t2 - t1)


if __name__ == '__main__':
    args = sys.argv # コマンドライン引数として開始地点のインデックスを数字で入力する
    
    count = 0
    
    global_counter = 0
    
    
    holder = ClientHolder(int(args[1]), code_s(int(args[1]))[0], code_s(int(args[1]))[1])
    firststep = True
    while True:
        if True:
            try:
                holder.get_prices_forever()
            except Exception as e:
                raise Exception(e)
                
        
    


        


        