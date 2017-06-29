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
    @classmethod
    def get_status(cls):
        return [cls.Invalid,cls.Waiting,cls.Excecuting,cls.Failure,cls.Pause,cls.Abort,cls.Recovery,cls.HangUp,cls.Done]

class GameResult:
    Win=0x01
    Pending=0x02
    Lose=0x04

class GameCommand:
    Move=0x01
    Catch=0x07
    SwitchCamera=0x20


if __name__=="__main__":
    print(GameCommand.getcommand())
