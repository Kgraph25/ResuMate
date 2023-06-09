import pandas as pd
from gensim.utils import simple_preprocess as preprocess
from gensim.models.doc2vec import Doc2Vec
import MeCab


def resumate_model(heart):
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
    # モデル読み込み
    model = Doc2Vec.load('scope.model')

    # 形態素解析器をインスタンス化し解析
    test_txt = heart
    word_list = mecab_by_wakati(test_txt)
    # モデルで評価
    similar_documents = model.docvecs.most_similar([model.infer_vector(word_list)])
    # キーを抽出します。
    keys = [document[0] for document in similar_documents]

    # キーを表示します。
    return keys[0], names[keys[0]], visions[keys[0]]


#    for key in keys:
#        # print(scopes_dataframe.loc[key])
#        # print(key, names[key], ":", visions[key])
#        return key, names[key], visions[key]
def mecab_by_wakati(test_txt):
    # インスタンス化
    tagger = MeCab.Tagger('-Owakati')
    tagger.parse('')
    node = tagger.parseToNode(test_txt)
    word_list = []
    while node:
        pos = node.feature.split(",")[0]
        if pos in ["名詞", "動詞", "形容詞", "形容動詞"]:  # 対象とする品詞
            word = node.surface
            word_list.append(word)
        node = node.next
    return word_list


if __name__ == "__main__":
    text = input('例題')
    resumate_model(text)
