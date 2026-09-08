from ...core.config_manager import Config

i = Config.CMD_SUFFIX

class BotCommands:
    StartCommand = f"start{i}"
    MirrorCommand = [f"mirror{i}", f"m{i}"]
    QbMirrorCommand = [f"qbmirror{i}", f"qm{i}"]
    JdMirrorCommand = [f"jdmirror{i}", f"jm{i}"]
    YtdlCommand = [f"ytdl{i}", f"y{i}"]
    GallerydlCommand = [f"gallerydl{i}", f"gdl{i}"]
    NzbMirrorCommand = [f"nzbmirror{i}", f"nm{i}"]
    LeechCommand = [f"tedl{i}", f"tl{i}"]
    QbLeechCommand = [f"qbtedl{i}", f"qtl{i}"]
    JdLeechCommand = [f"jdtedl{i}", f"jtl{i}"]
    YtdlLeechCommand = [f"ytdltedl{i}", f"ytl{i}"]
    GallerydlLeechCommand = [f"gallerydltedl{i}", f"gdltedl{i}"]
    NzbLeechCommand = [f"nzbtedl{i}", f"ntl{i}"]
    CloneCommand = f"clone{i}"
    CountCommand = f"count{i}"
    DeleteCommand = f"del{i}"
    CancelTaskCommand = [f"cancel{i}", f"c{i}"]
    CancelAllCommand = f"cancelall{i}"
    ForceStartCommand = [f"forcestart{i}", f"fs{i}"]
    ListCommand = f"list{i}"
    SearchCommand = f"search{i}"
    StatusCommand = f"status{i}"
    UsersCommand = f"users{i}"
    AuthorizeCommand = f"auth{i}"
    UnAuthorizeCommand = f"unauth{i}"
    AddSudoCommand = f"addsudo{i}"
    RmSudoCommand = f"rmsudo{i}"
    PingCommand = f"ping{i}"
    RestartCommand = f"restart{i}"
    StatsCommand = f"stats{i}"
    HelpCommand = f"help{i}"
    LogCommand = f"log{i}"
    ShellCommand = f"shell{i}"
    AExecCommand = f"aexec{i}"
    ExecCommand = f"exec{i}"
    ClearLocalsCommand = f"clearlocals{i}"
    BotSetCommand = [f"bsetting{i}", f"bs{i}"]
    UserSetCommand = [f"usetting{i}", f"us{i}"]
    SelectCommand = f"sel{i}"
    RssCommand = f"rss{i}"
    NzbSearchCommand = f"nzbsearch{i}"
