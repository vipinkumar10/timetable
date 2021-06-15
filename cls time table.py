# this program create a time table for a class
class xyz:
    # Days = [[], [], [], [], []]  # array of arrays name of days
    # sd = int(input("enter semester duration: \n"))        # semester duration
    # wd = sd-(int(sd/7)*2)
    # nos = int(input("enter number of subjects: \n"))
    def TT(self, sd, nos):
        Days = [[], [], [], [], []]
        wd = sd-(int(sd/7)*2)
        for s in range(nos):
            sub = input("enter subject name:\n")               # subject name
            cd = int(input("enter course duration: \n"))       # course duration
            key: float = wd/cd
            if key >= 1.0 and key<=1.5:
                for i in Days:
                    Days[Days.index(i)].append(sub)             # one lacture per day
            elif key>=1.5 and key <= 2.5:
                for i in range(0, len(Days), 2):
                    Days[i].append(sub)                         # one lacture per two day
            elif key>=2.5 and key <= 3.5:
                for i in range(0, len(Days), 3):
                    Days[i].append(sub)                         # one lacture per three day
            elif key>=3.5 and key <= 5.5:
                for i in range(0, len(Days), 4):
                    Days[i].append(sub)                         # one lacture per four day
            elif key>=5.5:
                for i in range(0, len(Days), 5):
                    Days[i].append(sub)                         # one lacture per week
        return Days
if __name__ == "__main__":
    ob1 = xyz()
    print(ob1.TT(int(input("enter semester duration:\n")),int(input("enter number of subjects:\n"))))
    