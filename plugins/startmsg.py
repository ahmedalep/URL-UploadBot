class Translation(object):
    START_TEXT = """Hi {} ๐

I'm Url Upload Bot ๐

<b>Permanent Thumbnail Support๐ฏ.</b>

<i>Send me a direct link and I will upload it to telegram as a file/video.</i>

Click /help for more details...."""
    ADD_CAPTION_HELP = """Select an uploaded file/video or forward me <b>Any Telegram File</b> and just write the text you want to be on the file <b>as a reply to the file</b> and the text you wrote will be attached as the caption! ๐คฉ
    
Example: <a href='https://te.legra.ph/file/ecf5297246c5fb574d1a0.jpg'>See This!</a> ๐"""

    INCORRECT_REQUEST = """Please make sure you submit your request correctly."""
    WAIT_PROCESS_FINISH = """Please wait for your current file to finish downloading before sending more links!

Or use /cancel to terminate incomplete processes."""
    PROCESS_CANCELLED = """File upload cancelled
You can now send a new URL."""
    NO_PROCESS_FOUND = """๐คทโโ๏ธ No pending uploads were found. You can upload files by sending a link now!"""
    FORMAT_SELECTION = "๐๐ฆ๐ฒ๐น๐ฒ๐ฐ๐ ๐๐ป๐ฑ ๐๐ต๐ผ๐๐ฒ ๐ฌ๐ผ๐๐ฟ ๐๐ผ๐ฟ๐บ๐ฎ๐๐"
    SET_CUSTOM_USERNAME_PASSWORD = """\n๐ฎโโ Powered By :</b> @A7_SYR"""
    DOWNLOAD_START = "๐ฅ DOWNLOADING..."
    UPLOAD_START = "๐ค UPLOADING..."
    RCHD_TG_API_LIMIT = "<b>Downloaded in:</b> {} seconds.\n<b>Detected file size:</b> {}.\n\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations ๐."
    #AFTER_SUCCESSFUL_UPLOAD_MSG = "๐๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐ ๐๐ ๐ฅฐ"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "๐๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐ ๐๐"
    SAVED_CUSTOM_THUMB_NAIL = "Save Your Thumbnail โ."
    DEL_ETED_CUSTOM_THUMB_NAIL = " Delete Your Thumbnail โ."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = """<b>I think you have entered an unaccessible url or a private url.</b>
<i>Go check if you can access the content in the url from your browser first!</i>

<b>YouTubeDL</b> said: {}"""
    HELP_USER = """<b>How to Use Me?</b> ๐ค

1. Send your URL link

2. Send thumbnail photo to save it permanently.

3. Select the desired option

4. Send /delthumbnail To Delete Your Thumbnail.

5.  Use /caption to Set caption as Reply to Media

6. Comments /about /viewthumbnail /info
"""
    ABOUT_TEXT = """<b>๐ My Name :</b> URL-UploadBot V3 ๐

<b>๐ Channel :</b> <a href="https://t.me/+uPg3TPNFuckwMDU0"

<b>๐ Source :</b> <a href="https://t.me/+uPg3TPNFuckwMDU0"

<b>๐ Language :</b> <a href="https://www.python.org/">Python 3.10.8</a>

<b>๐ Framework :</b> <a href="https://docs.pyrogram.org/">Pyrogram 1.4.16</a>

<b>๐ Creater :</b> @A7_SYR"""

    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Send your thumbnail pic to generate custom thumbail."
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    CANCEL_STR = "โ Cancelled โ"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds."
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    INFO_TEXT = """
๐ธ First Name : <b>{}</b>

๐ธ Second Name : <b>{}</b>

๐ธ Username : <b>@{}</b>

๐ธ Id : <code>{}</code>

๐ธ Profile : <b>{}</b>

๐ธ Dc : <b>{}</b>

๐ธ Language : <b>{}</b>

๐ธ Status : <b>{}</b>
"""
    # Soon ๐ฏ
    #START_BUTTONS = InlineKeyboardMarkup(
       #  [[
       #  InlineKeyboardButton('HELP', callback_data='help')
       #  InlineKeyboardButton('ABOUT', callback_data='about')
       #  ],[
      #   InlineKeyboardButton('CLOSE', callback_data='close')
        # ]]
  #  )
  # BUTTONS = InlineKeyboardMarkup(

