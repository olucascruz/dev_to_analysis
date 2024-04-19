from botcity.web import WebBot, Browser, By

def devto_scraping_data(bot:WebBot):
    list_dict_stories=[]
    stories = bot.find_elements("crayons-story", By.CLASS_NAME)
    for story in stories:
        story_dict = {}
        if story.get_attribute("data-content-user-id"):
            feed_id = story.get_attribute("data-feed-content-id")

            title = story.find_element_by_tag_name("a").get_attribute("innerHTML")

            title = title.replace("amp;", "")
            number_reactions = story.find_element_by_class_name("aggregate_reactions_counter").get_attribute("innerHTML")
            for char in number_reactions:
                if not char.isdigit():
                    number_reactions = number_reactions.replace(char, "")


            number_comments = story.find_element_by_class_name('crayons-story__details').find_elements_by_tag_name("a")[1].text
            
            for char in number_comments:
                if not char.isdigit():
                    number_comments = number_comments.replace(char, "")

            div_with_tags = story.find_element_by_class_name("crayons-story__tags")
            tags = div_with_tags.find_elements_by_tag_name("a")
            
            list_tags= []

            for tag in tags:
                text = tag.text[2:]
                list_tags.append(text)
            
            time_to_read = story.find_element_by_tag_name("small").text[:-9]


            story_dict["id"]= feed_id
            story_dict["title"] = title
            story_dict["number_reactions"] = number_reactions
            story_dict["number_comments"] = number_comments
            story_dict["tags"] = list_tags
            story_dict["minutes_to_read"] = time_to_read


            list_dict_stories.append(story_dict)
    return list_dict_stories