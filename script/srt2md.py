#!/usr/bin/python
import sys, getopt, re

def main(argv):
    # 参数处理
    season = ''
    episode = ''

    help_string = 'srt2md.py -s <season> -e <episode>'

    try:
        opts, args = getopt.getopt(argv, "hs:e:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print(help_string)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(help_string)
            sys.exit()
        elif opt in ('-s', '--season'):
            season = arg
        elif opt in ('-e', '--episode'):
            episode = arg

    file_path = "../subtitle/%s/How I Met Your Mother S%sE%s.srt" % (season, season, episode)
    print("开始处理第 %s 季第 %s 集，字幕文件：%s" % (season, episode, file_path))

    write_file_path = "../docs/s%s/e%s/README.md" % (season, episode)
    
    srt2md(file_path, write_file_path)

def srt2md(file_path, write_file_path):
    # 打开文件
    try:
        f = open(file_path, 'rb')
        wf = open(write_file_path, 'w')
        write_string_template = "| ID | Time | ZH | EN | Words | Remarks |\n| ---- | ---- | ---- | ---- | ---- | ---- |\n"
        wf.write(write_string_template)
        lines = f.readlines()
        for line in lines:
            # 对字符串处理
            line = line.decode('gbk') # 文件为 GBK 编码
            line = line.replace('\n', '').replace('\r', '')

            # 匹配到数字：开始组合字符串
            digit_pattern = re.compile("^\d+\s*$") # 匹配数字行
            if digit_pattern.match(line):
                # print(line)
                write_string = "| %s |" % line
                continue

            # 匹配时间轴
            # ?? 匹配 --> 为什么不能成功
            time_pattern = re.compile("\d+")
            if time_pattern.match(line):
                line = line.replace(":", ".")
                write_string += " %s |" % line
                continue

            # 匹配中英文字幕
            subtitle_pattern = re.compile("{(.*)?}(.*)?{(.*)?}")
            subtitle_match = subtitle_pattern.match(line)
            if subtitle_match:
                subtitle = subtitle_match.group(2)
                write_string += " %s |" % subtitle
                continue

            # print(line)

            # 上述都未匹配，可写入文件
            write_string += '\n'
            # print(write_string)
            wf.write(write_string)

        # 关闭文件
        wf.close()
        f.close()
    except FileNotFoundError:
        print("%s not found" % file_path)
        sys.exit(2)
    

if __name__ == "__main__":
    main(sys.argv[1:])