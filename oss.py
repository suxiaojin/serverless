import oss2
#上传到oss
auth=oss2.Auth('LTAI5t89QapPeFi1N42oPevW','IUQiToYURGiOD4oaAPWjEOdV52Czbl')
bucket=oss2.Bucket(auth,'oss-cn-beijing.aliyuncs.com','s-context-input  ')
bucket.put_object_from_file('cc.jpg','./zws.jpg')

