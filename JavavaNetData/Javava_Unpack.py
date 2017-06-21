import struct
from .info import MessageNames,GameStatus,GameCommand
from .base_protocal import Javava_Base_Proto,wordpack

class Task_Game_New(Javava_Base_Proto):
    def __init__(self,send_id,recv_id):
        super().__init__(MessageNames.Task_Game_New,send_id,recv_id)
    def unpack(self,data_no_header):
        #data_no_header=self.stripheader(data)
        paramtuple=struct.unpack('>32s32s4H',data_no_header[:72])
        taillength=len(data_no_header[72:])
        paramlist=list(paramtuple)
        paramlist.extend(struct.unpack(str(taillength)+'s',data_no_header[72:]))                        #length and other data
        return paramlist
    def pack(self,game_id,game_duration,game_rate1,game_rate2,game_rate3,game_other,task_rmtpurl):
        if not isinstance(task_rmtpurl,bytes):
            task_rmtpurl=task_rmtpurl.encode('utf-8')
        headerdata = self.packheader()
        id_data = self.pack_id()
        task_rmtpurl_len=str(len(task_rmtpurl))+'s'
        content_data = struct.pack('>32s32s4H'+task_rmtpurl_len, game_id,game_duration,game_rate1,game_rate2,game_rate3,game_other,task_rmtpurl)
        content_length = self.check_datalen(content_data+id_data)
        if content_length:
            return b''.join([headerdata, wordpack(content_length), id_data,content_data])
        raise ValueError("Status not right or Message too long")

class Task_GameStatus_Control(Javava_Base_Proto):
    def __init__(self,send_id,recv_id):
        super().__init__(MessageNames.Task_GameStatus_Control,send_id,recv_id)
    def unpack(self,data_no_header):
        paramtuple = struct.unpack('>32sB', data_no_header)
        paramlist = list(paramtuple)
        return paramlist
    def pack(self,game_id,game_status):
        headerdata=self.packheader()
        id_data = self.pack_id()
        if game_status==GameStatus.Done:
            content_data=struct.pack(">32sB",game_id,game_status)
            content_length=self.check_datalen(content_data+id_data)
            if content_length:
                return b''.join([headerdata,wordpack(content_length),id_data,content_data])
        raise ValueError("Status not right or Message too long")



class Task_Game_Query(Javava_Base_Proto):
    def __init__(self,send_id,recv_id):
        super().__init__(MessageNames.Task_GameResult_Query,send_id,recv_id)
    def unpack(self,data_no_header):
        #data_no_header=self.stripheader(data)
        paramtuple=struct.unpack('>32s',data_no_header)
        paramlist=list(paramtuple)
        return paramlist
    def pack(self,game_id):
        if not isinstance(game_id,bytes):
            game_id=game_id.encode('utf-8')
        headerdata = self.packheader()
        id_data = self.pack_id()
        content_data = struct.pack(">32s", game_id)
        content_length = self.check_datalen(content_data+id_data)
        if content_length:
            return b''.join([headerdata, wordpack(content_length), id_data,content_data])
        raise ValueError(" Game id  too long")

class Task_Game_Command(Javava_Base_Proto):
    def __init__(self,send_id,recv_id):
        super().__init__(MessageNames.Task_Game_Command,send_id,recv_id)
    def unpack(self,data_no_header):
        paramtuple = struct.unpack('>32sIB', data_no_header)
        paramlist = list(paramtuple)
        return paramlist
    def pack(self,game_id,game_timestamp,game_command):
        headerdata=self.packheader()
        id_data = self.pack_id()
        if game_command in GameCommand.getcommand():
            content_data=struct.pack('>32sIB',game_id,game_timestamp,game_command)
            content_length = self.check_datalen(content_data+id_data)
            if content_length:
                return b''.join([headerdata, wordpack(content_length), id_data,content_data])
        raise ValueError("Status not right or Message too long")
