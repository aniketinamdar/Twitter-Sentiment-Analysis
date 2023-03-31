from better_profanity import profanity
if __name__ == "__main__":
    dirty_text = "you piece of dog shit."
    print(profanity.contains_profanity(dirty_text))
    custom_badwords = ['gadha', 'loafer', 'nalayak']
    profanity.add_censor_words(custom_badwords)
    dirty_text_2 = "nalayak hai tu"
    print(profanity.contains_profanity(dirty_text_2))
    profanity.load_censor_words(custom_badwords, whitelist_words=['gadha'])
    print(profanity.contains_profanity("gadha hai kya"))
    #limitations
    print(profanity.contains_profanity("you are a piece of shitt"))
