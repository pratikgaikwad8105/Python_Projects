from llm_config import llm


class Instagram:
    def __init__(self, post_title, post_type, target_audience, tone, hashtags, word_limit):
        self.post_title = post_title
        self.post_type = post_type
        self.target_audience = target_audience
        self.tone = tone
        self.hashtags = hashtags
        self.word_limit = word_limit

        self.response = llm.invoke(

            f'''
                Generate a Instagram post using the below information. No preamble.

                1) Post Topic: {self.post_title}
                2) Length: {self.word_limit} words
                3) Language: English
                4) Post Type: {self.post_type}  
                5) Target Audience: {self.target_audience}
                6) Tone: {self.tone}  
                7) Hashtags: {self.hashtags}

                The script for the generated post should always be English.
                Please try to focus on length accuracy.
                '''

        )