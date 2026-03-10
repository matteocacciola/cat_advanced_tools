# C.A.T. — Cat Advanced Tools

[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=F4F4F5&style=for-the-badge&logo=cheshire_cat_black)](https://)

This plugin gives you fast access to a few core settings.

Currently supported settings:
- prompt prefix: change the instruction prompt that tells the language model how to behave;
- declarative memory k: change the number of declarative memories retrieved and used in the context;
- declarative memory threshold: change the minimum similarity score that declarative memories should have to be used as context;
- language of responses: change the language that the Cat will use to answer. Note that this does not affect the language of the prompt prefix, which is always in English. Hence, you can use this setting to make the Cat answer in a different language than English while keeping the prompt prefix in English.
  Possible values are:
  - "English"
  - "French"
  - "German"
  - "Italian"
  - "Spanish"
  - "Russian"
  - "Chinese"
  - "Japanese"
  - "Korean"
  - "Human"
  Use the "Human" value to let the Cat decide on the language.