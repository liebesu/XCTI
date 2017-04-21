import argparse
from multiprocessing.pool import Pool
import os
import urllib
import requests
import MySQLdb
downloader_path='malshare'
__author__ = 'liebesu'
def downloader(hash_md5):
    apikey='a6761270a4edb516387196309b80ea6df3ca58af32335aa8283a9fd8ee587b9d'
    payload={'action':'getfile','api_key':apikey,'hash':hash_md5}
    url='http://malshare.com/sampleshare.php'
    r=requests.post(url,params=payload)
    if os.path.exists(downloader_path):
        urllib.urlretrieve(r.url,hash_md5)
        print "downloading..."
    else:
        os.makedirs(downloader_path)
        urllib.urlretrieve(r.url,hash_md5)
        print "downloading..."
'''def get_hash(num):
    db=MySQLdb.connect(host='localhost',db='virusname',user='root',passwd='polydata',port=3306,charset='utf8')
    cursor=db.cursor()
    try:
        select_sql='select MD5 from malshare ORDER BY rand() limit 0,%d'%(num)
        cursor.execute(select_sql)
        md5s=cursor.fetchall()
        cursor.close()
        db.close()
        list_md5s=[list_md5[0] for list_md5 in md5s]
        pool(list_md5s)
    except Exception as e:
        print e'''

def pool(md5s):
    pool=Pool(processes=10)
    pool.map(downloader,md5s)
    pool.close()
    pool.join()
if __name__=="__main__":
    '''parser = argparse.ArgumentParser()
    parser.add_argument("n",type=int,help="downloader virus numbers")
    args = parser.parse_args()
    num=args.n
    get_hash(num)'''
    list_md5s=['d1bdc5aaa294b4c52678c4c60f052569',
'087951566fb77fe74909d4e4828dd4cb',
'8aacf26df235661245e98cb60e820f51',
'be0d32bb3a12896ff16e3f667eb4b644',
'f388391ca443056fd3b4cc733c3b61cd',
'344324e74971148b2b537e35511cacba',
'd6113972a2173a5f81da9d37cc43bbaa',
'0a60424e0967b6cfc172dac82e10a2fe',
'76a2f2ce03df87d87a45ab7890808a40',
'2d9a3315b9ff59d1db0b7cc4624a2c87',
'f603ff7e25027ff6892118ab3ce2c07c',
'51a057635fd5d481dd9dd6f0dc316370',
'fad9ef95f3f3114b683c8c1bd9ec0f57',
'1e3e129958646257ef5fdd3daf516fb6',
'aab127f9e8a3f8ac2038d2f3ce650ced']
    for i in list_md5:
        downloader(i)

    print "downloader finihed ",num
