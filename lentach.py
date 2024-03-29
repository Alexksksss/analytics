import vk_api
import json
import csv

access_token = "YOUR_TOKEN"

vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()

group_id = vk.groups.search(q = 'Лентач', count = 1)['items'][0]['id']
#print(group_id)

members = vk.groups.getMembers(group_id = group_id, count = 1000, fields = 'sex, city, relation')['items']

#print(members)

member_list = []
for member in members:
  id = member.get('id')
  sex = member.get('sex')
  relation = member.get('relation', 'не выставлен статус')
  city_str = str(member.get('city',''))
  first_index = city_str.rfind(':') + 3
  last_index = -2
  if city_str:
     city_name = city_str[first_index:last_index]
  else:
    city_name = 'не выставлен город'
  member_list.append({
      'id': id,
      'sex': sex,
      'relation': relation,
      'city_name': city_name,
  })
#print('member_list = ', member_list)

filename = "task3.csv"
f = open(filename, "w")
writer = csv.DictWriter(f, fieldnames=member_list[0].keys())
writer.writeheader()
for member in member_list:
  writer.writerow(member)