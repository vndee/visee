def parse_meta_data(doc):
    nd = dict()
    nd['domain'] = doc['domain']
    nd['link'] = doc['link']
    nd['title'] = doc['title']
    nd['price'] = doc['price']
    nd['description'] = doc['description']
    nd['rating_point'] = doc['rating_point']
    nd['rating_count'] = doc['rating_count']
    return nd