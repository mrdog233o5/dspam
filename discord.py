from header import *

# get inputs from user
def getopt():
    p.aprint("target channel id > ", end="")
    channelId = input("")
    p.aprint("your token > ", end="")
    token = input("")
    p.aprint("enter the spam message > ", end="")
    message = input("")
    p.aprint("sleep time (seconds) > ", end="")
    sleepTime = int(input(""))
    return channelId, token, message, sleepTime
    

def spam(channelId, token, message, sleepTime):
    while 1:
        url = f"https://discord.com/api/v9/channels/{channelId}/messages"

        headers = {
            "Authorization": f"{token}"
        }
        json = {
            "content": message
        }
        req = requests.post(url, headers = headers, json = json)
        print(f"message sent: {req}")
        time.sleep(sleepTime)

def main():
    channelId, token, message, sleepTime = getopt()
    spam(channelId, token, message, sleepTime)

if __name__ == "__main__":
    main()
