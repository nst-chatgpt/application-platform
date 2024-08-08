import streamlit as st
from langchain_openai import AzureChatOpenAI
from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain
from langchain_text_splitters import CharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain_community.document_loaders import TextLoader

st.title('簡易アプリ運用基盤R&D')

st.write('アプリ基盤')

st.header('検証アプリ')

# ボタンを作成
if st.button('クリックしてください'):
    print('ボタンをクリック')
    st.write('ボタンがクリックされました!')
else:
    st.write('ボタンがまだクリックされていません。')

# llm = AzureChatOpenAI(
#     openai_api_version = '2024-06-01',
#     azure_deployment = 'gpt-4o',
#     temperature = 0
# )

# Map
# with st.expander('prompt'):
#     map_template = st.text_area(
#         "map_template",
#         '''以下は一連のトランスクリプションの一部です
#         {docs}
#         この文書をベースとして、発言者、時刻、発言内容をまとめてください。
#         同一の発言者の連続した発言内容は１つにまとめてください。
#         えーと、あの、などの発言は省略してください。
#         発言内容の意味や順番が変わらないように注意して少しだけ要約してください。
#         有用な回答:'''
#     )
#     # Reduce
#     reduce_template = st.text_area(
#         "reduce_template",
#         '''以下は議事メモのセットです:
#         {docs}
#         これらを受け取り、議事録を作成してください。
#         - 日時、参加者、議事内容、重要な決定事項、ToDoを書いてください。
#         - 以下の例に従って文章の終わりにかっこ書きで発言者を書いてください。
#             - ダメな例）岡村誠が、このアプリの課題について説明しました。
#             - 良い例）このアプリの課題について説明（岡村）
#         - 重要な決定事項、ToDoはリスト形式で書いてください。
#         - ToDoはかっこ書きで対応者を書いてください。
#         有用な回答:'''
#     )

# map_prompt = PromptTemplate.from_template(map_template)
# map_chain = LLMChain(llm=llm, prompt=map_prompt)

# reduce_prompt = PromptTemplate.from_template(reduce_template)
# reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)

# combine_documents_chain = StuffDocumentsChain(
#     llm_chain=reduce_chain, document_variable_name='docs'
# )

# collapse_documents_chain = StuffDocumentsChain(
#     llm_chain=map_chain, document_variable_name='docs'
# )

# # マッピングされた文書を結合し、繰り返しreduceを実施
# reduce_documents_chain = ReduceDocumentsChain(
#     # これが呼び出される最終的なチェーンです
#     combine_documents_chain=combine_documents_chain,
#     # 文書が`StuffDocumentsChain`のコンテキストを超える場合
#     collapse_documents_chain=collapse_documents_chain,
#     # ドキュメントをまとめる最大のトークン数
#     token_max=8000,
# )

# # 文書にチェーンをマッピングし、結果を結合することで統合
# map_reduce_chain = MapReduceDocumentsChain(
#     # Mapチェーン
#     llm_chain=map_chain,
#     # Reduceチェーン
#     reduce_documents_chain=reduce_documents_chain,
#     # llm_chainへの入力となる文書の変数名
#     document_variable_name='docs',
#     # アウトプットにmapステップの結果を含める
#     return_intermediate_steps=True,
# )

# text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#     chunk_size=2000, chunk_overlap=0
# )

# file = st.file_uploader('テキストファイルをアップロードしてください', type=['txt'])
# if st.button('要約'):
#     if file is None:
#         st.write('ファイルがアップロードされていません')
#         st.stop()
#     else:
#         # uploadされたファイル名でファイルを保存
#         org_path = f'/data/{file.name}'
#         with open(org_path, 'wb') as f:
#             f.write(file.read())
#         docs = TextLoader(org_path).load()
#         result = map_reduce_chain.invoke(docs)
#         summary_file_name = f'{file.name.split(".")[0]}_summary.txt'
#         summary_path = f'/data/{summary_file_name}'
#         print(result)
#         intermediate_steps = '\n'.join(result['intermediate_steps'])
#         result_text = f"""
#         {result['output_text']}


#         --intermediate_steps--
        
        
#         {intermediate_steps}
#         """
#         with open(summary_path, 'w') as f:
#             f.write(result_text)
#         st.header('結果')
#         st.write(result_text)
#         st.download_button('ダウンロード', result_text, summary_file_name)
