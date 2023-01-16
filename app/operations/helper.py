# def new_product_stats_helper(current_stats:dict, new_product: dict):
#     current_stats['total_retail'] += (new_product['retail'] * new_product['quantity'])
#     current_stats['total_resell'] += (new_product['resell'] * new_product['quantity']) 
#     current_stats['current_net'] = current_stats['total_resell'] - current_stats['total_retail']
#     current_stats['total_quantity'] += new_product['quantity']

#     if new_product['status'] == 'NOT LISTED':
#         current_stats['amount_not_listed'] += new_product['quantity']
#     elif new_product['status'] == 'LISTED':
#         current_stats['amount_listed'] += new_product['quantity']
#     elif new_product['status'] == 'PACKED':
#         current_stats['amount_packed'] += new_product['quantity']
#     elif new_product['status'] == 'SHIPPED':
#         current_stats['amount_shipped'] += new_product['quantity']


# def delete_product_stats_helper(current_stats:dict, old_product:dict):
#     current_stats['total_retail'] -= (old_product['retail']*old_product['quantity'])
#     current_stats['total_resell'] -= (old_product['resell']*old_product['quantity'])
#     current_stats['current_net'] = current_stats['total_resell'] - current_stats['total_retail'] 
#     current_stats['total_quantity'] -= old_product['quantity']
#     current_stats[f'amount_{old_product["status"].lower().replace(" ","_")}'] -= old_product['quantity']


def new_product_stats_helper(current_stats:dict, new_product: dict):
    current_stats['total_retail'] += (new_product['retail'])
    current_stats['total_resell'] += (new_product['resell']) 
    current_stats['current_net'] = current_stats['total_resell'] - current_stats['total_retail']
    current_stats['total_quantity'] += 1

    if new_product['status'] == 'NOT LISTED':
        current_stats['amount_not_listed'] += 1
    elif new_product['status'] == 'LISTED':
        current_stats['amount_listed'] += 1
    elif new_product['status'] == 'PACKED':
        current_stats['amount_packed'] += 1
    elif new_product['status'] == 'SHIPPED':
        current_stats['amount_shipped'] += 1


def delete_product_stats_helper(current_stats:dict, old_product:dict):
    current_stats['total_retail'] -= (old_product['retail'])
    current_stats['total_resell'] -= (old_product['resell'])
    current_stats['current_net'] = current_stats['total_resell'] - current_stats['total_retail'] 
    current_stats['total_quantity'] -= 1
    current_stats[f'amount_{old_product["status"].lower().replace(" ","_")}'] -= old_product['quantity']