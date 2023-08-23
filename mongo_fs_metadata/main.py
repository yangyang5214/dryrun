from pymongo import MongoClient
from gridfs import GridFS


def main():
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['demo']
    fs = GridFS(db)

    # 存储文件和元数据
    metadata = {
        'title': 'beer',
        'tags': ['json', 'document'],
        'author': 'John Doe'
    }

    with fs.new_file(filename='sample.json', metadata=metadata) as f:
        f.write(b'{"key": "value"}')

    query = {'metadata.tags': 'json'}
    cursor = db.fs.files.find(query)

    for document in cursor:
        print(document)

    query = {'metadata.title': 'xxx'}
    cursor = db.fs.files.find(query)

    for document in cursor:
        print(document)


if __name__ == '__main__':
    main()
