
import datetime

def register_work(work_list):
    dt = str(datetime.datetime.now())
    print("作業内容を入力してください。")
    work = input()
    print("備考を入力してください。")
    bikou = input()
    print("こちらでよろしいですか？(y/n)")
    print("-" * 50)
    print("作業日：" + dt[:10])
    print("作業内容：" + work)
    print("備考：" + bikou)
    print("-" * 50)
    k = 0
    while k == 0:
        i = input()
        if i == "y":
            work_list.append([dt[:10], work, bikou])
            k = 1
        elif i == "n":
            print("入力を消去します")
            k = 1
        else:
            print("yまたはnを入力してください。")
            

            
def output_work(work_list):
    dt = str(datetime.datetime.now())
    print("清掃報告書")
    print("-"*50)
    print("日時：" + dt[:10])
    print("文責：松浦健悟")
    print("-"*50)
    print("="*30)
    print("作業報告")
    print("="*30)
    for i in range(len(work_list)):
        print("作業日：" + work_list[i][0])
        print("作業内容" + work_list[i][1])
        print("備考" + work_list[i][2])
        print("-"*30)

        
def write_data_to_txt(filename):
    file = open(filename, 'w')
    for i in range(len(work_list)):
        for j in range(3):
            file.write(work_list[i][j] + " ")
        file.writelines("\n")
    file.close()

if __name__ == '__main__':
    state = 1
    work_list = []
    while state == 1:
        print("何をしますか？数字を入力してください。")
        print("0：作業の登録")
        print("1：作業の出力")
        print("2：終了")
        order = int(input())
        if order == 0:
            register_work(work_list)
        elif order == 1:
            output_work(work_list)
        elif order == 2:
            print("入力したdataを保存しますか？(y/n)")
            hozon = input()
            if hozon == "y":
                dt = str(datetime.datetime.now())
                filename = str(dt[:10]) + "_work.txt"
                write_data_to_txt(filename)
                print("終了します。")
                state = 0
            elif hozon == "n":
                print("終了します。")
                state = 0
            else:
                print("入力が無効です。")
                print("-"*50)

        else:
            print("入力が無効です。")
            print("-"*50)

    state = 1