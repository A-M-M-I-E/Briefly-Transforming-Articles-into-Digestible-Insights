import streamlit as st
import newspaper

st.title('Briefly: Transforming Articles into Digestible Insights')
url=st.text_input('Enter URL' , placeholder='Type URL and enter ')

if url:
    article=newspaper.Article(url)
    article.download()

    article.parse()
    authors=article.authors
    st.write(','.join(authors))

    article.nlp()
    st.subheader('Keywords')
    key=article.keywords
    st.write(', '.join(key))

    

    tab1 ,tab2=st.tabs(['Full text','Summary'])

    

    with tab1:
        article.text

    with tab2:
        st.write(article.summary)