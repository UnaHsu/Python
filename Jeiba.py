import jieba
#pip install jieba

 # jieba.cut 為斷詞, cut_all=True 為全模式, cut_all=False 為精確模式
seg_list = jieba.cut("今天天氣很好", cut_all=True)
print("Full Mode: " + "，".join(seg_list))  # 全模式方式
print("===================")
