#创建Employee类
class Employee:
    def __init__(self, name, IDnumber, department, position):
        self.name = name
        self.IDnumber = IDnumber
        self.department = department
        self.position = position

    def beStr(self):
        str = self.name + ' ' + self.IDnumber + ' ' + self.department + ' ' + self.position
        return str

    def getChange(self):
        self.name = input('Please enter the changed name:')
        self.department = input('Please enter the changed department:')
        self.position = input('Please enter the changed position:')

#加载序列化的字典，若文件不存在，则以空字典开始
def createDict(dict):
    input_txt = 'Employee.txt'
    try:
        f = open(input_txt)
        for line in f:
            str = line.strip('\n')
            str = str.split(' ')
            e1 = Employee(str[1],str[2],str[3],str[4])
            dict[str[0]] = e1
        f.close()
    except Exception as e:
        print('File does not exist. Employee dictionary is empty!!!')

#在字典中查找雇员
def searchee(dict):
    IDnumber = input("Please enter the ID of the employee you want to query")
    if IDnumber in dict.keys():
        for k in dict.keys():
            if IDnumber == k:
                print(dict[k].beStr())
                break
    else:
        print("The corresponding employee file could not be found.")

#将新员工添加到字典中
def addNewee(dict):
    name = input()
    IDnumber = input()
    department = input()
    position = input()
    newee = Employee(name, IDnumber, department, position)
    dict[IDnumber] = newee

#更改字典中现有员工的姓名、部门和职位
def changeInf(dict):
    IDnumber = input('Please enter the ID for which you want to change the information:')
    if IDnumber in dict.keys():
        for k in dict.keys():
            if IDnumber == k:
                dict[k].getChange()
                break
    else:
        print('The employees of the corresponding ID were not found.')

#从字典中删除一名员工
def deleteee(dict):
    IDnumber = input('Please enter the ID for which you want to delete:')
    if IDnumber in dict.keys():
        for k in dict.keys():
            if IDnumber == k:
                dict.pop(IDnumber)
                print('Corresponding employee information has been deleted')
                break
    else:
        print('The employees of the corresponding ID were not found.')

#序列化字典并将其保存到文件中
def saveToFile(dict):
    input_txt = 'Employee.txt'
    f = open(input_txt, 'w')
    for k, i in dict.items():
        f.write(k + ' ' + i.beStr() + '\n')
    f.close()

#显示菜单
def menu():
    print('1:在字典中查找雇员')
    print('2:将新员工添加到字典中')
    print('3:更改字典中现有员工的姓名、部门和职位')
    print('4:从字典中删除一名员工')
    print('5:退出程序')

def main():
    dict = {}
    createDict(dict)
    menu()
    choice = (int)(input('Please enter your choice：'))
    while(1):
        if choice == 1:
            searchee(dict)
        elif choice == 2:
            addNewee(dict)
        elif choice == 3:
            changeInf(dict)
        elif choice == 4:
            deleteee(dict)
        elif choice == 5:
            saveToFile(dict)
            break
        else:
            print('Invalid input!!!')
        choice = (int)(input('Please enter your choice：'))

main()

