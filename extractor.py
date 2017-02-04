import os
import re
import wget
import time

MD5_REGEX = r'[A-Fa-f0-9]{32}'
md5_dict = {}

SHA1_REGEX = r'[A-Fa-f0-9]{40}'
sha1_dict = {}

SHA256_REGEX = r'[A-Fa-f0-9]{64}'
sha256_dict = {}

SHA512_REGEX = r'[A-Fa-f0-9]{128}'
sha512_dict = {}

GOOGLE_API_REGEX = r'(AIza.{35})'
google_api_dict = {}

AWS_API_ID_REGEX = r'AKIA.{16}'
aws_api_id_dict = {}

AWS_SECRET_KEY_REGEX = r'[^A-Za-z0-9/+=][A-Za-z0-9/+=]{40}(?![A-Za-z0-9/+=])'
aws_secret_key_dict = {}


EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
email_dict = {}

def extract(line, regex, dict, fill):
    m = re.findall(regex, line)
    if len(m) > 0:
        for val in m:
            val = val.strip()
            dict[val] = True
            line = re.sub(val, fill, line)
        print line
    return line

if __name__ == "__main__":
    f = open('url_list.txt', 'r')
    urls = f.read().split('\n')
    for i in urls:
        ticks = str(time.time())

        # filename = wget.download(url)
        if not 'http://' in i and not 'https://' in i:
            i = 'http://' + i
        print i
        wget.download(i, 'raw/'+ticks+'.txt')

    for file in os.listdir("raw/"):
        if file.endswith(".txt"):
            f = open('raw/'+file, 'r')
            lines = f.read().split('\r\n')
            for line in lines:
                line = extract(line, EMAIL_REGEX, email_dict, '[EMAIL]')
                line = extract(line, GOOGLE_API_REGEX, google_api_dict, '[GOOGLE API]')
                line = extract(line, AWS_API_ID_REGEX, aws_api_id_dict, '[AWS API ID]')
                # line = extract(line, AWS_SECRET_KEY_REGEX, aws_secret_key_dict, '[AWS SECRET KEY]')
                line = extract(line, SHA512_REGEX, sha512_dict, '[SHA512]')
                line = extract(line, SHA256_REGEX, sha256_dict, '[SHA256]')
                line = extract(line, SHA1_REGEX, sha1_dict, '[SHA1]')
                line = extract(line, MD5_REGEX, md5_dict, '[MD5]')

    ticks = str(int(time.time()))
    f = open('processed/email'+ticks+'.txt', 'w')
    for i in email_dict.keys():
        f.write(i+'\n')  # python will convert \n to os.linesep
    f.close()

    ticks = str(int(time.time()))
    f = open('processed/google_api'+ticks+'.txt', 'w')
    for i in google_api_dict.keys():
        f.write(i+'\n')  # python will convert \n to os.linesep
    f.close()

    ticks = str(int(time.time()))
    f = open('processed/aws_api_id'+ticks+'.txt', 'w')
    for i in aws_api_id_dict.keys():
        f.write(i+'\n')  # python will convert \n to os.linesep
    f.close()

    ticks = str(int(time.time()))
    f = open('processed/aws_secret_key'+ticks+'.txt', 'w')
    for i in aws_secret_key_dict.keys():
        f.write(i+'\n')  # python will convert \n to os.linesep
    f.close()

    ticks = str(int(time.time()))
    f = open('processed/sha512'+ticks+'.txt', 'w')
    for i in sha512_dict.keys():
        f.write(i+'\n')  # python will convert \n to os.linesep
    f.close()

    ticks = str(int(time.time()))
    f = open('processed/sha256'+ticks+'.txt', 'w')
    for i in sha256_dict.keys():
        f.write(i+'\n')  # python will convert \n to os.linesep
    f.close()

    ticks = str(int(time.time()))
    f = open('processed/sha1'+ticks+'.txt', 'w')
    for i in sha1_dict.keys():
        f.write(i+'\n')  # python will convert \n to os.linesep
    f.close()

    ticks = str(int(time.time()))
    f = open('processed/md5'+ticks+'.txt', 'w')
    for i in md5_dict.keys():
        f.write(i+'\n')  # python will convert \n to os.linesep
    f.close()
