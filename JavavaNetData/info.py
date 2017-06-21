class MessageNames:
    Task_HeartBeat=0x00
    Task_Onlog=0x01
    Task_Game_New=0x10
    Task_GameStatus_Return=0x11
    Task_GameStatus_Control=0x12
    Task_GameResult_Query=0x13
    Task_GameResult_Return=0x14
    Task_Game_Command=0x20
    Task_GamePic_UpLoad=0x21
    Task_Game_New_Apply=0x55
    Task_Jvv_Login=0x51


class GameStatus:
    Invalid=0x00
    Waiting=0x01
    Excecuting=0x02
    Failure=0x04
    Pause=0x05
    Abort=0x06
    Recovery=0x07
    HangUp=0x08
    Done=0x09

class GameResult:
    Win=0x01
    Pending=0x02
    Lose=0x04

class GameCommand:
    Forward=0x01
    Backward=0x02
    Left=0x03
    Right=0x04
    Upward=0x05
    Downward=0x06
    Catch=0x07
    Loose=0x08

    @classmethod
    def getcommand(cls):
        return [cls.Forward,cls.Backward,cls.Left,cls.Right,cls.Upward,cls.Downward,cls.Catch,cls.Loose]


if __name__=="__main__":
    print(GameCommand.getcommand())
