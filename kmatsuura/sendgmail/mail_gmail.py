import base64
import apiclient
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from gmail_auth import create_Gmail_credential

import datetime

def send_msg_with_file(sender, to, cc, subject, message_text, file_name):
    """Create a message for an email.
    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.
    file: The path to the file to be attached.
    Returns:
    An object containing a base64url encoded email object.
    """
    # initialize message object
    message = MIMEMultipart()
    # set each elementes needed
    message['to'] = to
    message['cc'] = cc
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(message_text)
    message.attach(msg)
    try:
        # defie file type
        msg = MIMEBase('text', 'comma-separated-values')
        # define file location and open it
        file_location = os.path.abspath(file_name)
        # make attachment
        attachment = open(file_location, "rb")
        # set attachment
        msg.set_payload((attachment).read())
        encoders.encode_base64(msg)
        msg.add_header(f'Content-Disposition', "attachment; filename={file_location}")
        # attach the file
        message.attach(msg)
    except:
        print("There is no file here")
    # encode bytes string
    byte_msg = message.as_string().encode(encoding="UTF-8")
    byte_msg_b64encoded = base64.urlsafe_b64encode(byte_msg)
    str_msg_b64encoded = byte_msg_b64encoded.decode(encoding="UTF-8")
    return {"raw": str_msg_b64encoded}

def send_message(to, cc, subject, message_text, file_name = "none"):
    # "me" means that your email address authorized
    sender = "me"
    # create credentials
    service = create_Gmail_credential()
    if file_name != "none":

        try:
            result = service.users().messages().send(
                userId=sender,
                body=send_msg_with_file(sender, to, cc, subject, message_text)
            ).execute()
            print("Message Id: {}".format(result["id"]))
        except apiclient.errors.HttpError:
            print("------start trace------")
            traceback.print_exc()
            print("------end trace------")
    
    else:
        try:
            result = service.users().messages().send(
                userId=sender,
                body=send_msg_with_file(sender, to, cc, subject, message_text, file_name)
            ).execute()
            print("Message Id: {}".format(result["id"]))
        except apiclient.errors.HttpError:
            print("------start trace------")
            traceback.print_exc()
            print("------end trace------")


if __name__ == "__main__":
    os.chdir("/home/kmatsuura/Desktop/study/daily_report")
    ans = "n"
    while ans != "y":

        print("始業時間（例：12:00）")
        starttime = input()

        print("就業時間（例：17:00）")
        endtime = input()

        print("実労時間（例：5:00）")
        worktime = input()

        print("進捗")
        sintyoku = input()

        print("課題")
        kadai = input()

        print("共有")
        kyouyuu = input()

        print("-"*20)
        print("始業時間：" + starttime)
        print("就業時間：" + endtime)
        print("実労時間：" + worktime)
        print("進捗：" + sintyoku)
        print("課題：" + kadai)
        print("共有：" + kyouyuu)
        print("-"*20)
        print("こちらでよろしいですか？(y/n)")
        ans = input()
        if ans == "y":
            break
        else:
            print("入力をはじめからやり直します。")
    # set email address you want to send
    to = "tech_kanri@hmcom.co.jp"
    cc = "kengo.matsuura@hmcom.co.jp,sales_kanri@hmcom.co.jp"
    # set subject
    dt_now = datetime.datetime.now()
    yobi = ["月","火","水","木","金","土","日"]
    today = dt_now.strftime('%Y年%m月%d日') + "（" + yobi[dt_now.weekday()] + "）"
    subject = "【日報】" + today
    # set message
    message_text = "お疲れ様です。" + today +  """の日報を報告いたします。
    【勤怠】""" + starttime + "-" + endtime + "( 実働:" + worktime + """)
     ======================================
    （研究・開発）FAST-D開発（2019年度）(1950201)
     ======================================

    予定 :飛行機のエンジンの異常音を検知する特徴量の探索
    進捗 :""" + sintyoku + """
    課題 :""" + kadai + """
    共有：""" + kyouyuu
    # set filemessage
    filename = ""
    send_message(to, cc, subject, message_text)