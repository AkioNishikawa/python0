%matplotlib  inline
import  pandas  as  pd
import  matplotlib.pyplot  as  plt

data = {
    "math" : [100, 85, 90, 95,80, 80,75, 65, 65, 60, 55, 45, 45]
    "sci" : [94, 90, 95, 90, 85, 80, 75, 70, 60, 60, 50, 50, 48]
  "social" : [80, 88, 70, 62, 86, 70, 79, 65, 75, 67, 75, 68, 60]
}
df = pd.DataFrame(data)
df.head()

