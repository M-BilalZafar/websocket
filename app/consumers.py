

from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):
    #methods
    
    def websocket_connet(self,event):
      print('websocket connected....' , event)
      
    
    def websocket_recive(self,event):
        print('websocket recieved....' , event)
        
    def websocket_disconnect(self,event):
        print("websocket disconnect....", event)  