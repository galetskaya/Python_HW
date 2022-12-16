#Creates a dict from list
def convert_to_dict(data):
    with open(data, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        lst2 = []
        for each in lines:
            str = each.replace('\n', '')
            lst2.append(str)
            
    def convert(lst):
        res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
        return res_dct
            
    return(convert(lst2))