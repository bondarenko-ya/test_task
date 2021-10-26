import os
import datetime
import filecmpmod

def dir_diff(path1, path2):
    folder1 = sorted(os.listdir(path1))
    folder2 = sorted(os.listdir(path2))
    if (folder1 > folder2):
        folder_diff = (set(folder1) - set(folder2))
        return sorted(folder_diff)

#root = os.getcwd()
#root = os.path.join('logs')
root = 'logs'                                                               #храним части путей относительно скрипта по "кускам"
                                                                            #чтобы печатать в файл относительные пути тестов
                                                                            #в формате <Группа тестов>/<Конкретный тест>/                
##print (root)
if os.path.exists(root):
    logs = os.listdir(root)
##    print (logs)
    tests=[]
    for i in range(len(logs)):
        temp_paths = os.listdir(os.path.join(root,logs[i]))
##        #print(*temp_path, sep='\n')
        for j in range (len(temp_paths)):
##            print('цикл j '+logs[i])
            tests.append(os.path.join(logs[i],temp_paths[j]))
        for test in tests:
            report = open(os.path.join(root,test, "report.txt"), "w+")
##            print('цикл test '+test)
            
            ref_path = os.path.join(test, 'ft_reference') #путь к результатам теста относительно logs
            run_path = os.path.join(test, 'ft_run')
            #print(ref_path)
            #print(run_path)
           
            check_ref = os.path.exists(os.path.join(root,ref_path)) #внутрь .exists передаётся полный путь (с logs)
            check_run = os.path.exists(os.path.join(root,run_path)) #относительно положения скрипта
            if (check_ref and check_run):
                #print (os.path.join(root,ref_path), '\n', os.path.join(root,run_path))
                ref_tests = os.listdir(os.path.join(root,ref_path))
                run_tests = os.listdir(os.path.join(root,run_path))
                #print(*ref_tests, sep='\n')
                if ref_tests==run_tests:
                    pass
                else:                    
                    diff=dir_diff(os.path.join(root,ref_path), os.path.join(root,run_path))
                    another_diff = filecmpmod.dircmp(os.path.join(root,ref_path), os.path.join(root,run_path))
##                    if another_diff.left_only:
##                        print (another_diff.left_only)
                    print (another_diff.left_only)
                    if diff:
                        pass
                        #print (os.path.join(root,ref_path),diff)
                    diff=dir_diff(os.path.join(root,run_path), os.path.join(root,ref_path))
                    if diff:
                        pass
                        #print (os.path.join(root,run_path),diff)
                #report.write("OK: "+test+"\n") Если всё будет хорошо
            else:
                if not check_run or not check_ref:
                    report.write("FAIL: "+test+"\n")
                if not check_run:
                    report.write("directory missing: ft_run"+test+"\n")
                if not check_ref:
                    report.write("directory missing: ft_reference"+test+"\n")                 

else:
    with open("error_messages.txt", "a") as err_file:
        err_file.write('\n'+str(datetime.datetime.now())+'\n')
        err_file.write("Put the script in the same directory as the logs")

#print (*logs, sep='\n')
#print (*temp_paths, sep='\n')
#print (*tests, sep='\n')


