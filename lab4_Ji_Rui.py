# Rui Ji, ruiji@usc.edu
# ITP 115, Spring 2021
# Lab 4

def main():


        import requests
        url = 'http://www.cxyzjd.com/article/weixin_42298645/114941568'
        data = requests.get(url)
        print(data)


main()