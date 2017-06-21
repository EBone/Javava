import struct

def bytepack(intdata):
    assert isinstance(intdata, int), "value is not int"
    bytedata=struct.pack('>B',intdata)
    return bytedata

def wordpack(intdata):
    assert isinstance(intdata, int), "value is not int"
    wordata=struct.pack('>H',intdata)
    return wordata

class Javava_Base_Proto:
    proto_header=(0xac,0xe0)
    proto_name = 0x01
    version_number = 0x10
    # use message_length to check datalength
    message_max_length=(1<<32)-1

    def __init__(self,message_name,send_id,recv_id):
        #check value and get the bytedata
        self.message_name=bytepack(message_name)
        self.send_id=send_id
        self.recv_id=recv_id


    def packheader(self):
        headerdata=b''.join([struct.pack('>B',self.proto_header[0]),struct.pack('>B',self.proto_header[1]),struct.pack('>B',self.proto_name),struct.pack('>B',self.version_number),self.message_name])
        return headerdata
    def pack_id(self):
        send_len=len(self.send_id)
        recv_len=len(self.recv_id)
        id_data=struct.pack('>H'+str(send_len)+'s'+'H'+str(recv_len)+'s',send_len,self.send_id,recv_len,self.recv_id)
        return id_data

    def check_datalen(self,contentdata):
        datalen=len(contentdata)
        if datalen<self.message_max_length:
            return datalen

    def pack(self,data):
        raise NotImplementedError

    def unpack(self,data_no_header):
        raise NotImplementedError


if __name__=="__main__":
    pass
