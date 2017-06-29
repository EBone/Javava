import unittest
from JavavaNetData import pack_data,unpack_data
from JavavaNetData.info import MessageNames,GameCommand
import struct
send_id="192.163.31.1".encode('utf-8')
recv_id="188.88.88.8".encode('utf-8')

def handle_data(classname,data):
    if isinstance(data,str) or isinstance(data,bytes):
        pack_result = pack_data(classname, send_id, recv_id, data)
    elif data==None:
        pack_result = pack_data(classname, send_id, recv_id)
    else:
        pack_result = pack_data(classname, send_id, recv_id,*data)
    print(pack_result)
    unpack_result = unpack_data(classname,pack_result[7:])
    print(unpack_result)
    return pack_result,unpack_result


class TestJavavaMethods(unittest.TestCase):

    def test_Task_heart(self):
        pack_result, unpack_result = handle_data(MessageNames.Task_HeartBeat,None)
        self.assertEqual(unpack_result[0], send_id)
        self.assertEqual(unpack_result[1], recv_id)


    def test_Task_onlog(self):
        content="fuckit"
        pack_result,unpack_result=handle_data(MessageNames.Task_Onlog,content)
        self.assertEqual(unpack_result[0],send_id)
        self.assertEqual(unpack_result[1], recv_id)
        self.assertEqual(unpack_result[2],content.encode('utf-8'))

    def test_Task_new(self):
        content =(b'a'*32,0x11,0x11,0x22,0x33,0x44,'rtmp:123.123.123.123'.encode('utf-8'))
        pack_result, unpack_result = handle_data(MessageNames.Task_Game_New,content)
        self.assertEqual(unpack_result[0], send_id)
        self.assertEqual(unpack_result[1], recv_id)
        self.assertEqual(unpack_result[2:],content )

    def test_Task_gamestatus_return(self):
        for i in range(20):
            try:
                content=(b'x'*32,i)
                pack_result, unpack_result = handle_data(MessageNames.Task_GameStatus_Return,content)
                self.assertEqual(unpack_result[0], send_id)
                self.assertEqual(unpack_result[1], recv_id)
                self.assertEqual(tuple(unpack_result[2:]), content)
            except ValueError:
                print("%d is not registered"%i)


    def test_Task_gamestatus_control(self):
        for i in range(20):
            try:
                content=(b'x'*32,i)
                pack_result, unpack_result = handle_data(MessageNames.Task_GameStatus_Control,content)
                self.assertEqual(unpack_result[0], send_id)
                self.assertEqual(unpack_result[1], recv_id)
                self.assertEqual(unpack_result[2:], content)
            except ValueError:
                print("%d is not registered"%i)

    def test_Task_gameresult_query(self):
        content=b's'*32
        pack_result, unpack_result = handle_data(MessageNames.Task_GameResult_Query, content)
        self.assertEqual(unpack_result[0], send_id)
        self.assertEqual(unpack_result[1], recv_id)
        self.assertEqual(unpack_result[2], content)


    def test_Task_gameresult_return(self):
        id=b'd'*32
        status=range(10)
        result=0x01,0x02,0x04
        result_list=[]
        for s in status:
            for r in result:
                result_list.append((id,s,r))
        for content in result_list:
            #print(content)
            try:
                pack_result, unpack_result = handle_data(MessageNames.Task_GameResult_Return,content)
                self.assertEqual(unpack_result[0], send_id)
                self.assertEqual(unpack_result[1], recv_id)
                self.assertEqual(unpack_result[2:], tuple(content))
            except ValueError:
                print(content,end=" ")
                print("content is not registered")

    def test_Task_game_command(self):
        for i in [GameCommand.Move,GameCommand.Catch,GameCommand.SwitchCamera]:
            content=(b"c"*32,0x1234,i,99,98)
            pack_result, unpack_result = handle_data(MessageNames.Task_Game_Command, content)
            self.assertEqual(unpack_result[0], send_id)
            self.assertEqual(unpack_result[1], recv_id)
            self.assertEqual(tuple(unpack_result[2:]), content)


    def test_Task_gamepic_upload(self):
        with open("test.jpg",'rb') as picjpg:
            content=(b"u"*32,0x12221,picjpg.read())
            pack_result, unpack_result = handle_data(MessageNames.Task_GamePic_UpLoad, content)
            self.assertEqual(unpack_result[0], send_id)
            self.assertEqual(unpack_result[1], recv_id)
            self.assertEqual(tuple(unpack_result[2:]), content)

    def test_Task_gamenew_apply(self):
        content=("sd"*16,"sf"*16)
        pack_result, unpack_result = handle_data(MessageNames.Task_Game_New_Apply, content)
        self.assertEqual(unpack_result[0], send_id)
        self.assertEqual(unpack_result[1], recv_id)
        self.assertEqual(unpack_result[2:], (content[0].encode('utf-8'),content[1].encode('utf-8')))
    def test_Task_Jvv_login(self):
        content="abcd"*5
        pack_result, unpack_result = handle_data(MessageNames.Task_Jvv_Login, content)
        self.assertEqual(unpack_result[0], send_id)
        self.assertEqual(unpack_result[1], recv_id)
        self.assertEqual(unpack_result[2], content.encode('utf-8'))


if __name__=="__main__":
    unittest.main()
