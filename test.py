from imap_tools import MailBox, AND, A

# Get date, subject and body len of all emails from INBOX folder
with MailBox('imap.gmail.com').login('pkzoom94320@gmail.com', 'yomfkroicvfuujlo') as mailbox:
    for msg in mailbox.fetch(A()):
        print(msg.text)
        print(msg)

a = 1