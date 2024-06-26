'''member=input("Add a new member:")
file=open("members.txt",'r')
existing_members=file.readlines()
file.close()
member=member.title()
existing_members.append(member+'\n')
file=open("members.txt",'w')
exisiting_members=file.writelines(existing_members)
file.close()'''
filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for filename in filenames:
    file=open(f"file/{filename}",'w')
    file.writelines("hello this is sidra")
    file.close()


