def solution(today, terms, privacies):
    answer = []
    privacy_info = []
    term_info = []
    key_list = []
    value_list = []
    pri_crawl_date_list = []
    
    for term in terms:
        term_info = term.split()
        key_list.append(term_info[0])
        value_list.append(term_info[1])
    term_dic = dict(zip(key_list,value_list))
    
    for num, privacy in enumerate(privacies):
        privacy_info = privacy.split()
        pri_crawl_date = privacy_info[0]
        term_type = privacy_info[1]
        term_crawl_date = term_dic.get(term_type)
        
        pri_crawl_date_list = pri_crawl_date.split('.')
        yy = pri_crawl_date_list[0]
        mm = pri_crawl_date_list[1]
        dd = pri_crawl_date_list[2]

        add_mm = int(mm) + int(term_crawl_date)
        if  add_mm > 9:
            if add_mm % 12 < 10:
                if add_mm % 12 == 0:
                    new_mm = '12'
                    new_yy = (add_mm // 12) - 1
                else:
                    new_mm = '0' + str(add_mm % 12)
                    new_yy = add_mm // 12
            else:
                new_mm = str(add_mm % 12)
                new_yy = add_mm // 12
            add_date = str(int(yy) + new_yy) + '.' + new_mm + '.' + dd
        else:
            new_mm = '0' + str(add_mm)
            add_date = str(yy + '.' + new_mm + '.' + dd)
        
        if today >= add_date:
            answer.append(num+1)
        
    return answer