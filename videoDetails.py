from pymediainfo import MediaInfo
media_info = MediaInfo.parse(f'/storage/emulated/0/{input(">>> path of video: ")}').tracks
print("fileSize              {}MB".format(media_info[0].other_file_size[0].split(" MiB")[0]))
print("width                 {}".format(media_info[1].width))
print("height                {}".format(media_info[1].height))
print("duration              {}".format(media_info[0].other_duration[3]))