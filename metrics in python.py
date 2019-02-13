import csv

def rmse():
  with open('mae.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    s=0
    count=0
    for row in csv_reader:
      # print(f'{row[0]}\t{row[1]}\t{row[2]}')
      s=s+abs(float(row[1])-float(row[2]))**2
      count=count+1
    print("Root Mean Square Error is", (s/count)**0.5)

def nrmse():
  with open('mae.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    s=0
    count=0
    maxi=-99999999
    mini=99999999
    for row in csv_reader:
      s=s+abs(float(row[1])-float(row[2]))**2
      count=count+1
      if maxi<float(row[1]):
        maxi=float(row[1])
      if mini>float(row[1]):
        mini=float(row[1])
    print("Normalised Root Mean Square Error is", ((s/count)**0.5)*100/abs(maxi-mini))


def mae():
  with open('mae.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    s=0
    count=0
    for row in csv_reader:
      # print(f'{row[0]}\t{row[1]}\t{row[2]}')
      s=s+abs(float(row[1])-float(row[2]))
      count=count+1
    print(f"Mean Absolute Error is {s/count}")

def precision(tp,fp):
  return (tp/(tp+fp))

def recall(tp,fn):
  return (tp/(tp+fn))

def fmeasure(r,p):
  return (2*p*r/(p+r))

def ndcg():
  with open('ndcg.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    s=0
    count=0
    maxi=-99999999
    # print(f'{row[0]}\t{row[1]}\t{row[2]}')
    s=s+int(row[0])
    if maxi<float(row[0]):
      maxi=float(row[0])
      count=count+1
    print("Normalized Discounted Cumulative Gain",s*100/(count*maxi))

print("Choose one from the following:")
print("1)Root Mean Sqaure Error")
print("2)Normalized Root Mean Square Error")
print("3)Mean Absolute Error")
print("4)F-Measure(F1 Score)")
print("5)Precision")
print("6)Recall")
print("7)Normalized Discounted Cumulative Gain")
print("0)Exit")
x=int(input())
while x!=0:
  if x==1:
    rmse()

  elif x==2:
    nrmse()

  elif(x==3):
    mae()

  elif(x==4):
    print("Enter tp,fp,tn values in order:")
    tp=int(input())
    fp=int(input())
    fn=int(input())
    r=recall(tp,fn)
    p=precision(tp,fp)
    print("F-Measure value is", fmeasure(r,p))

  elif(x==5):
    print("Enter tp,fp values in order:")
    tp=int(input())
    fp=int(input())
    print("Precision Value is ",precision(tp,fp))

  elif(x==6):
    print("Enter tp,fn values in order:")
    tp=int(input())
    fn=int(input())
    print("Recall Value is ",recall(tp,fn))

  elif x==7:
    ndcg()

  else:
    print("Enter a valid Input")
  x=int(input())

