import nlpcloud
class NLPclass:

    api_key = "Your_API_KEY"
    
    def ner(self,para,entity):
        client = nlpcloud.Client("gpt-oss-120b", NLPclass.api_key, gpu=True)
        response=client.entities(para,searched_entity=entity)
        result_lst = response['entities']
        str = ''
        for result_dict in result_lst:
            str = str + result_dict['text'] + '\n'
        return str
    
    def sentiment_analysis(self,text):
        client = nlpcloud.Client("gpt-oss-120b",NLPclass.api_key, gpu=True)
        response = client.sentiment(text,target="NLP Cloud")
        result_lst = response['scored_labels']
        str=''
        for result_dict in result_lst:
            str += result_dict['label'] 
        return str
    
    def title_gen(self,text):
        client = nlpcloud.Client("t5-base-en-generate-headline", NLPclass.api_key, gpu=False)
        response = client.summarization(text)
        return response['summary_text']
    

    