import struct
from .info import MessageNames,GameCommand,GameStatus,GameResult
from .base_protocal import Javava_Base_Proto,wordpack

class Task_HeartBeat(Javava_Base_Proto):

    def __init__(self):
        super(Task_HeartBeat,self).__init__(MessageNames.Task_HeartBeat)
    def pack(self,send_id,recv_id):
        headerdata=self.packheader()
        id_data = self.pack_id(send_id,recv_id)
        content_length = len(id_data)
        if content_length < self.message_max_length:
            return b''.join([headerdata, wordpack(content_length), id_data])
        raise ValueError("Message too long")

    def unpack(self,data_no_header):
        data_no_header, send_id, recv_id = self.unpack_id(data_no_header)
        print("Task_HeartBeat Recieved!")
        return (send_id,recv_id)

class Task_Onlog(Javava_Base_Proto):

    def __init__(self):
        super(Task_Onlog,self).__init__(MessageNames.Task_Onlog)
    def pack(self,send_id,recv_id,log_content):
        if not isinstance(log_content,bytes):
            content_data=log_content.encode('utf-8')
        headerdata=self.packheader()
        id_data = self.pack_id(send_id,recv_id)
        content_length=len(id_data+content_data)
        if content_length<self.message_max_length:
            return b''.join([headerdata,wordpack(content_length),id_data,content_data])
        raise ValueError("Message too long")
    def unpack(self,data_no_header):
        data_no_header, send_id, recv_id = self.unpack_id(data_no_header)
        datalen=len(data_no_header)
        paramtuple = struct.unpack(str(datalen)+'s',data_no_header)
        paramlist = list(paramtuple)
        paramlist.insert(0, recv_id)
        paramlist.insert(0, send_id)
        return tuple(paramlist)


class Task_GameStatus_Return(Javava_Base_Proto):

    def __init__(self):
        super(Task_GameStatus_Return,self).__init__(MessageNames.Task_GameStatus_Return)
    def pack(self,send_id,recv_id,game_id,game_status):
        if not isinstance(game_id,bytes):
            game_id=game_id.encode('utf-8')
        #game_id needs to be bytes string
        headerdata=self.packheader()
        id_data = self.pack_id(send_id,recv_id)
        if game_status in GameStatus.get_status():
            content_data = struct.pack('>32sB', game_id, game_status)
            content_length = len(content_data+id_data)
            if content_length < self.message_max_length:
                return b''.join([headerdata, wordpack(content_length),id_data, content_data])
        raise ValueError("Status not right or Message too long")
    def unpack(self,data_no_header):
        data_no_header, send_id, recv_id = self.unpack_id(data_no_header)
        paramtuple = struct.unpack('>32sB', data_no_header)
        paramlist = list(paramtuple)
        paramlist.insert(0, recv_id)
        paramlist.insert(0, send_id)
        return tuple(paramlist)


class Task_GameResult_Return(Javava_Base_Proto):

    def __init__(self):
        super(Task_GameResult_Return,self).__init__(MessageNames.Task_GameResult_Return)
    def pack(self,send_id,recv_id,game_id,game_status,game_result):
        if not isinstance(game_id,bytes):
            game_id=game_id.encode('utf-8')
        #game_id needs to be bytes string
        headerdata=self.packheader()
        id_data = self.pack_id(send_id,recv_id)
        if game_status in GameStatus.get_status() and game_result in [GameResult.Win,GameResult.Pending,GameResult.Lose]:
            content_data=struct.pack('>32sBB',game_id,game_status,game_result)
            content_length = self.check_datalen(content_data+id_data)
            if content_length:
                return b''.join([headerdata, wordpack(content_length), id_data,content_data])
        raise ValueError("Status not right or Message too long")
    def unpack(self,data_no_header):
        data_no_header, send_id, recv_id = self.unpack_id(data_no_header)
        paramtuple = struct.unpack('>32sBB', data_no_header)
        paramlist = list(paramtuple)
        paramlist.insert(0, recv_id)
        paramlist.insert(0, send_id)
        return tuple(paramlist)


class Task_Jvv_Login(Javava_Base_Proto):

    def __init__(self):
        super(Task_Jvv_Login,self).__init__(MessageNames.Task_Jvv_Login)
    def pack(self,send_id,recv_id,machine_code):
        if not isinstance(machine_code,bytes):
            machine_code=machine_code.encode('utf-8')
        headerdata = self.packheader()
        id_data = self.pack_id(send_id,recv_id)
        content_data=struct.pack(">20s",machine_code)
        content_length = len(id_data + content_data)
        if content_length < self.message_max_length:
            return b''.join([headerdata, wordpack(content_length), id_data, content_data])
        raise ValueError("Machineid too long")
    def unpack(self, data_no_header):
        data_no_header, send_id, recv_id = self.unpack_id(data_no_header)
        paramtuple = struct.unpack('>20s', data_no_header)
        paramlist = list(paramtuple)
        paramlist.insert(0, recv_id)
        paramlist.insert(0, send_id)
        return tuple(paramlist)

class Task_Game_New_Apply(Javava_Base_Proto):

    def __init__(self):
        super(Task_Game_New_Apply,self).__init__(MessageNames.Task_Game_New_Apply)
    def pack(self,send_id,recv_id,jid,auid):
        if not isinstance(jid,bytes):
            jid=jid.encode('utf-8')
        if not isinstance(auid,bytes):
            auid=auid.encode('utf-8')
        headerdata = self.packheader()
        id_data = self.pack_id(send_id,recv_id)
        content_data=struct.pack('>32s32s',jid,auid)
        content_length = len(id_data + content_data)
        if content_length < self.message_max_length:
            return b''.join([headerdata, wordpack(content_length), id_data, content_data])
        raise ValueError("Machineid too long")
    def unpack(self, data_no_header):
        data_no_header, send_id, recv_id = self.unpack_id(data_no_header)
        paramtuple = struct.unpack('>32s32s', data_no_header)
        paramlist = list(paramtuple)
        paramlist.insert(0, recv_id)
        paramlist.insert(0, send_id)
        return tuple(paramlist)

class Task_GamePic_UpLoad(Javava_Base_Proto):

    def __init__(self):
        super(Task_GamePic_UpLoad,self).__init__(MessageNames.Task_GamePic_UpLoad)
    def pack(self,send_id,recv_id,game_id,timestamp,game_pic):
        if not isinstance(game_id,bytes):
            game_id=game_id.encode('utf-8')
        headerdata = self.packheader()
        id_data = self.pack_id(send_id,recv_id)
        game_pic_length=str(len(game_pic))+'s'
        content_data=struct.pack('>32sI'+game_pic_length,game_id,timestamp,game_pic)
        content_length = self.check_datalen(content_data+id_data)
        if content_length:
            return b''.join([headerdata, wordpack(content_length), id_data,content_data])
        raise ValueError("picture data too big ")
    def unpack(self,data_no_header):
        data_no_header, send_id, recv_id = self.unpack_id(data_no_header)
        piclen = str(len(data_no_header[36:]))+'s'
        paramtuple = struct.unpack('>32sI'+piclen, data_no_header)
        paramlist = list(paramtuple)
        paramlist.insert(0, recv_id)
        paramlist.insert(0, send_id)
        return tuple(paramlist)






