import os
import subprocess
import sys

# # print(os.environ.get("ADB",""))
# # argument = sys.argv[1]
# # # print(os.system(""))
# # print(argument)
# # if not os.path.exists(argument):
# #     with open(argument,"w") as f:
# #         f.write("new file")
# #         print("doesnt exists")
# # subprocess.run("ping 8.8.8.8")
# # result = subprocess.run(["nslookup","8.8.8.8"],capture_output=True)
# # print(result.stdout.decode("UTF-8"))
# #
# # completed = subprocess.run(["powershell", "-Command", "Get-ChildItem -Name"], capture_output=True)
# # print(completed.stdout.decode())
# log = sys.argv[1]
# with open(log) as f:
#     for line in f:
#         if not "migrating" in line:
#             continue
#         print(line)
# print("read ended")
import re
def show_time_of_pid(line):
  assert type(line) == str,"line must be string"
  pattern = "Jul \d \d\d:\d\d:\d\d"
  result = re.search(pattern, line)
  if(result == None):
    return ;
  return result.group()

def example():
  print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

  print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

  print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

  print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

  print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

  print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

  print(show_time_of_pid(" ")) # Jul 6 14:05:01 pid:29440

if __name__ == '__main__':
    example()