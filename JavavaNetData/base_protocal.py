import struct

def bytepack(intdata):
    assert isinstance(intdata, int), "value is not int"
    bytedata=struct.pack('>B',intdata)
    return bytedata

def wordpack(intdata):
    assert isinstance(intdata, int), "value is not int"
    wordata=struct.pack('>H',intdata)
    return wordata

class Javava_Base_Proto(object):
    proto_header=(0xac,0xe0)
    proto_name = 0x01
    version_number = 0x10
    # use message_length to check datalength
    message_max_length=(1<<15)-1

    def __init__(self,message_name):
        #check value and get the bytedata
        self.message_name=bytepack(message_name)

    def packheader(self):
        headerdata=b''.join([struct.pack('>B',self.proto_header[0]),struct.pack('>B',self.proto_header[1]),struct.pack('>B',self.proto_name),struct.pack('>B',self.version_number),self.message_name])
        return headerdata
    def pack_id(self,send_id,recv_id):
        if not isinstance(send_id,bytes):
            send_id=send_id.encode('utf-8')
        if not isinstance(recv_id,bytes):
            recv_id=recv_id.encode('utf-8')
        send_len=len(send_id)
        recv_len=len(recv_id)
        id_data=struct.pack('>H'+str(send_len)+'s'+'H'+str(recv_len)+'s',send_len,send_id,recv_len,recv_id)
        return id_data

    def check_datalen(self,contentdata):
        datalen=len(contentdata)
        if datalen<self.message_max_length:
            return datalen
    def unpack_id(self,data_no_header):
        send_len = struct.unpack('>H', data_no_header[:2])[0]
        send_content_pos = send_len + 2
        send_id = struct.unpack(str(send_len) + 's', data_no_header[2:send_content_pos])[0]
        recv_len = struct.unpack('>H', data_no_header[send_content_pos:send_content_pos + 2])[0]
        recv_content_pos = send_content_pos + 2 + recv_len
        recv_id = struct.unpack(str(recv_len) + 's', data_no_header[send_content_pos + 2:recv_content_pos])[0]
        return data_no_header[recv_content_pos:],send_id,recv_id

    def pack(self,send_id,recv_id,data):
        raise NotImplementedError

    def unpack(self,data_no_header):
        raise NotImplementedError


if __name__=="__main__":
    pass
