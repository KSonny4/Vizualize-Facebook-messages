import json
from wordcloud import WordCloud
from os import path
import matplotlib.pyplot as plt



#https://stackoverflow.com/questions/50008296/facebook-json-badly-encoded
def parse_obj(obj):
    for key in obj:
        if isinstance(obj[key], str):
            obj[key] = obj[key].encode('latin_1').decode('utf-8')
        elif isinstance(obj[key], list):
            obj[key] = list(map(lambda x: x if type(x) != str else x.encode('latin_1').decode('utf-8'), obj[key]))
        pass
    return obj


def cloud_simple(data):
    d = path.dirname(__file__)
    font_path = path.join(d, 'CenturyGothic.TTF')
    word_cloud = WordCloud(font_path=font_path).generate(data)

    # Display the generated image:
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()






def show_wordcloud(data, title=None):
    d = path.dirname(__file__)
    font_path = path.join(d, 'CenturyGothic.TTF')
    wordcloud = WordCloud(
        font_path=font_path,
        background_color='white',
        stopwords=stopwords,
        max_words=100,
        max_font_size=20,
        scale=3,
        random_state=1  # chosen at random by flipping a coin; it was heads
    ).generate(str(data))


    fig = plt.figure(1, figsize=(24, 24))
    plt.axis('off')
    if title:
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()
    fig.savefig('cloud.png')  # save the figure to file
    plt.close(fig)


# Usage: import your facebook messages in json provided by facebook
# to "json_file" variable and run the program
if __name__ == '__main__':
    json_file = 'demo.json'

    #Stopwords file provided by https://github.com/stopwords-iso/stopwords-cs
    stopwords_file = 'stopwords.json'

    with open(json_file) as f:
        data = json.load(f, object_hook=parse_obj)

    with open(stopwords_file) as f:
        stopwords = json.load(f)


    print('Number of messages: {}'.format(len(data['messages'])))

    list_of_all_words = []
    for msg in data['messages']:
        if 'content' in msg:
            message = msg['content']
            list_of_all_words.extend(message.split())

    print('Number of words: {}'.format(len(list_of_all_words)))


    # filter all diacritics from words
    # letters_only = re.sub("[^a-zA-Z]",  # Search for all non-letters
    #                       " ",  # Replace all non-letters with spaces
    #                       str(list_of_all_words))
    # show_wordcloud(letters_only, 'FB chat')

    show_wordcloud(' '.join(list_of_all_words), 'FB chat')


