def LaunchApp_Javaversion_OnLogError(Sender, LogParams):
    locked = aqString.Find(LogParams.Str, "The object \"btnLater\" does not exist.")   ##here we use the name btnLater, if this changes we hace to update this parameter.
    if locked != -1:
      LogParams.Locked=True
    else:
      LogParams.Locked = False

def EventControl1_OnLogError(Sender, LogParams):
    pass
