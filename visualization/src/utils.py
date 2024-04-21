import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def count_tag_occurrences(tags):
    """
    Counts the occurrences of individual tags in a list of tags.

    Args:
        tags (list): A list containing tags.

    Returns:
        dict: A dictionary containing the counts of individual tags.
    """
    tags_counts = {}
    for tag in tags:
        if type(tag) != str:
            continue
        split_tags = tag.split(", ")

        for individual_tag  in split_tags:
            tags_counts[individual_tag] = tags_counts.get(individual_tag, 0) + 1
    return tags_counts

def count_occurrences_with_threshold(word_counts, threshold)-> dict:
    """
    Counts occurrences of words/tags with a frequency above a specified threshold.
    Words/tags with frequency below the threshold are grouped under the "other" category.

    Args:
        word_counts (dict): A dictionary containing word/tag counts.
        threshold (int): The frequency threshold. Words/tags with counts below this threshold
                         will be grouped under the "other" category.

    Returns:
        dict: A dictionary containing word/tag counts above the threshold, grouped by word/tag.
              Words/tags with counts below the threshold are grouped under the "other" category.
    """

    # Group tags with frequency below the threshold under the "other" category
    other_count = 0
    filtered_tags = {}
    for tag, count in word_counts.items():
        if count >= threshold:
            filtered_tags[tag] = count
        else:
            other_count += count

    if other_count > 0:
        filtered_tags['other'] = other_count

    return filtered_tags

def get_articles_most_reacted(data, n=5):
    """
    Returns the top N articles with the highest number of reactions from the provided DataFrame.

    Args:
        data (DataFrame): The DataFrame containing the articles data.
        n (int, optional): The number of top articles to return. Defaults to 5.

    Returns:
        DataFrame: A DataFrame containing the top N articles with the highest number of reactions.
    """
    df_dev_to_sorted_reactions = data.sort_values(by='number_reactions', ascending=False)
    articles_most_reacted = df_dev_to_sorted_reactions.head(n)
    return articles_most_reacted   

def get_data_path() -> str:
    """
    Returns the path to the 'data.csv' file within the 'bot_dev_to' directory.

    Returns:
        str: The full path to the 'data.csv' file.
    """
    src_dir = os.path.dirname(__file__)
    data_path = os.path.join(src_dir, "..", "..", "bot_dev_to", "results", "data.csv")
    return data_path


def plot_bar_chart(st, labels, sizes, title, xlabel = "Items", ylabel="Occurrences") -> None:
    """
    Plots a bar chart.

    Args:
        st (streamlit): Streamlit object for displaying the chart.
        labels (list): List of labels for the bars.
        sizes (list): List of sizes (values) for the bars.
        title (str): Title of the chart.
        xlabel (str): Label for the x-axis
        ylabel (str): Label for the y-axis

    """
    # Create the bar chart
    figure = plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, sizes, color='skyblue')

    # Add labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Add value labels on top of bars
    for bar, size in zip(bars, sizes):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(size), ha='center', va='bottom')

    # Display the chart
    plt.tight_layout()
    st.pyplot(figure)


def plot_wordcloud(st, words:str)-> None:
    """
    Plots a wordcloud.

    Args:
        st (streamlit): Streamlit object for displaying the chart.
        words (str): Str with all words separate for ' ' (white space) 
    """
    # Generate a word cloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(words)

    # Plot the word cloud
    figure = plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(figure)

def add_blank_spaces(st, num_spaces=4):
    """
    Adds blank spaces to the Streamlit app.

    Args:
        st (streamlit): Streamlit object for adding elements to the app.
        num_spaces (int, optional): The number of blank spaces to add. Defaults to 4.
    """
    for _ in range(num_spaces):
        st.markdown('##')