import os

def count_tag_occurrences(tags):
    tags_counts = {}
    for tag in tags:
        if type(tag) != str:
            continue
        split_tags = tag.split(", ")

        for individual_tag  in split_tags:
            tags_counts[individual_tag] = tags_counts.get(individual_tag, 0) + 1
    return tags_counts

def count_occurrences_with_threshold(word_counts, threshold):
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
        df_dev_to_sorted_reactions = data.sort_values(by='number_reactions', ascending=False)
        articles_most_reacted = df_dev_to_sorted_reactions.head(n)
        return articles_most_reacted   

def get_data_path():
    src_dir = os.path.dirname(__file__)
    data_path = os.path.join(src_dir, "..", "..", "bot_dev_to", "results", "data.csv")
    return data_path