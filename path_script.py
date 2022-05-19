map1_path = [(0, 97), (16.0, 97.0), (66.5, 97.0), (128.0, 97.0), (189.5, 97.0), (242.0, 98.5), (266.5, 101.0), (278.0, 105.5), 
                          (285.0, 119.5), (287.0, 145.0), (287.0, 190.0), (287.0, 254.0), (281.0, 314.0), (249.5, 344.0), (193.0, 348.0), 
                          (132.0, 352.0), (100.0, 384.0), (101.5, 441.0), (133.0, 474.0), (193.0, 478.0), (256.0, 478.0), (319.0, 478.0), 
                          (382.0, 478.0), (446.0, 478.0), (512.5, 478.0), (576.5, 478.0), (638.5, 478.0), (700.5, 471.5), (731.0, 440.0), 
                          (731.0, 382.0), (731.0, 317.0), (738.0, 258.5), (774.5, 227.0), (837.0, 222.0), (883.0, 222.0), (898.0, 222.0), 
                          (32, 97), (101, 97), (155, 97), (224, 97), (260, 100), (273, 102), (283, 109), (287, 130), (287, 160), (287, 220), 
                          (287, 288), (275, 340), (224, 348), (162, 348), (102, 356), (98, 412), (105, 470), (161, 478), (225, 478), (287, 478), 
                          (351, 478), (413, 478), (479, 478), (546, 478), (607, 478), (670, 478), (731, 465), (731, 415), (731, 349), (731, 285), 
                          (745, 232), (804, 222), (870, 222), (896, 222), (900, 222)
             ]

map1_path_copy = [(0, 97), (16.0, 97.0), (66.5, 97.0), (128.0, 97.0), (189.5, 97.0), (242.0, 98.5), (266.5, 101.0), (278.0, 105.5), 
                          (285.0, 119.5), (287.0, 145.0), (287.0, 190.0), (287.0, 254.0), (281.0, 314.0), (249.5, 344.0), (193.0, 348.0), 
                          (132.0, 352.0), (100.0, 384.0), (101.5, 441.0), (133.0, 474.0), (193.0, 478.0), (256.0, 478.0), (319.0, 478.0), 
                          (382.0, 478.0), (446.0, 478.0), (512.5, 478.0), (576.5, 478.0), (638.5, 478.0), (700.5, 471.5), (731.0, 440.0), 
                          (731.0, 382.0), (731.0, 317.0), (738.0, 258.5), (774.5, 227.0), (837.0, 222.0), (883.0, 222.0), (898.0, 222.0), 
                          (32, 97), (101, 97), (155, 97), (224, 97), (260, 100), (273, 102), (283, 109), (287, 130), (287, 160), (287, 220), 
                          (287, 288), (275, 340), (224, 348), (162, 348), (102, 356), (98, 412), (105, 470), (161, 478), (225, 478), (287, 478), 
                          (351, 478), (413, 478), (479, 478), (546, 478), (607, 478), (670, 478), (731, 465), (731, 415), (731, 349), (731, 285), 
                          (745, 232), (804, 222), (870, 222), (896, 222), (900, 222)
             ]

index = 0
for index in range (0,len(map1_path) - 1):
    x1 = map1_path[index][0]
    y1 = map1_path[index][1]
    x2 = map1_path[index + 1][0]
    y2 = map1_path[index + 1][1]
    new_node = ((x1+x2)/2, (y1+y2)/2)
    map1_path_copy.insert(index + 1, new_node)
    
print(map1_path_copy)

[(0, 97), (16.0, 97.0), (66.5, 97.0), (128.0, 97.0), (189.5, 97.0), (242.0, 98.5), (266.5, 101.0), (278.0, 105.5), (285.0, 119.5), (287.0, 145.0), (287.0, 190.0), (287.0, 254.0), (281.0, 314.0), (249.5, 344.0), (193.0, 348.0), (132.0, 352.0), (100.0, 384.0), (101.5, 441.0), (133.0, 474.0), (193.0, 478.0), (256.0, 478.0), (319.0, 478.0), (382.0, 478.0), (446.0, 478.0), (512.5, 478.0), (576.5, 478.0), (638.5, 478.0), (700.5, 471.5), (731.0, 440.0), (731.0, 382.0), (731.0, 317.0), (738.0, 258.5), (774.5, 227.0), (837.0, 222.0), (883.0, 222.0), (898.0, 222.0), (32, 97), (101, 97), (155, 97), (224, 97), (260, 100), (273, 102), (283, 109), (287, 130), (287, 160), (287, 220), (287, 288), (275, 340), (224, 348), (162, 348), (102, 356), (98, 412), (105, 470), (161, 478), (225, 478), (287, 478), (351, 478), (413, 478), (479, 478), (546, 478), (607, 478), (670, 478), (731, 465), (731, 415), (731, 349), (731, 285), (745, 232), (804, 222), (870, 222), (896, 222), (900, 222)]
