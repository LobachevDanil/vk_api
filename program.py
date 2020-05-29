import argparse
import urllib.request
import json

URL = "https://api.vk.com/method/"
METHOD_NAME = "friends.get?"
TOKEN = "b673fdc130c04660888ea12287e13506fd820711215baff35ff5890bed2ada8808db8285df6c5e8dbffeb"
VERSION = '5.107'


def make_request(user_id, fields):
    options = ""
    if len(fields) != 0:
        options = "&fields=" + ','.join(fields)
    info_id = '&user_id=' + user_id
    info_token = '&access_token=' + TOKEN
    version = '&v=' + VERSION
    data = URL + METHOD_NAME + options + info_id + info_token + info_token + version
    print(data)
    answer = urllib.request.urlopen(data)
    return json.load(answer)


def main(id):
    addr = 'https://api.vk.com/method/users.get?user_id=10042554&access_token=b673fdc130c04660888ea12287e13506fd820711215baff35ff5890bed2ada8808db8285df6c5e8dbffeb&v=5.74'
    addr2 = 'https://api.vk.com/method/friends.get?&order=name&fields=first_name,last_name,online&user_id=10042554&access_token=b673fdc130c04660888ea12287e13506fd820711215baff35ff5890bed2ada8808db8285df6c5e8dbffeb&v=5.107'

    a = urllib.request.urlopen(addr2)
    print(a)
    result = json.load(a)
    print(result['response']['count'])
    i = 0
    for p in result['response']['items']:
        print(p)
        i += 1
    print(i)

    answer = make_request(id, ["first_name", "last_name"])
    data = answer['response']
    count = answer['count']
    people = data['items']

    print(answer)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AS script')
    parser.add_argument('-id', type=str, action='store', default=input(),
                        help='enter the user id')
    args = parser.parse_args()

    main(args.id)
