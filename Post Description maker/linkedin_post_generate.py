from llm_config import llm


class Linkedin:
    def __init__(self, post_content, purpose, target_audience, tone, word_limit):
        self.post_content = post_content
        self.purpose = purpose
        self.target_audience = target_audience
        self.tone = tone
        self.word_limit = word_limit

        self.response = llm.invoke(

            f'''
                Generate a LinkedIn post using the below information. No preamble.
        
                1) Post Topic: {self.post_content}
                2) Length: {self.word_limit} words
                3) Language: English
                4) Purpose: {self.purpose}  
                5) Target Audience: {self.target_audience}
                6) Tone: {self.tone}  
                
                The script for the generated post should always be English.
                Please try to focus on length accuracy.
                '''

        )