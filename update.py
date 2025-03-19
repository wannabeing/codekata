import os
from urllib import parse

HEADER = """# 코드카타(CodeKata)

A kata is an exercise in karate where you repeat a form many, many times, making little improvements in each.

카타는 하나의 양식을 여러 번 반복하면서 조금씩 개선하는 가라데의 운동입니다.  
SQL과 알고리즘 문제를 반복적으로 풀며 코딩 실력을 단련하고자 합니다.

"""

def main():
  content = ""
  content += HEADER
  
  directories = []
  solveds = []
  
  for root, dirs, files in os.walk("."):
    dirs.sort()
    if root == '.':
      for dir in ('.git', '.github'):
        try:
          dirs.remove(dir)
        except ValueError:
          pass
      continue
    
    category = os.path.basename(root)
    
    if category == 'images':
      continue
      
    directory = os.path.basename(os.path.dirname(root))
    
    if directory == '.':
      continue
      
    if directory not in directories:
      if directory in ["백준", "프로그래머스"]:
        content += "## 📚 {}\n".format(directory)
      else:
        content += "### 🚀 LEVEL {}\n".format(directory)
        content += "| 문제번호 | 링크 |\n"
        content += "| ----- | ----- |\n"
      directories.append(directory)
      
    for file in files:
      if category not in solveds:
        content += "|{}|[링크]({})|\n".format(category, parse.quote(os.path.join(root, file)))
        solveds.append(category)
        
  with open("README.md", "w") as fd:
    fd.write(content)
    
if __name__ == "__main__":
  main()
