import os
from flask import Flask, render_template
import pandas as pd
from gensim.utils import simple_preprocess as preprocess
from gensim.models.doc2vec import Doc2Vec

# CSVに基づいてデータフレームを作成
scopes_dataframe = pd.read_csv('scopes_dataframe.csv')

# キーに基づいて出力を得るためにnamesとvisionsのリストを作成する。
names = []
for name in scopes_dataframe['company_name']:
    names.append(name)
visions = []
for vision in scopes_dataframe['scopes']:
    visions.append(vision)

# データフレームを出力
print(scopes_dataframe)
#モデル読み込み
model = Doc2Vec.load('scope.model')
# モデルを評価します。
test_txt = input('prease_visions')
similar_documents = model.docvecs.most_similar([model.infer_vector(preprocess(test_txt))])
# キーを抽出します。
keys = [document[0] for document in similar_documents]

# キーを表示します。
for key in keys:
    # print(scopes_dataframe.loc[key])
    print(key, names[key], ":", visions[key])

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = 'Welcome! Resumate!!'

    return render_template('index.html',

                           message=message)


if __name__ == '__main__':
    app.run(debug=True)
