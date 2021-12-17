from google.cloud import firestore

db = firestore.Client()

# Add a new doc in collection
def add_document(collection, data):
    data = db.collection(collection).add(data)

    return data[1].id


def get_ticker(ticker):
    doc_ref = db.collection('symbol').document(ticker)

    doc = doc_ref.get()

    return doc.to_dict()


def get_collection(collection):
    docs = db.collection(collection).stream()
    data = {}
    for doc in docs:
        data[doc.id] = doc.to_dict()

    return data


def get_document(collection, document):
    data = db.collection(collection).document(document).get().to_dict()
    return data


def set_document(collection, document, data):
    db.collection(collection).document(document).set(data)


def update_document(collection, document, data):
    db.collection(collection).document(document).update(data)


def delete_document(collection, document):
    db.collection(collection).document(document).delete()


def set_field(collection, document, key, value):
    db.collection(collection).document(document).update({key: value})


def delete_field(collection, document, key):
    db.collection(collection).document(document).update({key: firestore.DELETE_FIELD})


def get_orders_by_status(status):
    orders = db.collection(u'orders').where(u'status', u'==', status).stream()

    data = {}

    for order in orders:
        data[order.id] = order.to_dict()

    return data

