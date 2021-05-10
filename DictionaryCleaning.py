from RegularExpression import cleanText


class DictionaryCleaning:

    def clean_dictionary(self, twitter_dict):
        for key in twitter_dict.keys():
            if type(twitter_dict.get(key)) == str and (key != 'created_at' and key != 'DATE'):
                twitter_dict[key] = cleanText(twitter_dict.get(key))

            elif type(twitter_dict.get(key)) == dict:
                self.clean_dictionary(twitter_dict.get(key))
