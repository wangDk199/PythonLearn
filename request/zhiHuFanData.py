"""
爬取知乎专栏粉丝数据
"""

import requests
import csv
import json

def crawl():
    url = "http://www.zhihu.com/api/v4/columns/smetalk/followers"
    header = {
        "user-agent": "Mozillla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrom/79.0.3945.130 Safari/537.36"
    }
    csvfile = open('./request/zhihuFanData.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter = ',', quoting=csv.QUOTE_All)
    keys = {'id', 'name', 'url', 'gender', 'avater_url', 'follower_count'}
    writer.writerow(keys)
    for j in range(5000):
        params = {
            'limit': 20,
            'offset': j,
            'include': "data[*].follower_count, gender, is_followers"
        }
        response = requests.get(url, headers=header, params = params)
        print("请求url:", response.url)
        print("返回的数据：", response.text)
        
        i = 1
        for dic in response.json.get("data"):
        writer.writerow([dic['id'], dic['name'], dic['url'], dic['gender'], dic['avater_url'], dic['follower_count'], ])
        i += 1
    csvfile.close

if __name__ == '__main__':
    main()

