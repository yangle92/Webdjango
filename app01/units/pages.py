from django.utils.safestring import mark_safe

def page(request,data,num=10):
    '''
    :param request: request
    :param data:  querysets
    :param num:  每一页存放的数据条数
    :return: 
    '''
    if  int(divmod(int(len(data)),num)[1])==0:
        total_page=int(divmod(int(len(data)),num)[0])[0]
    else:
        total_page = int(divmod(int(len(data)),num)[0])+1

    if request.GET.get('page'):
        current_page=int(request.GET.get('page'))
        data = data[(current_page - 1) * num:current_page * num - 1]
        page_str_list = [
            '<li><a href="/list/user/?page=1" aria-label="Previous"><span aria-hidden="true">«</span></a></li>']

        # 这里是
        if current_page -5 <=0 and total_page <=5:
            for i in range(1,total_page+1):
                ele = '<li><a href="/list/user/?page={}">{}</a></li>'.format(i, i)
                page_str_list.append(ele)
        if current_page -5 <=0 and total_page >5 :
            for i in range(1,current_page+5):
                ele = '<li><a href="/list/user/?page={}">{}</a></li>'.format(i, i)
                page_str_list.append(ele)

        for i in range(current_page-5, current_page+5):
            if current_page + 5 >= total_page:
                for i in range(current_page - 5, total_page + 1):
                    ele = '<li><a href="/list/user/?page={}">{}</a></li>'.format(i, i)
                    page_str_list.append(ele)
            ele = '<li><a href="/list/user/?page={}">{}</a></li>'.format(i, i)
            page_str_list.append(ele)
        page_str_list.append('<li><a href="/list/user/?page={{ total_page }}" aria-label="Next"><span aria-hidden="true">»</span></a></li>')
        page_string = mark_safe(''.join(page_str_list))
        return data,page_string,total_page
    else:
        current_page =1
        data = data[(current_page - 1) * num:current_page * num - 1]
        page_str_list = [
            '<li><a href="/list/user/?page=1" aria-label="Previous"><span aria-hidden="true">«</span></a></li>']
        for i in range(1, current_page + 5):
            ele = '<li><a href="/list/user/?page={}">{}</a></li>'.format(i, i)
            page_str_list.append(ele)
        page_str_list.append(
            '<li><a href="/list/user/?page={{ total_page }}" aria-label="Next"><span aria-hidden="true">»</span></a></li>')
        page_string = mark_safe(''.join(page_str_list))
        return data, page_string,total_page





