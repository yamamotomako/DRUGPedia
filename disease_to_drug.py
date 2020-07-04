#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import re


db_path = "./H29DB"

target_str = sys.argv[1]
#target_str = "アトピー リウマチ"
target_arr = filter(lambda x: x != "", target_str.split(" "))

with open(db_path+"/drug_disease_ja.txt", "r") as f:
    lines = f.read().rstrip("\n").split("\n")

    hit_drug = []
    for line in lines:
        hit_arr = []
        for t in target_arr:
            if line.find(t) >= 0:
                hit_arr.append(True)
            else:
                hit_arr.append(False)

        if all(hit_arr):
            hit_drug.append(line.split("\t")[0])



drug_dict = {}
drug_dict_ja = {}

with open(db_path+"/drug.txt", "r") as f:
    lines = f.read().rstrip("\n").split("\n")
    for line in lines:
        data = line.split("\t")
        drug_dict[data[0]] = data[1]

with open(db_path+"/drug_ja.txt", "r") as f:
    lines = f.read().rstrip("\n").split("\n")
    for line in lines:
        data = line.split("\t")
        drug_dict_ja[data[0]] = data[1]


indc_dict = {}
with open(db_path+"/indications.txt", "r") as f:
    lines = f.read().rstrip("\n").split("\n")
    for line in lines:
        if line[:4] == "KEGG":
            kegg_drug_id = line.split("\t")[1]
            if not indc_dict.has_key(kegg_drug_id):
                indc_dict[kegg_drug_id] = []
            arr = [""]*2
            continue

        if line[:5] == "JAPIC":
            japic_num = line.split("\t")[1]
            arr[0] = japic_num
            continue

        if line[:9] == "商品名":
            product_name = line.split("\t")[1]
            arr[1] = product_name
            continue

        if line[:3] == "///":
            indc_dict[kegg_drug_id].append(arr)
            continue



result_str = ""
for drug_id in hit_drug:

    r = re.compile('(.+)\(.+\)')
    m = r.search(drug_dict[drug_id])

    if m != None:
        drug_en = m.group(1)[:-1]
    else:
        drug_en = drug_dict[drug_id]


    r = re.compile('(.+)\(.+\)')
    m = r.search(drug_dict_ja[drug_id])
    if m != None:
        drug_ja = m.group(1)[:-1]
    else:
        drug_ja = drug_dict_ja[drug_id]


    str = ""
    for buf in indc_dict[drug_id]:
        str += buf[0]+"_"+buf[1]+","

    result_str += drug_id+"|"+drug_en+"|"+drug_ja+"|"+str[:-1]+"|||"


print result_str[:-3]
