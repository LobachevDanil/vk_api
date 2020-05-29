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
    answer = urllib.request.urlopen(data)
    return json.load(answer)


def main(id):
    try:
        answer = make_request(id, ["first_name", "last_name"])
    except Exception as e:
        print("An error occurred when making the request")
        print(e)
    if 'error' in answer:
        print("An unexpected error occurred")
        return

    data = answer['response']
    count = data['count']
    people = data['items']

    print(str(count) + " friends were found")
    header = '{0:<8}{1:^40}{2:<10}'.format("Number", "Name", "ID")
    print(header)
    for i in range(count):
        user = people[i]
        if user['first_name'] != 'DELETED':
            row = "{0:<8}{1:^40}{2:<10}".format(i + 1, user['first_name'] + " " + user['last_name'], user['id'])
            print(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AS script')
    parser.add_argument('-id', type=str, action='store', default=input(),
                        help='enter the user id')
    args = parser.parse_args()

    main(args.id)
