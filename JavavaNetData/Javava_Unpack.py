import struct
from .info import MessageNames,GameStatus,GameCommand
from .base_protocal import Javava_Base_Proto,wordpack

class Task_Game_New(Javava_Base_Proto):

    def __init__(self):
        super(Task_Game_New,self).__init__(MessageNames.Task_Game_New)
    def unpack(self,data_no_header):
        #data_no_header=self.stripheader(data)
        data_no_header,send_id,recv_id=self.unpack_id(data_no_header)
        paramtuple=struct.unpack('>32s5H',data_no_header[:42])
        taillength=len(data_no_header[42:])
        paramlist=list(paramtuple)
        paramlist.extend(struct.unpack(str(taillength)+'s',data_no_header[42:]))#length and other data
        paramlist.insert(0,recv_id)
        paramlist.insert(0, send_id)
        return tuple(paramlist)
    def pack(self,send_id,recv_id,game_id,game_duration,game_rate1,game_rate2,game_rate3,game_other,task_rmtpurl):
        if not isinstance(game_id,bytes):
            game_id=game_id.encode('utf-8')
        if not isinstance(task_rmtpurl,bytes):
            task_rmtpurl=task_rmtpurl.encode('utf-8')
        headerdata = self.packheader()
        id_data = self.pack_id(send_id,recv_id)
        task_rmtpurl_len=str(len(task_rmtpurl))+'s'
        content_data = struct.pack('>32s5H'+task_rmtpurl_len, game_id,game_duration,game_rate1,game_rate2,game_rate3,game_other,task_rmtpurl)
        content_length = self.check_datalen(content_data+id_data)
        if content_length:
            return b''.join([headerdata, wordpack(content_length), id_data,content_data])
        raise ValueError("Status not right or Message too long")

class Task_GameStatus_Control(Javava_Base_Proto):

    def __init__(self):
        super(Task_GameStatus_Control,self).__init__(MessageNames.Task_GameStatus_Control)
    def unpack(self,data_no_header):
        data_no_header, send_id, recv_id = self.unpack_id(data_no_header)
        paramtuple = struct.unpack('>32sB', data_no_header)
        paramlist = list(paramtuple)
        paramlist.insert(0, recv_id)
        paramlist.insert(0, send_id)
        return tuple(paramlist)
    def pack(self,send_id,recv_id,game_id,game_status):
        headerdata=self.packheader()
        id_data = self.pack_id(send_id,recv_id)
        if game_status in GameStatus.get_status():
            content_data=struct.pack(">32sB",game_id,game_status)
            content_length=self.check_datalen(content_data+id_data)
            if content_length:
                return b''.join([headerdata,wordpack(content_length),id_data,content_data])
        raise ValueError("Status not right or Message too long")

class Task_Game_Query(Javava_Base_Proto):

    def __init__(self):
        super(Task_Game_Query,self).__init__(MessageNames.Task_GameResult_Query)
    def unpack(self,data_no_header):
        #data_no_header=self.stripheader(data)
        data_no_header, send_id, recv_id = self.unpack_id(data_no_header)
        paramtuple=struct.unpack('>32s',data_no_header)
        paramlist=list(paramtuple)
        paramlist.insert(0, recv_id)
        paramlist.insert(0, send_id)
        return tuple(paramlist)
    def pack(self,send_id,recv_id,game_id):
        if not isinstance(game_id,bytes):
            game_id=game_id.encode('utf-8')
        headerdata = self.packheader()
        id_data = self.pack_id(send_id,recv_id)
        content_data = struct.pack(">32s", game_id)
        content_length = self.check_datalen(content_data+id_data)
        if content_length:
            return b''.join([headerdata, wordpack(content_length), id_data,content_data])
        raise ValueError(" Game id  too long")

class Task_Game_Command(Javava_Base_Proto):

    def __init__(self):
        super(Task_Game_Command,self).__init__(MessageNames.Task_Game_Command)
    def unpack(self,data_no_header):
        data_no_header, send_id, recv_id = self.unpack_id(data_no_header)
        paramtuple = struct.unpack('>32sIB2H', data_no_header)
        paramlist = list(paramtuple)
        paramlist.insert(0, recv_id)
        paramlist.insert(0, send_id)
        return paramlist
    def pack(self,send_id,recv_id,game_id,game_timestamp,game_command,game_speed_x,game_speed_y):
        headerdata=self.packheader()
        id_data = self.pack_id(send_id,recv_id)
        if game_command in [GameCommand.Move,GameCommand.Catch,GameCommand.SwitchCamera]:
            content_data=struct.pack('>32sIB2H',game_id,game_timestamp,game_command,game_speed_x,game_speed_y)
            content_length = self.check_datalen(content_data+id_data)
            if content_length:
                return b''.join([headerdata, wordpack(content_length), id_data,content_data])
        raise ValueError("Status not right or Message too long")
