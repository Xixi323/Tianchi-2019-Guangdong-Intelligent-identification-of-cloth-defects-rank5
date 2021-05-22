import json

json_file1 = "/content/mjcdrive/MyDrive/data/fabric/Annotations/anno_train_20190925.json"
json_file2 = "/content/mjcdrive/MyDrive/data/fabric/Annotations/anno_train_20191008.json"
save_json = "/content/mjcdrive/MyDrive/data/fabric/Annotations/anno_train_round2.json"
with open(json_file1, 'r') as f1:
    anno1 = json.load(f1)

with open(json_file2, 'r') as f2:
    anno2 = json.load(f2)

anno1.extend(anno2)
with open(save_json, 'w') as fp:
    json.dump(anno1, fp, indent=4, separators=(',', ': '))
