[![Inline docs](https://travis-ci.com/yoyocm/kata-tennis.svg?branch=master)](https://travis-ci.com/yoyocm/kata-tennis.svg?branch=master)

# kata-tennis
http://codingdojo.org/kata/Tennis/

### How to run a tennis match simulation
```console
user@laptop:~$ python main.py
```


### To-do list
- [x] Create Game object
- [x] Create Player object
- [x] Create Score object
- [x] Use faker module to generate fake first and last names
- [ ] Match has to return Player who won or None
- [ ] Define an entity as opponent on a match and player will inherit from this entity (to handle doubles tennis matches)
- [ ] Use Factory design pattern to generate players
- [ ] Implement tests for Game object
- [x] Implement tests for Score object
- [x] Implement tests for Player object
- [x] Run CI on commits
- [ ] Generate requirements.txt file
- [ ] Add attributes in Player object
- [ ] Handle deuce situation
