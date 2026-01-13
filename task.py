# TODO Напишите функцию find_common_participants
def find_common_participants(g1, g2, sep=','):
    l1 = g1.split(sep)
    l2 = g2.split(sep)
    common = [x for x in l1 if x in l2]
    return sorted(set(common))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, sep='|')
print("Общие участники:", result)
# TODO Провеьте работу функции с разделителем отличным от запятой