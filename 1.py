filename = tkinter.filedialog.askopenfilename() 
        name = Path(filename).stem  
        pathname = os.path.splitext(filename)[0]  

        # ls = filename
        suffix = filename[filename.rfind('.') + 0:] 
        suffix2 = os.path.dirname(filename)  # 获得文件路径
        self.suffix2= suffix2
        
        
with open(filename, "rb") as f:
     with open(pathname + "破解" + suffix, "wb") as f1:  # 写文件
         f.seek(0)  # 光标移动到开头
                for x in list_dec:
                    a = struct.pack('B', x)
                    f1.write(a)
                while True:
                    old = f.read(1024000000)
                    f1.write(old)
                    if not old:
                        break
#gui使用可视化pyqt5(qt设计师),头文件自己导入,目前还在优化,解耦合,现阶段乱七八糟的就不放出来了
