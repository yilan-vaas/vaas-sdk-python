# encoding: utf-8
import sys

# 测试模块
sys.path.append('../src/vaas/')
import vaas
import report
import credentials


# 频道相关
def test_channel(vaas):
    print("\n ###获取频道数据### \n")
    channels = vaas.channels()
    print(channels)


# 推荐相关
def test_recommend(vaas):
    print("\n ###获取视频信息流数据### \n")
    video_type = 1
    channel_id = 10175
    feed = vaas.feed(video_type, channel_id)
    print(feed)

    print("\n ###获取相关视频数据### \n")
    id = 'Jy8nbGGXEJjR'
    relation = vaas.relation(id)
    print(relation)


# 视频、cp相关
def test_video(vaas):
    print("\n ###获取作者详情### \n")
    id = '28yJYbZwR65k'
    video_type = 1
    # video_type = 2
    cpInfo = vaas.cpinfo(id, video_type)
    print(cpInfo)

    print("\n ###获取视频详情### \n")
    ids = 'gjwbEJZnV0MV,EjVx74kPNoyQ'
    video_type = 1
    # ids = 'eJMeOJN9B5KX,ZVjkOgN0WjGp'
    # video_type = 2
    detail = vaas.detail(ids, video_type)
    print(detail)

    print("\n ###获取作者视频列表### \n")
    # id = 'pbjDYWR0P52N'
    # video_type = 1
    id = 'RJj017XJvx58'
    video_type = 2
    cpVideos = vaas.cpvideos(id, video_type)
    print(cpVideos)

    print("\n ###获取播放数据### \n")
    id = 'njz3Dn7N1r5V'
    plays = vaas.play(id)
    print(plays)


def test_report(report):
    print("\n ###视频曝光上报### \n")
    videoid = 'gjwbEJZnV0MV'
    referpage = 'channel_100'
    pos = 1
    ret = report.videoshow(videoid, referpage, pos)
    print(ret)

    print("\n ###点击播放上报### \n")
    videoid = 'gjwbEJZnV0MV'
    referpage = 'channel_100'
    ret = report.videoplay(videoid, referpage)
    print(ret)

    print("\n ###播放时长上报### \n")
    videoid = 'gjwbEJZnV0MV'
    bt = 1622527513
    et = 1622527523
    rt = 0
    ret = report.videoplaytm(videoid, bt, et, rt)
    print(ret)

    print("\n ###视频反馈上报### \n")
    videoid = 'gjwbEJZnV0MV'
    cpid = 'nJ5vdO8kr8MV'
    action = 'like'
    ret = report.videofeedback(videoid, cpid, action)
    print(ret)


if __name__ == '__main__':
    # 设置公共参数
    credentials = credentials.Credentials()
    credentials.set_key('')
    credentials.set_token('')
    credentials.set_pkgname('')
    credentials.set_platform(2)
    # 设备唯一标识，客户端生成
    udid = '5459daf640bdb6a6a7e294a5f3f5f0d1'
    vaas = vaas.Vaas(udid)
    report = report.Report(udid)
    # 频道相关
    test_channel(vaas)
    # 推荐相关
    test_recommend(vaas)
    # 视频作者相关
    test_video(vaas)
    # 数据上报相关
    test_report(report)
