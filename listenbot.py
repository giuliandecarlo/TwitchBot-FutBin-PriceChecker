from bot import Bot
import futbinSearch
import yaml

config = yaml.safe_load(open('config/config.yml', 'rb'))
CHANNEL=config['CHANNEL']
COMMANDBOT=config['COMMANDBOT']

class ListenBot(Bot):
    def action(self, username, msg):
        if(username==CHANNEL and COMMANDBOT in msg): #only the channel owner can use this command 
            commands=msg.split()
            try:
                searchKey=""
                for word in commands:
                    if(word!=COMMANDBOT):         #all words after COMMANDBOT are searchkeys
                        searchKey=searchKey+" "+word
                answer=futbinSearch.searchPlayer(searchKey)
                self.chat(answer)    #answer is sent as a chat reply
            except:
                self.chat("An error has occurred, please try again")


bot = ListenBot("#"+CHANNEL)
bot.run()
