import os


class Commandi:
    LEECH = os.environ.get(
        "COMMANDI_LEECH",
        "leech@MaxLeechVideo_bot"
    )
    PURGE = os.environ.get(
        "COMMANDI_PURGE",
        "purge"
    )
    YTDL = os.environ.get(
        "COMMANDI_YTDL",
        "ytdl@MaxLeechVideo_bot"
    )
    STATUS = os.environ.get(
        "COMMANDI_STATUS",
        "status@MaxLeechVideo_bot"
    )
    CANCEL = os.environ.get(
        "COMMANDI_CANCEL",
        "cancel"
    )
    EXEC = os.environ.get(
        "COMMANDI_EXEC",
        "exec"
    )
    RENAME = os.environ.get(
        "COMMANDI_RENAME",
        "rename"
    )
    UPLOAD = os.environ.get(
        "COMMANDI_UPLOAD",
        "upload"
    )
    HELP = os.environ.get(
        "COMMANDI_HELP",
        "help"
    )
    SAVETHUMBNAIL = os.environ.get(
        "COMMANDI_SAVETHUMBNAIL",
        "savethumbnail@MaxLeechVideo_bot"
    )
    CLEARTHUMBNAIL = os.environ.get(
        "COMMANDI_CLEARTHUMBNAIL",
        "clearthumbnail@MaxLeechVideo_bot"
    )
    GET_RCLONE_CONF_URI = os.environ.get(
        "COMMANDI_GET_RCLONE_CONF_URI",
        "getrcloneconfuri"
    )
