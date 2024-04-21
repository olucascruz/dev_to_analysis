import streamlit as st
import pandas as pd
import utils

@st.cache_data
def load_data():
    data = None
    try:
        data = pd.read_csv(utils.get_data_path())
    except FileNotFoundError as err:
        print(err)

    return data
def main():
    st.set_page_config(layout="wide", page_title= "dev.to top week")

    try:
        with open( "style.css" ) as css:
            st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    except Exception as ex:
        print(ex)
        st.write("without css file")
        return

    data_load_state = st.text('Loading data...')

    data = load_data()
    if data is None: return

    # If the article does not have tags, convert 'nan' to an empty string.
    data["tags"] = data["tags"].apply(lambda x: '' if isinstance(x, (int, float)) else x)

    data_load_state.text("")
    col1, col2= st.columns(spec=[0.5,0.5])

    with col1:      
        st.title('Dados - Dev.to top week')
        
        st.markdown("## **Mais reagidos**")
        
        articles_most_reacted = utils.get_articles_most_reacted(data)
        count = 1
        for article in articles_most_reacted["title"]:
            number_reacts = articles_most_reacted[articles_most_reacted["title"] == article]["number_reactions"]
            st.write(f"{count}º {article} - {number_reacts.values[0]} reações")
            count += 1

        tag_counts_articles_most_reacted = utils.count_tag_occurrences(articles_most_reacted["tags"])

        sorted_tags = sorted(tag_counts_articles_most_reacted.items(), key=lambda item: item[1], reverse=True)

        sorted_tags = sorted_tags[:5]
        # Prepare data for the bar chart
        labels = [tag[0] for tag in sorted_tags]

        tags_most_reacted = ""
        for label in labels:
            tags_most_reacted += f"#{label} "

        tags = data["tags"]

        tags = utils.count_tag_occurrences(tags)
        sorted_tags = sorted(tags.items(), key=lambda item: item[1], reverse=True)

        sorted_tags = sorted_tags[0:10]
        # Prepare data for the bar chart
        labels = [tag[0] for tag in sorted_tags]
        sizes = [tag[1] for tag in sorted_tags]

        st.write(f"TAGS: {tags_most_reacted}")
        utils.add_blank_spaces(st, num_spaces=4)
        st.markdown(f"# **Tag com maior frequência:** {labels[0]}")
    
        st.markdown("## **As tags mais frequentes**")

        # Create the bar chart
        utils.plot_bar_chart(st=st, labels=labels, sizes=sizes, title="Tag Distribution", xlabel="Tags", ylabel="Occurrences")
        
        words_list = data["tags"]
        text = ' '.join(words_list)

        utils.plot_wordcloud(st, words=text)
        
    with col2:
        column_minutes_to_read = data["minutes_to_read"]
        mean_minutes_to_read = column_minutes_to_read.mean()

        st.markdown("\n")

        st.markdown(f"## **Média do tempo de leitura:** {round(mean_minutes_to_read)} minutos")
        st.markdown("## **Mais comentados**")
        df_dev_to_sorted_comments = data.sort_values(by='number_comments', ascending=False)
        articles_most_commented = df_dev_to_sorted_comments.head(5)
        
        count = 1
        for article in articles_most_commented["title"]:
            number_comments = articles_most_commented[articles_most_commented["title"] == article]["number_comments"] 
            st.write(f"{count}º {article} - {int(number_comments.values[0])} comentários")
            count += 1
            

        tag_counts_most_commented_articles = utils.count_tag_occurrences(articles_most_commented["tags"])

        sorted_tags = sorted(tag_counts_most_commented_articles.items(), key=lambda item: item[1], reverse=True)

        sorted_tags = sorted_tags[:5]

        tags_most_commented = ""
        labels = [tag[0] for tag in sorted_tags]
        for label in labels:
            tags_most_commented += f"#{label} "

        st.write(f"TAGS: {tags_most_commented}")
        utils.add_blank_spaces(st, num_spaces=6)
        st.markdown("\n")

        st.markdown("## **Palavras mais frequentes nos títulos**")
        # Convert the list to a single string with space-separated words
        words_list = data["title"]
        titles = ' '.join(words_list)
        
        utils.plot_wordcloud(st, words=titles)

if __name__ ==  '__main__':
    main()
