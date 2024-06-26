contents=["All carrots are to be sliced longitudinally","The carrot were repotedly sliced","Tghe slicing process was well presented"]
filenames=["doc.txt","report.txt","presentation.txt"]
for content,filename in zip(contents,filenames):
    file=open(f"file/{filename}",'w')
    file.write(content)